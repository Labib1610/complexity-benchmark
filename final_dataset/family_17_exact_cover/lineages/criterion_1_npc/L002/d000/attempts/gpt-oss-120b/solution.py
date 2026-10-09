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

    n_cols = 3 * q                     # columns are 1..3q
    # ----- DLX structures -----
    max_nodes = 3 * t + n_cols + 1     # + header
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes                # column of node
    S = [0] * (n_cols + 1)             # size of column, 1‑based
    row_of_node = [0] * max_nodes      # which input row a node belongs to

    header = 0
    # initialise column headers
    for i in range(1, n_cols + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
        C[i] = i
    L[header] = n_cols
    R[header] = 1
    L[1] = header
    R[n_cols] = header

    node_cnt = n_cols
    # add rows
    for rid, (a, b, c) in enumerate(triples, start=1):
        first = None
        for col in (a, b, c):
            node_cnt += 1
            nd = node_cnt
            C[nd] = col
            row_of_node[nd] = rid
            # vertical links (insert at bottom of column)
            D[nd] = col
            U[nd] = U[col]
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

    def cover(col: int) -> None:
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

    def uncover(col: int) -> None:
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

    found = False

    def search(k: int) -> None:
        nonlocal found
        if R[header] == header:          # all columns covered
            found = True
            return
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
            return
        cover(col)
        r = D[col]
        while r != col:
            solution_rows.append(row_of_node[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            search(k + 1)
            if found:
                return
            # backtrack
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(col)

    search(0)

    out = []
    if found:
        out.append("YES")
        # retrieve triples in the order they were stored
        for rid in solution_rows:
            a, b, c = triples[rid - 1]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()