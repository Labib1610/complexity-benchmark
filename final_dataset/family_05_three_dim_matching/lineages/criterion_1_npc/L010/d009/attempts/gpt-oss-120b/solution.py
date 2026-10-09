import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triples.append((a, b, c))

    ncol = 3 * k                     # total columns
    max_nodes = t * 3 + ncol + 1    # header + column headers + all nodes

    # dancing‑links arrays
    left = [0] * max_nodes
    right = [0] * max_nodes
    up = [0] * max_nodes
    down = [0] * max_nodes
    col = [0] * max_nodes           # column of a node
    row_of_node = [0] * max_nodes   # which input row a node belongs to
    size = [0] * (ncol + 1)         # number of rows in each column

    # header (0) linked with column headers 1..ncol
    right[0] = 1 if ncol else 0
    left[0] = ncol if ncol else 0
    for i in range(1, ncol + 1):
        left[i] = i - 1
        right[i] = i + 1 if i < ncol else 0
        up[i] = down[i] = i
        size[i] = 0

    node_id = ncol + 1               # first free node index

    for idx, (a, b, c) in enumerate(triples):
        cols = [a, k + b, 2 * k + c]   # 1‑based column numbers
        first = -1
        prev = -1
        for cc in cols:
            nd = node_id
            node_id += 1
            col[nd] = cc
            row_of_node[nd] = idx

            # vertical links (insert just above column header)
            up[nd] = up[cc]
            down[nd] = cc
            down[up[cc]] = nd
            up[cc] = nd
            size[cc] += 1

            # horizontal links inside the row
            if first == -1:
                first = nd
                left[nd] = right[nd] = nd
            else:
                left[nd] = prev
                right[nd] = right[prev]
                left[right[prev]] = nd
                right[prev] = nd
            prev = nd

    solution_rows = []

    sys.setrecursionlimit(10000)

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

    def search() -> bool:
        if right[0] == 0:          # all columns covered
            return True
        # choose column with minimal size
        c = right[0]
        s = size[c]
        j = right[c]
        while j != 0:
            if size[j] < s:
                s = size[j]
                c = j
                if s == 0:
                    break
            j = right[j]
        if s == 0:
            return False
        cover(c)
        r = down[c]
        while r != c:
            solution_rows.append(row_of_node[r])
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
        for idx in solution_rows:
            a, b, c = triples[idx]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()