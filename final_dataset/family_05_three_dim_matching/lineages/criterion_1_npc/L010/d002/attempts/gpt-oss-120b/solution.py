import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))

    n_cols = 3 * k  # columns: tech 0..k-1, hard k..2k-1, shift 2k..3k-1

    # Dancing Links structures
    max_nodes = t * 3 + n_cols + 1
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes  # column header for each node
    S = [0] * (n_cols)   # size of each column
    row_id = [0] * max_nodes  # which input row (index in triples)

    # header node 0
    for i in range(n_cols + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n_cols
    R[n_cols] = 0

    node_cnt = n_cols + 1  # next free node index

    def add_row(ridx, cols):
        nonlocal node_cnt
        first = None
        for col in cols:
            nd = node_cnt
            node_cnt += 1
            C[nd] = col
            row_id[nd] = ridx

            # vertical links
            U[nd] = U[col]
            D[nd] = col
            D[U[col]] = nd
            U[col] = nd
            S[col] += 1

            # horizontal links
            if first is None:
                first = nd
                L[nd] = R[nd] = nd
            else:
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd

    for idx, (x, y, z) in enumerate(triples):
        cols = [x, k + y, 2 * k + z]
        add_row(idx, cols)

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

    def search(k_depth=0):
        if R[0] == 0:  # all columns covered
            return True
        # choose column with minimal S
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
                cover(C[j])
                j = R[j]
            if search(k_depth + 1):
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

    possible = search()
    out = []
    if possible:
        out.append("YES")
        for ridx in solution_rows:
            x, y, z = triples[ridx]
            out.append(f"{x+1} {y+1} {z+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()