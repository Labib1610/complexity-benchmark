import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        triples.append((a, b, c))

    n = 3 * q                     # number of columns (elements)

    # ---------- Dancing Links structures ----------
    # column header nodes: 0..n (0 is the root)
    size = [0] * (n + 1)          # number of rows in each column
    up = list(range(n + 1))
    down = list(range(n + 1))
    left = [0] * (n + 1)
    right = [0] * (n + 1)

    for i in range(n + 1):
        left[i] = i - 1
        right[i] = i + 1
    left[0] = n
    right[n] = 0

    # row nodes will be stored in arrays; each node knows its column and row id
    col = []      # column of node i
    row = []      # row id of node i
    L = []        # left neighbor in row
    R = []        # right neighbor in row

    row_head = []   # for each row, index of one of its nodes

    def add_node(rid, c):
        idx = len(col)
        col.append(c)
        row.append(rid)
        L.append(0)
        R.append(0)

        # insert into column c at the bottom (just above header)
        up_idx = up[c]
        down_idx = c
        up.append(up_idx)
        down.append(down_idx)

        down[up_idx] = idx
        up[c] = idx

        size[c] += 1
        return idx

    for rid, (a, b, c) in enumerate(triples):
        nodes = [add_node(rid, a), add_node(rid, b), add_node(rid, c)]
        # link the three nodes circularly
        for i in range(3):
            L[nodes[i]] = nodes[(i - 1) % 3]
            R[nodes[i]] = nodes[(i + 1) % 3]
        row_head.append(nodes[0])

    # ---------- DLX operations ----------
    def cover(c):
        # remove column header
        right[left[c]] = right[c]
        left[right[c]] = left[c]
        # for each row i in column c
        i = down[c]
        while i != c:
            j = R[i]
            while j != i:
                # remove node j from its column
                down[up[j]] = down[j]
                up[down[j]] = up[j]
                size[col[j]] -= 1
                j = R[j]
            i = down[i]

    def uncover(c):
        i = up[c]
        while i != c:
            j = L[i]
            while j != i:
                size[col[j]] += 1
                down[up[j]] = j
                up[down[j]] = j
                j = L[j]
            i = up[i]
        right[left[c]] = c
        left[right[c]] = c

    solution_rows = []

    def search(k=0):
        if right[0] == 0:          # no columns left
            return True
        # choose column with minimal size
        c = right[0]
        min_sz = size[c]
        j = right[c]
        while j != 0:
            if size[j] < min_sz:
                c = j
                min_sz = size[j]
                if min_sz == 0:
                    break
            j = right[j]
        if min_sz == 0:
            return False

        cover(c)
        r = down[c]
        while r != c:
            solution_rows.append(row[r])
            j = R[r]
            while j != r:
                cover(col[j])
                j = R[j]
            if search(k + 1):
                return True
            # backtrack
            j = L[r]
            while j != r:
                uncover(col[j])
                j = L[j]
            solution_rows.pop()
            r = down[r]
        uncover(c)
        return False

    if search():
        out = ["YES"]
        for rid in solution_rows:
            out.append(' '.join(map(str, triples[rid])))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()