import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))

    # ----- DLX construction -----
    # columns: 0..k-1   -> X
    #          k..2k-1 -> Y
    #          2k..3k-1-> Z
    C = 3 * k                     # number of columns
    max_nodes = t * 3 + C + 1     # +1 for header

    # link arrays
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    col = [0] * max_nodes        # column of each node
    size = [0] * (C + 1)         # size of each column, 0 is header

    # header node is 0
    for i in range(C + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = C
    R[C] = 0

    node_id = C + 1               # next free node index
    row_of_node = [0] * max_nodes   # to retrieve triple later
    # store triples index per row
    row_head = []                 # first node of each row

    for r_idx, (x, y, z) in enumerate(triples):
        cols = [x, k + y, 2 * k + z]
        first = None
        for c in cols:
            nd = node_id
            node_id += 1
            col[nd] = c + 1          # columns are 1‑based in DLX
            # vertical links (insert above header)
            U[nd] = U[col[nd]]
            D[nd] = col[nd]
            D[U[nd]] = nd
            U[D[nd]] = nd
            size[col[nd]] += 1

            if first is None:
                first = nd
                L[nd] = R[nd] = nd
            else:
                # horizontal insertion at the end of the row list
                L[nd] = L[first]
                R[nd] = first
                R[L[nd]] = nd
                L[first] = nd
            row_of_node[nd] = r_idx
        row_head.append(first)

    # ----- DLX operations -----
    def cover(c):
        # remove column header
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                size[col[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[col[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c

    solution_rows = []

    def search():
        if R[0] == 0:          # no columns left
            return True
        # choose column with minimal size
        c = R[0]
        min_sz = size[c]
        j = R[c]
        while j != 0:
            if size[j] < min_sz:
                c = j
                min_sz = size[j]
                if min_sz == 0:
                    break
            j = R[j]
        if min_sz == 0:
            return False
        cover(c)
        r = D[c]
        while r != c:
            solution_rows.append(row_of_node[r])
            j = R[r]
            while j != r:
                cover(col[j])
                j = R[j]
            if search():
                return True
            # backtrack
            j = L[r]
            while j != r:
                uncover(col[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(c)
        return False

    ok = search()
    out = []
    if ok:
        out.append("YES")
        used = set()
        for idx in solution_rows:
            x, y, z = triples[idx]
            out.append(f"{x+1} {y+1} {z+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()