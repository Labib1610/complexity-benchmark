import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    routes = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        routes.append((x, y, z))

    n_cols = 3 * k  # source, transformer, destination columns

    # DLX structures
    max_nodes = t * 3 + n_cols + 1
    left = [0] * max_nodes
    right = [0] * max_nodes
    up = [0] * max_nodes
    down = [0] * max_nodes
    col = [0] * max_nodes
    row_id = [0] * max_nodes
    size = [0] * (n_cols + 1)  # column sizes, header is 0

    header = 0
    # header linked to column headers 1..n_cols
    for i in range(n_cols + 1):
        left[i] = i - 1
        right[i] = i + 1
        up[i] = down[i] = i
    right[n_cols] = header
    left[header] = n_cols

    node_cnt = n_cols + 1  # next free index

    # add rows
    for r_idx, (x, y, z) in enumerate(routes):
        cols = [1 + x, 1 + k + y, 1 + 2 * k + z]  # column numbers (1‑based after header)
        first = -1
        for c in cols:
            nd = node_cnt
            node_cnt += 1
            col[nd] = c
            row_id[nd] = r_idx

            # vertical links
            up[nd] = up[c]
            down[nd] = c
            down[up[c]] = nd
            up[c] = nd
            size[c] += 1

            # horizontal links
            if first == -1:
                left[nd] = right[nd] = nd
                first = nd
            else:
                left[nd] = left[first]
                right[nd] = first
                right[left[first]] = nd
                left[first] = nd

    solution_rows = []

    def cover(c):
        # remove column header
        left[right[c]] = left[c]
        right[left[c]] = right[c]
        # remove rows
        i = down[c]
        while i != c:
            j = right[i]
            while j != i:
                down[up[j]] = down[j]
                up[down[j]] = up[j]
                size[col[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                size[col[j]] += 1
                down[up[j]] = j
                up[down[j]] = j
                j = left[j]
            i = up[i]
        left[right[c]] = c
        right[left[c]] = c

    found = False

    def search(depth):
        nonlocal found
        if right[header] == header:
            # all columns covered
            found = True
            return True
        # choose column with minimal size
        c = right[header]
        min_s = size[c]
        cc = c
        j = right[c]
        while j != header:
            if size[j] < min_s:
                min_s = size[j]
                cc = j
                if min_s == 0:
                    break
            j = right[j]
        if min_s == 0:
            return False
        cover(cc)
        r = down[cc]
        while r != cc:
            solution_rows.append(row_id[r])
            j = right[r]
            while j != r:
                cover(col[j])
                j = right[j]
            if search(depth + 1):
                return True
            # backtrack
            j = left[r]
            while j != r:
                uncover(col[j])
                j = left[j]
            solution_rows.pop()
            r = down[r]
        uncover(cc)
        return False

    if search(0):
        out = ["YES"]
        for idx in solution_rows:
            x, y, z = routes[idx]
            out.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()