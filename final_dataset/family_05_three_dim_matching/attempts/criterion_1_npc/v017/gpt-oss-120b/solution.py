import sys
sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []                     # (a,b,c) 1‑based
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triples.append((a, b, c))

    ncol = 3 * k                     # columns are 1..ncol

    # ----- DLX structures -----
    # header = 0, column headers = 1..ncol
    L = [0] * (1 + ncol)             # left neighbour
    R = [0] * (1 + ncol)             # right neighbour
    U = [0] * (1 + ncol)             # up neighbour
    D = [0] * (1 + ncol)             # down neighbour
    C = [0] * (1 + ncol)             # column of node (only for ordinary nodes)
    row_id = [0] * (1 + ncol)        # row index of node (only for ordinary nodes)
    S = [0] * (ncol + 1)             # size of each column

    # initialise column headers and header list
    for i in range(ncol + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = ncol
    R[ncol] = 0

    # ----- function to add a row -----
    node_cnt = ncol + 1               # next free index
    def add_row(cols, rid):
        nonlocal node_cnt
        first = None
        for col in cols:
            idx = node_cnt
            node_cnt += 1
            # vertical links
            U[idx] = U[col]
            D[idx] = col
            D[U[col]] = idx
            U[col] = idx
            C[idx] = col
            row_id[idx] = rid
            S[col] += 1
            # horizontal links (temporary)
            if first is None:
                first = idx
                L[idx] = R[idx] = idx
            else:
                # insert to the left of first (circular list)
                L[idx] = L[first]
                R[idx] = first
                R[L[first]] = idx
                L[first] = idx

    # build rows
    for idx, (a, b, c) in enumerate(triples, start=1):
        add_row([a, k + b, 2 * k + c], idx)

    # ----- DLX core operations -----
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

    # ----- search -----
    solution_rows = []
    answer = None

    def choose_column():
        # column with smallest S
        c = R[0]
        best = c
        min_sz = S[c]
        c = R[c]
        while c != 0:
            if S[c] < min_sz:
                min_sz = S[c]
                best = c
                if min_sz == 0:
                    break
            c = R[c]
        return best

    def search():
        nonlocal answer
        if R[0] == 0:                     # all columns covered
            answer = solution_rows.copy()
            return True
        c = choose_column()
        if S[c] == 0:                     # dead end
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

    possible = search()

    out = []
    if possible:
        out.append("YES")
        for rid in answer:
            a, b, c = triples[rid - 1]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()