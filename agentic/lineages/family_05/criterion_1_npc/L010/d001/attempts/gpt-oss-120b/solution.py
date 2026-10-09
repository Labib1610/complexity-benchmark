import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    rows = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        rows.append((x, y, z))

    # DLX implementation
    n_cols = 3 * k                     # columns: specialists 0..k-1, machines k..2k-1, times 2k..3k-1
    max_nodes = t * 3 + n_cols + 1    # each row has 3 nodes

    # header node is 0
    left = [0] * (max_nodes)
    right = [0] * (max_nodes)
    up = [0] * (max_nodes)
    down = [0] * (max_nodes)
    col = [0] * (max_nodes)
    row_id = [0] * (max_nodes)

    size = [0] * (n_cols)   # size of each column

    # initialise column headers (1..n_cols)
    for i in range(n_cols + 1):
        left[i] = i - 1
        right[i] = i + 1
        up[i] = down[i] = i
    left[0] = n_cols
    right[n_cols] = 0

    node_cnt = n_cols + 1  # next free node index

    def add_node(r, c):
        nonlocal node_cnt
        idx = node_cnt
        node_cnt += 1
        col[idx] = c
        row_id[idx] = r

        # vertical links
        up[idx] = up[c]
        down[idx] = c
        down[up[c]] = idx
        up[c] = idx
        size[c] += 1

        return idx

    # build rows
    for r, (x, y, z) in enumerate(rows):
        first = None
        for c in (x, k + y, 2 * k + z):
            nd = add_node(r, c + 1)   # column numbers are 1‑based in DLX
            if first is None:
                first = nd
            else:
                # horizontal links
                left[nd] = left[first]
                right[nd] = first
                right[left[first]] = nd
                left[first] = nd

    # cover / uncover operations
    def cover(c):
        # remove column header
        left[right[c]] = left[c]
        right[left[c]] = right[c]
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

    solution_rows = []

    sys.setrecursionlimit(10000)

    def search():
        if right[0] == 0:          # all columns covered
            return True
        # choose column with minimal size
        c = right[0]
        min_sz = size[c - 1]
        cc = c
        j = right[c]
        while j != 0:
            if size[j - 1] < min_sz:
                min_sz = size[j - 1]
                cc = j
                if min_sz == 0:
                    break
            j = right[j]
        c = cc
        if min_sz == 0:
            return False

        cover(c)
        r = down[c]
        while r != c:
            solution_rows.append(row_id[r])
            j = right[r]
            while j != r:
                cover(col[j])
                j = right[j]
            if search():
                return True
            # backtrack
            j = left[r]
            while j != r:
                uncover(col[j])
                j = left[j]
            solution_rows.pop()
            r = down[r]
        uncover(c)
        return False

    if search():
        out = ["YES"]
        for rid in solution_rows:
            x, y, z = rows[rid]
            out.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()