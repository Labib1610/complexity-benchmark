import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q                     # number of columns
    rows = []                     # list of triples (as ints)
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        rows.append((a, b, c))

    # ---------- DLX construction ----------
    max_nodes = 1 + n + 3 * t      # header + column headers + each 1
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes           # column of node
    S = [0] * (n + 1)             # size of column, 1..n

    header = 0
    # link column headers horizontally
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    # initially each column header points to itself vertically
    for i in range(1, n + 1):
        U[i] = D[i] = i

    node_cnt = n + 1  # next free index

    row_id_of_node = [0] * max_nodes   # to retrieve original triple
    for rid, (a, b, c) in enumerate(rows, start=1):
        for col in (a, b, c):
            node = node_cnt
            node_cnt += 1
            C[node] = col
            row_id_of_node[node] = rid

            # insert node at bottom of column col
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            S[col] += 1

            # link horizontally within the row
            if node == node_cnt - 1:   # first node of this row
                L[node] = R[node] = node
            else:
                # insert to the left of the first node of this row
                first = node - (node_cnt - (n + 1) - 1)  # tricky, easier: keep a list
                pass
    # The above horizontal linking is messy; redo with explicit per-row handling.

def solve():
    import sys
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it)); t = int(next(it))
    n = 3 * q
    triples = [tuple(map(int, (next(it), next(it), next(it)))) for _ in range(t)]

    # DLX structures
    max_nodes = 1 + n + 3 * t
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes
    S = [0] * (n + 1)
    row_of = [0] * max_nodes

    header = 0
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0
    for i in range(1, n + 1):
        U[i] = D[i] = i

    node = n + 1
    first_in_row = []   # store first node index of each row
    for rid, (a, b, c) in enumerate(triples, start=1):
        cols = (a, b, c)
        first = None
        prev = None
        for col in cols:
            cur = node
            node += 1
            C[cur] = col
            row_of[cur] = rid
            # vertical insert
            U[cur] = U[col]
            D[cur] = col
            D[U[col]] = cur
            U[col] = cur
            S[col] += 1
            # horizontal insert
            if first is None:
                first = cur
                L[cur] = R[cur] = cur
            else:
                # insert cur to the left of first
                L[cur] = L[first]
                R[cur] = first
                R[L[first]] = cur
                L[first] = cur
        first_in_row.append(first)

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

    def search(k):
        if R[header] == header:   # all columns covered
            return True
        # choose column with minimal S
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
            solution_rows.append(row_of[r])
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
        uncover(col)
        return False

    ok = search(0)
    out = []
    if ok:
        out.append("YES")
        # retrieve triples in order of solution_rows
        for rid in solution_rows:
            a, b, c = triples[rid - 1]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()