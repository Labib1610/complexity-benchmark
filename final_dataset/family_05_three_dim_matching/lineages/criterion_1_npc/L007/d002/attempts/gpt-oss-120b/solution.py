import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # columns: 0..k-1 chassis, k..2k-1 navigation, 2k..3k-1 sensor
    C = 3 * k
    rows = []          # each row: (c, n, i, [col indices])
    for _ in range(t):
        c = int(next(it)) - 1
        n = int(next(it)) - 1
        i = int(next(it)) - 1
        cols = [c, k + n, 2 * k + i]
        rows.append((c, n, i, cols))

    # ---------- DLX structures ----------
    # node 0 is the header
    max_nodes = 1 + C + t * 3
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    Ccol = [0] * max_nodes          # column of node
    S = [0] * (C + 1)               # size of column (only for column headers)
    row_id = [0] * max_nodes        # which original row a node belongs to

    # header links
    for i in range(C + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = C
    R[C] = 0

    # column headers are 1..C (shift by +1)
    # we will use column index+1 as header node id
    node_ptr = C + 1

    # add rows
    for rid, (c, n, i, cols) in enumerate(rows):
        first = -1
        for col in cols:
            col_header = col + 1
            nd = node_ptr
            node_ptr += 1
            Ccol[nd] = col_header
            row_id[nd] = rid
            # vertical links (insert at bottom of column)
            U[nd] = U[col_header]
            D[nd] = col_header
            D[U[col_header]] = nd
            U[col_header] = nd
            S[col_header] += 1
            # horizontal links within the row
            if first == -1:
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
        R[L[col]] = R[col]
        L[R[col]] = L[col]
        # remove rows
        i = D[col]
        while i != col:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                S[Ccol[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                S[Ccol[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        R[L[col]] = col
        L[R[col]] = col

    def search():
        if R[0] == 0:          # all columns covered
            return True
        # choose column with minimal size
        c = R[0]
        min_s = S[c]
        col = c
        j = R[c]
        while j != 0:
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
                cover(Ccol[j])
                j = R[j]
            if search():
                return True
            # backtrack
            j = L[r]
            while j != r:
                uncover(Ccol[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(col)
        return False

    if search():
        out = ["YES"]
        for rid in solution_rows:
            c, n, i, _ = rows[rid]
            out.append(f"{c+1} {n+1} {i+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()