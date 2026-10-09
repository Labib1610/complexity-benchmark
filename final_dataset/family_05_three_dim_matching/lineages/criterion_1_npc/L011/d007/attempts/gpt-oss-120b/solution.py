import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # column ids: 0..k-1   -> X_1..X_k
    #             k..2k-1 -> Y_1..Y_k
    #             2k..3k-1-> Z_1..Z_k
    ncol = 3 * k

    # DLX structures
    # header node is 0, columns are 1..ncol
    size = 1 + ncol + 3 * t + 5   # enough space
    U = [0] * size
    D = [0] * size
    L = [0] * size
    R = [0] * size
    C = [0] * size          # column of a node
    row_id = [0] * size     # which input row (index) a node belongs to

    # column header nodes: 1..ncol
    for i in range(ncol + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    col_size = [0] * (ncol + 1)   # number of nodes in each column
    node_cnt = ncol               # last used index

    triples = []  # store input triples for output
    for idx in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x + 1, y + 1, z + 1))   # keep 1‑based for output
        cols = [x, k + y, 2 * k + z]            # column numbers (0‑based)

        first = None
        for col in cols:
            node_cnt += 1
            nd = node_cnt
            C[nd] = col + 1          # column header id (1‑based)
            row_id[nd] = idx

            # insert into column (at bottom)
            D[nd] = col + 1
            U[nd] = U[col + 1]
            D[U[col + 1]] = nd
            U[col + 1] = nd
            col_size[col + 1] += 1

            # link row horizontally
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
                col_size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                col_size[C[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[col]] = col
        R[L[col]] = col

    def search():
        if R[0] == 0:          # all columns covered
            return True
        # choose column with minimal size
        c = R[0]
        min_sz = col_size[c]
        j = R[c]
        while j != 0:
            if col_size[j] < min_sz:
                c = j
                min_sz = col_size[j]
                if min_sz == 0:
                    break
            j = R[j]
        if min_sz == 0:
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
    if ok and len(solution_rows) == k:
        out.append("YES")
        for idx in solution_rows:
            x, y, z = triples[idx]
            out.append(f"{x} {y} {z}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()