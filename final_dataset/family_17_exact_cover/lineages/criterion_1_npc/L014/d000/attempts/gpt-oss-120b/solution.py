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

    ncol = 3 * q                     # columns are 1..ncol
    # DLX structures
    max_nodes = 3 * t + ncol + 1     # + header
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes
    row_id = [-1] * max_nodes        # only meaningful for row header nodes
    size = [0] * (ncol + 1)          # column sizes, index 1..ncol

    header = 0
    # initialise column headers linked horizontally
    for i in range(ncol + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    R[ncol] = header
    L[header] = ncol

    node_cnt = ncol + 1  # next free index

    # add rows
    for rid, (a, b, c) in enumerate(triples):
        first = -1
        for col in (a, b, c):
            nd = node_cnt
            node_cnt += 1
            C[nd] = col
            # vertical links (insert at bottom of column)
            U[nd] = U[col]
            D[nd] = col
            D[U[col]] = nd
            U[col] = nd
            size[col] += 1
            # horizontal links within the row
            if first == -1:
                first = nd
                L[nd] = R[nd] = nd
            else:
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd
        row_id[first] = rid   # store which triple this row corresponds to

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
                size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                size[C[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[col]] = col
        R[L[col]] = col

    # heuristic: column with minimal size
    def choose_column():
        c = R[header]
        min_sz = size[c]
        best = c
        while c != header:
            if size[c] < min_sz:
                min_sz = size[c]
                best = c
                if min_sz == 0:
                    break
            c = R[c]
        return best

    found = False

    def search():
        nonlocal found
        if R[header] == header:          # all columns covered
            found = True
            return True
        col = choose_column()
        if size[col] == 0:
            return False
        cover(col)
        r = D[col]
        while r != col:
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
        uncover(col)
        return False

    if search():
        out = ["YES"]
        for rid in solution_rows:
            a, b, c = triples[rid]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()