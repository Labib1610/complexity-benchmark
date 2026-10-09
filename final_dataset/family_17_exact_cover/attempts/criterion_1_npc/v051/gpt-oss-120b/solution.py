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
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    ncol = 3 * q                     # number of columns (elements)
    # dancing links arrays
    max_nodes = 1 + ncol + 3 * t + 5
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes               # column of node
    row_id = [0] * max_nodes          # which input triple
    S = [0] * (ncol + 1)              # column sizes, 1..ncol

    # header node 0, column headers 1..ncol
    for i in range(ncol + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol + 1               # next free index

    # add rows
    for rid, (a, b, c) in enumerate(triples):
        cols = [a + 1, b + 1, c + 1]   # shift to 1‑based column ids
        first = -1
        for col in cols:
            nd = node_cnt
            node_cnt += 1
            C[nd] = col
            row_id[nd] = rid
            # vertical links (insert at bottom of column)
            U[nd] = U[col]
            D[nd] = col
            D[U[col]] = nd
            U[col] = nd
            S[col] += 1
            # horizontal links
            if first == -1:
                first = nd
                L[nd] = R[nd] = nd
            else:
                # insert to the right of first
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

    def search(k: int) -> bool:
        nonlocal found
        if R[0] == 0:          # no columns left
            found = True
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
            if search(k + 1):
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

    if search(0):
        out = ["YES"]
        for rid in solution_rows:
            a, b, c = triples[rid]
            out.append(f"{a+1} {b+1} {c+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()