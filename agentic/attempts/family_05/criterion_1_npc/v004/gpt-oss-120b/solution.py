import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []
    rows = []          # list of column indices for each row
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x + 1, y + 1, z + 1))
        rows.append([x, k + y, 2 * k + z])

    ncol = 3 * k                     # number of columns
    # DLX structures
    max_nodes = 3 * t + ncol + 1     # + header
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes              # column of node
    S = [0] * (ncol + 1)             # column sizes, 1‑based for columns
    col_head = [0] * (ncol + 1)      # header node index for each column

    header = 0
    # initialise column headers linked in a circular list
    for i in range(1, ncol + 1):
        col_head[i] = i
        S[i] = 0
        U[i] = i
        D[i] = i
        L[i] = i - 1 if i > 1 else ncol
        R[i] = i + 1 if i < ncol else header
    L[header] = ncol
    R[header] = 1

    node_cnt = ncol + 1  # next free index

    # add rows
    row_id_of_node = [0] * max_nodes   # to retrieve original triple
    for r_idx, cols in enumerate(rows):
        first = None
        for col in cols:
            col += 1                     # make 1‑based
            nd = node_cnt
            node_cnt += 1
            C[nd] = col
            row_id_of_node[nd] = r_idx

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
                # insert to the right of first
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd

    solution_rows = []

    sys.setrecursionlimit(10000)

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
            solution_rows.append(row_id_of_node[r])
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
            x, y, z = triples[rid]
            out.append(f"{x} {y} {z}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()