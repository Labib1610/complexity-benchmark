import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # columns: 0..k-1   base
    #          k..2k-1 catalyst
    #          2k..3k-1 profile
    ncol = 3 * k
    rows = []          # each row: (base,cat,prof) as given
    col_of_row = []    # list of column indices for each row (length 3)

    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        rows.append((x + 1, y + 1, z + 1))
        col_of_row.append([x, k + y, 2 * k + z])

    # ---------- dancing links ----------
    # node 0 is header
    max_nodes = 1 + ncol + 3 * t
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes          # column of node
    S = [0] * (ncol + 1)         # size of column, 1‑based for columns
    row_id = [0] * max_nodes     # which row a node belongs to (0‑based)

    # header links
    for i in range(ncol + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol + 1  # next free index

    # add rows
    for r, cols in enumerate(col_of_row, start=1):   # rows numbered from 1
        first = -1
        for col in cols:
            col += 1          # make column indices 1‑based for DLX
            idx = node_cnt
            node_cnt += 1

            C[idx] = col
            row_id[idx] = r
            # vertical links
            U[idx] = U[col]
            D[idx] = col
            D[U[col]] = idx
            U[col] = idx
            S[col] += 1

            # horizontal links
            if first == -1:
                first = idx
                L[idx] = R[idx] = idx
            else:
                L[idx] = L[first]
                R[idx] = first
                R[L[first]] = idx
                L[first] = idx

    solution_rows = []

    def cover(col):
        # remove column header
        L[R[col]] = L[col]
        R[L[col]] = R[col]
        # remove rows
        i = D[col]
        while i != col:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                S[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                S[C[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[col]] = col
        R[L[col]] = col

    def search():
        if R[0] == 0:          # no columns left
            return True
        # choose column with minimal size
        c = R[0]
        min_s = S[c]
        j = R[c]
        while j != 0:
            if S[j] < min_s:
                c = j
                min_s = S[j]
                if min_s == 0:
                    break
            j = R[j]
        if min_s == 0:
            return False

        cover(c)
        r = D[c]
        while r != c:
            solution_rows.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            if search():
                return True
            # backtrack
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(c)
        return False

    ok = search()
    out = []
    if ok:
        out.append("YES")
        for rid in solution_rows:
            out.append("{} {} {}".format(*rows[rid - 1]))
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()