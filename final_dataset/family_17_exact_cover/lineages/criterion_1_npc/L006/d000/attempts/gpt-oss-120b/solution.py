import sys
sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    ncol = 3 * q                     # columns are 1..ncol
    rows = []                        # list of triples (as ints)
    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        rows.append((a, b, c))

    # ---------- Dancing Links ----------
    # Node arrays (0 is the header of column list)
    max_nodes = 3 * t + ncol + 1
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes          # column of node
    S = [0] * (ncol + 1)         # size of each column
    row_id = [0] * max_nodes     # which input row a node belongs to

    # column headers 1..ncol, plus a root header 0
    for i in range(ncol + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol
    # add rows
    for rid, (a, b, c) in enumerate(rows, 1):
        first = 0
        for col in (a, b, c):
            node_cnt += 1
            idx = node_cnt
            C[idx] = col
            row_id[idx] = rid
            # vertical links
            U[idx] = U[col]
            D[idx] = col
            D[U[col]] = idx
            U[col] = idx
            S[col] += 1
            # horizontal links
            if first == 0:
                L[idx] = R[idx] = idx
                first = idx
            else:
                L[idx] = L[first]
                R[idx] = first
                R[L[first]] = idx
                L[first] = idx

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

    def choose_column() -> int:
        # heuristic: column with minimal size
        c = R[0]
        min_s = 10**9
        best = c
        while c != 0:
            if S[c] < min_s:
                min_s = S[c]
                best = c
                if min_s == 0:
                    break
            c = R[c]
        return best

    found = False

    def search(k: int) -> None:
        nonlocal found
        if R[0] == 0:          # all columns covered
            found = True
            return
        col = choose_column()
        if S[col] == 0:        # dead end
            return
        cover(col)
        r = D[col]
        while r != col and not found:
            solution_rows.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            search(k + 1)
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
        for rid in solution_rows:
            a, b, c = rows[rid - 1]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()