import sys

sys.setrecursionlimit(10000)

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
        rows.append((x, y + k, z + 2 * k))   # column indices

    ncol = 3 * k
    # DLX structures
    max_nodes = t * 3 + ncol + 1
    left = [0] * max_nodes
    right = [0] * max_nodes
    up = [0] * max_nodes
    down = [0] * max_nodes
    col = [0] * max_nodes
    row_id = [0] * max_nodes
    size = [0] * (ncol + 1)   # column header sizes, header 0 is root

    # header node 0 is root
    for i in range(ncol + 1):
        left[i] = i - 1
        right[i] = i + 1
        up[i] = down[i] = i
    left[0] = ncol
    right[ncol] = 0

    node_cnt = ncol + 1

    # add rows
    for r_idx, cols in enumerate(rows):
        first = -1
        for c in cols:
            node = node_cnt
            node_cnt += 1
            col[node] = c + 1          # column headers are 1..ncol
            row_id[node] = r_idx
            # vertical links
            up[node] = up[col[node]]
            down[node] = col[node]
            down[up[node]] = node
            up[col[node]] = node
            size[col[node]] += 1
            # horizontal links
            if first == -1:
                left[node] = right[node] = node
                first = node
            else:
                left[node] = left[first]
                right[node] = first
                right[left[node]] = node
                left[first] = node

    solution_rows = []

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

    def search():
        if right[0] == 0:   # all columns covered
            return True
        # choose column with minimal size
        c = right[0]
        min_sz = size[c]
        cc = c
        j = right[c]
        while j != 0:
            if size[j] < min_sz:
                min_sz = size[j]
                cc = j
                if min_sz == 0:
                    break
            j = right[j]
        if min_sz == 0:
            return False
        cover(cc)
        r = down[cc]
        while r != cc:
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
        uncover(cc)
        return False

    if search():
        out = ["YES"]
        for idx in solution_rows:
            x, y, z = rows[idx]
            out.append(f"{x+1} {y - k +1} {z - 2*k +1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()