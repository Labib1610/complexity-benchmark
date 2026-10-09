import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    ncol = 3 * q                     # number of columns
    rows = []                         # each row = list of column indices (0‑based)

    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        rows.append([a, b, c])

    # ---------- DLX structure ----------
    # column header nodes: 0 .. ncol-1
    # node 0 is a dummy header for the column list
    max_nodes = 1 + ncol + len(rows) * 3 + 5
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes          # column of a node
    S = [0] * (ncol)             # size of each column
    row_id = [0] * max_nodes     # which input row a node belongs to

    # header links
    header = 0
    for i in range(ncol):
        L[i + 1] = i
        R[i] = i + 1
        U[i + 1] = D[i + 1] = i + 1
        C[i + 1] = i
    R[ncol] = header
    L[header] = ncol
    R[header] = 1

    node_cnt = ncol + 1  # next free index

    # add rows
    for rid, cols in enumerate(rows):
        first = -1
        for col in cols:
            col_node = col + 1  # column header index
            nd = node_cnt
            node_cnt += 1
            C[nd] = col
            row_id[nd] = rid
            # vertical links (insert at bottom of column)
            U[nd] = U[col_node]
            D[nd] = col_node
            D[U[col_node]] = nd
            U[col_node] = nd
            S[col] += 1
            # horizontal links
            if first == -1:
                first = nd
                L[nd] = R[nd] = nd
            else:
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd

    solution = []

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
        R[L[col]] = col
        L[R[col]] = col

    def choose_column():
        # heuristic: column with minimal size
        c = R[header]
        min_s = 10**9
        best = c
        while c != header:
            if S[C[c]] < min_s:
                min_s = S[C[c]]
                best = c
                if min_s == 0:
                    break
            c = R[c]
        return best

    found = False

    def search(k):
        nonlocal found
        if R[header] == header:
            # all columns covered
            found = True
            return True
        col = choose_column()
        if S[C[col]] == 0:
            return False
        cover(col)
        r = D[col]
        while r != col:
            solution.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j] + 1)
                j = R[j]
            if search(k + 1):
                return True
            # backtrack
            j = L[r]
            while j != r:
                uncover(C[j] + 1)
                j = L[j]
            solution.pop()
            r = D[r]
        uncover(col)
        return False

    if search(0):
        out = ["YES"]
        for rid in solution:
            a, b, c = rows[rid]
            out.append(f"{a+1} {b+1} {c+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()