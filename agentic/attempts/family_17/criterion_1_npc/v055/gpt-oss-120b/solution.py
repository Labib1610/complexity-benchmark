import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    ncol = 3 * q                     # number of columns
    rows = []                        # list of triples (as list of column indices 0‑based)

    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        rows.append([a, b, c])

    # ---------- DLX construction ----------
    max_nodes = 3 * t + ncol + 1      # +1 for header
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes              # column of a node
    S = [0] * (ncol + 1)             # size of each column, column ids 1..ncol
    row_id = [0] * max_nodes         # which input row a node belongs to

    head = 0
    # header links columns 1..ncol
    for i in range(ncol + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol + 1  # next free index

    for r_idx, cols in enumerate(rows):
        first = -1
        for col in cols:
            col_id = col + 1          # column nodes are 1‑based
            node = node_cnt
            node_cnt += 1

            C[node] = col_id
            row_id[node] = r_idx

            # vertical insertion (bottom of column)
            U[node] = U[col_id]
            D[node] = col_id
            D[U[col_id]] = node
            U[col_id] = node
            S[col_id] += 1

            # horizontal linking within the row
            if first == -1:
                first = node
                L[node] = R[node] = node
            else:
                # insert to the right of first
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

    # ---------- DLX operations ----------
    def cover(col):
        # remove column header
        L[R[col]] = L[col]
        R[L[col]] = R[col]
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

    solution_rows = []

    def search(k):
        if R[head] == head:          # all columns covered
            return True
        # choose column with minimal size
        c = R[head]
        min_s = S[c]
        col = c
        j = R[c]
        while j != head:
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
            if search(k + 1):
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

    ok = search(0)

    out = []
    if ok:
        out.append("YES")
        for rid in solution_rows:
            a, b, c = rows[rid]
            out.append(f"{a+1} {b+1} {c+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()