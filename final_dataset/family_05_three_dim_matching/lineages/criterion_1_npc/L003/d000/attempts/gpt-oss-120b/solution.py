import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    C = 3 * k                     # number of columns
    triples = []                  # (a,b,c) zero based

    # ---- DLX structures ----
    L = []        # left neighbor
    R = []        # right neighbor
    U = []        # up neighbor
    D = []        # down neighbor
    col_of_node = []   # column header of a node (1..C), 0 for headers
    row_of_node = []   # which row this node belongs to
    S = [0] * (C + 1)  # size of each column (header index)

    # root header = 0
    L.append(C)   # temporary, will be fixed after columns are added
    R.append(1)
    U.append(0)
    D.append(0)
    col_of_node.append(0)
    row_of_node.append(-1)

    # column headers 1 .. C
    for i in range(1, C + 1):
        L.append(i - 1)
        R.append(i + 1)
        U.append(i)
        D.append(i)
        col_of_node.append(i)  # header points to itself
        row_of_node.append(-1)
        S[i] = 0

    # close the circular list of column headers
    R[C] = 0
    L[0] = C
    L[1] = 0
    R[0] = 1

    # ----- helper to add a row -----
    def add_row(row_idx, cols):
        first = None
        prev = None
        for c in cols:
            col_hdr = c + 1               # column headers are 1‑based
            node = len(L)
            L.append(0)
            R.append(0)
            U.append(0)
            D.append(0)
            col_of_node.append(col_hdr)
            row_of_node.append(row_idx)

            # vertical insertion (just before column header)
            U[node] = U[col_hdr]
            D[node] = col_hdr
            D[U[col_hdr]] = node
            U[col_hdr] = node
            S[col_hdr] += 1

            # horizontal linking inside the row
            if first is None:
                first = node
                prev = node
            else:
                L[node] = prev
                R[prev] = node
                prev = node

        # close the row's circular list
        if first is not None:
            L[first] = prev
            R[prev] = first

    # read all triples and insert rows
    for idx in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))
        cols = [a, k + b, 2 * k + c]
        add_row(idx, cols)

    solution_rows = []

    # ----- DLX operations -----
    def cover(col):
        # remove column header
        R[L[col]] = R[col]
        L[R[col]] = L[col]
        # remove rows
        i = D[col]
        while i != col:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                S[col_of_node[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                S[col_of_node[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        R[L[col]] = col
        L[R[col]] = col

    # ----- recursive search -----
    def search():
        if R[0] == 0:          # all columns covered
            return True
        # choose column with minimal S
        c = R[0]
        min_s = S[c]
        j = R[c]
        while j != 0:
            if S[j] < min_s:
                min_s = S[j]
                c = j
                if min_s == 0:
                    break
            j = R[j]
        if min_s == 0:
            return False

        cover(c)
        r = D[c]
        while r != c:
            solution_rows.append(row_of_node[r])

            # cover other columns of this row
            j = R[r]
            while j != r:
                cover(col_of_node[j])
                j = R[j]

            if search():
                return True

            # backtrack
            j = L[r]
            while j != r:
                uncover(col_of_node[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]

        uncover(c)
        return False

    ok = search()
    out = []
    if ok:
        out.append("YES")
        for rid in solution_rows:
            a, b, c = triples[rid]
            out.append(f"{a+1} {b+1} {c+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()