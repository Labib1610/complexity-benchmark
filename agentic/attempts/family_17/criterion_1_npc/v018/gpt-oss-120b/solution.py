import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    U = 3 * q                     # number of columns, numbered 1..U
    rows = []                     # list of triples (a,b,c)
    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        rows.append((a, b, c))

    # ---------- dancing links ----------
    # node 0 is the root header
    # nodes 1..U are column headers
    # other nodes start from idx = U+1
    max_nodes = 1 + U + 3 * t + 5
    L = [0] * max_nodes
    R = [0] * max_nodes
    U_ = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes          # column of a node
    row_id = [0] * max_nodes     # which row a node belongs to

    # initialise column headers linked list
    for i in range(U + 1):
        L[i] = i - 1
        R[i] = i + 1
        U_[i] = i
        D[i] = i
    L[0] = U
    R[U] = 0

    size = [0] * (U + 1)         # number of rows in each column
    first_node_of_row = []       # for uncovering

    node_cnt = U + 1
    for rid, (a, b, c) in enumerate(rows):
        cols = (a, b, c)
        first = -1
        for col in cols:
            nd = node_cnt
            node_cnt += 1
            C[nd] = col
            row_id[nd] = rid
            # insert into column col (at the bottom)
            D[nd] = col
            U_[nd] = U_[col]
            D[U_[col]] = nd
            U_[col] = nd
            size[col] += 1
            if first == -1:
                first = nd
                L[nd] = R[nd] = nd
            else:
                # insert into row circular list
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd
        first_node_of_row.append(first)

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
                U_[D[j]] = U_[j]
                D[U_[j]] = D[j]
                size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col: int) -> None:
        i = U_[col]
        while i != col:
            j = L[i]
            while j != i:
                size[C[j]] += 1
                U_[D[j]] = j
                D[U_[j]] = j
                j = L[j]
            i = U_[i]
        L[R[col]] = col
        R[L[col]] = col

    # heuristic: choose column with minimal size
    def choose_column() -> int:
        c = R[0]
        min_sz = size[c]
        best = c
        while c != 0:
            if size[c] < min_sz:
                min_sz = size[c]
                best = c
                if min_sz == 0:
                    break
            c = R[c]
        return best

    found = False

    def search(k: int) -> None:
        nonlocal found
        if R[0] == 0:          # all columns covered
            found = True
            return
        c = choose_column()
        if size[c] == 0:
            return
        cover(c)
        r = D[c]
        while r != c:
            solution_rows.append(row_id[r])
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
        uncover(c)

    search(0)

    out = []
    if found:
        out.append("YES")
        for rid in solution_rows:
            a, b, c = rows[rid]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()