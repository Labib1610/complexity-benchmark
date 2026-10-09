import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # column indices: 0..k-1 specialists, k..2k-1 machines, 2k..3k-1 times
    ncol = 3 * k

    rows = []          # list of (x,y,z) for each allowed triple
    row_cols = []      # list of column indices for each row (length 3)

    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        rows.append((x + 1, y + 1, z + 1))
        row_cols.append([x, k + y, 2 * k + z])

    # ---------- DLX structures ----------
    # Node arrays (0 is the header)
    max_nodes = t * 3 + ncol + 1
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes          # column header for each node
    S = [0] * (ncol + 1)         # size of each column (header 1..ncol)
    row_id = [0] * max_nodes     # which original row a node belongs to

    # header links columns in a circular list
    header = 0
    for i in range(ncol + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    R[ncol] = header
    L[header] = ncol

    node_cnt = ncol + 1  # next free index

    # add rows
    for r, cols in enumerate(row_cols, start=1):
        first = None
        for col in cols:
            col += 1                     # shift to 1..ncol for headers
            nd = node_cnt
            node_cnt += 1

            C[nd] = col
            row_id[nd] = r

            # vertical links (insert at bottom of column)
            U[nd] = U[col]
            D[nd] = col
            D[U[col]] = nd
            U[col] = nd
            S[col] += 1

            # horizontal links within the row
            if first is None:
                first = nd
                L[nd] = R[nd] = nd
            else:
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd

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
        if R[header] == header:          # all columns covered
            return True
        # choose column with minimal size
        c = R[header]
        min_s = S[c]
        col = c
        j = R[c]
        while j != header:
            if S[j] < min_s:
                min_s = S[j]
                col = j
                if min_s == 0:
                    break
            j = R[j]
        if min_s == 0:
            return False
        cover(col)
        r = D[col]
        while r != col:
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
        uncover(col)
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