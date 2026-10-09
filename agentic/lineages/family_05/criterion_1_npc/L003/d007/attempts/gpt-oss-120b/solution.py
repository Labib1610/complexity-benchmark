import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # columns: 0..C-1, where C = 3*k
    C = 3 * k
    # column ids for convenience
    def col_x(x): return x - 1               # 0 .. k-1
    def col_y(y): return k + (y - 1)         # k .. 2k-1
    def col_z(z): return 2 * k + (z - 1)     # 2k .. 3k-1

    rows = []          # each row: (x,y,z)
    # dancing links structures
    max_nodes = t * 3 + C + 5
    left = [0] * max_nodes
    right = [0] * max_nodes
    up = [0] * max_nodes
    down = [0] * max_nodes
    col = [0] * max_nodes          # column of node
    row_id = [0] * max_nodes       # which input row the node belongs to
    size = [0] * C                 # number of nodes in each column

    # header node 0, column headers 1..C
    header = 0
    for i in range(C + 1):
        left[i] = i - 1
        right[i] = i + 1
        up[i] = down[i] = i
    right[C] = header
    left[header] = C

    node_cnt = C + 1   # next free index

    # add a row (list of three column numbers)
    def add_row(rid, cols):
        nonlocal node_cnt
        first = None
        for c in cols:
            nd = node_cnt
            node_cnt += 1
            col[nd] = c
            row_id[nd] = rid

            # vertical links
            up[nd] = up[c + 1]
            down[nd] = c + 1
            down[up[nd]] = nd
            up[down[nd]] = nd
            size[c] += 1

            # horizontal links
            if first is None:
                left[nd] = right[nd] = nd
                first = nd
            else:
                left[nd] = left[first]
                right[nd] = first
                right[left[first]] = nd
                left[first] = nd

    for idx in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        rows.append((x, y, z))
        add_row(idx, [col_x(x), col_y(y), col_z(z)])

    # cover / uncover operations
    def cover(c):
        # remove column header
        left[right[c]] = left[c]
        right[left[c]] = right[c]
        # remove rows
        i = down[c]
        while i != c:
            j = right[i]
            while j != i:
                up[down[j]] = up[j]
                down[up[j]] = down[j]
                size[col[j]] -= 1
                j = right[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                size[col[j]] += 1
                up[down[j]] = j
                down[up[j]] = j
                j = left[j]
            i = up[i]
        left[right[c]] = c
        right[left[c]] = c

    solution = []

    def search():
        if right[header] == header:          # all columns covered
            return True
        # choose column with minimal size
        c = right[header]
        min_sz = size[c - 1]
        cc = c
        j = right[c]
        while j != header:
            if size[j - 1] < min_sz:
                min_sz = size[j - 1]
                cc = j
                if min_sz == 0:
                    break
            j = right[j]
        if min_sz == 0:
            return False
        cover(cc)
        r = down[cc]
        while r != cc:
            solution.append(row_id[r])
            j = right[r]
            while j != r:
                cover(col[j] + 1)
                j = right[j]
            if search():
                return True
            # backtrack
            j = left[r]
            while j != r:
                uncover(col[j] + 1)
                j = left[j]
            solution.pop()
            r = down[r]
        uncover(cc)
        return False

    # column numbers in dancing links are 1‑based (header is 0)
    # we stored sizes indexed by 0..C-1, so when covering we use c = column+1
    # adjust functions accordingly
    # rewrite cover/uncover to accept column index (0‑based) and add 1 internally
    # but for simplicity we re‑map: when calling cover/uncover we pass column+1

    # modify search to use column+1
    def cover(col0):
        c = col0 + 1
        left[right[c]] = left[c]
        right[left[c]] = right[c]
        i = down[c]
        while i != c:
            j = right[i]
            while j != i:
                up[down[j]] = up[j]
                down[up[j]] = down[j]
                size[col[j] - 1] -= 1
                j = right[j]
            i = down[i]

    def uncover(col0):
        c = col0 + 1
        i = up[c]
        while i != c:
            j = left[i]
            while j != i:
                size[col[j] - 1] += 1
                up[down[j]] = j
                down[up[j]] = j
                j = left[j]
            i = up[i]
        left[right[c]] = c
        right[left[c]] = c

    # redo search with corrected functions
    solution.clear()

    def search():
        if right[header] == header:
            return True
        # choose column with minimal size
        c = right[header]
        best = c
        min_sz = size[col[c] - 1] if c != header else 0
        j = right[c]
        while j != header:
            sz = size[col[j] - 1]
            if sz < min_sz:
                min_sz = sz
                best = j
                if sz == 0:
                    break
            j = right[j]
        if min_sz == 0:
            return False
        cover(col[best] - 1)
        r = down[best]
        while r != best:
            solution.append(row_id[r])
            j = right[r]
            while j != r:
                cover(col[j] - 1)
                j = right[j]
            if search():
                return True
            # backtrack
            j = left[r]
            while j != r:
                uncover(col[j] - 1)
                j = left[j]
            solution.pop()
            r = down[r]
        uncover(col[best] - 1)
        return False

    # start search
    if search():
        out = ["YES"]
        for idx in solution:
            x, y, z = rows[idx]
            out.append(f"{x} {y} {z}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()