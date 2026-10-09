import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q                     # number of columns
    rows = []                     # list of triples (as tuple)
    # DLX structures
    max_nodes = t * 3 + n + 1     # + header
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes           # column of node
    S = [0] * (n + 1)             # size of column (header 0 unused)
    # column headers are 1..n, header node is 0
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_cnt = n + 1  # next free index

    # add a row (list of columns)
    def add_row(cols, row_id):
        nonlocal node_cnt
        first = None
        for col in cols:
            nd = node_cnt
            node_cnt += 1
            C[nd] = col
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
        # store row id in first node (optional)
        # we can map node -> row later via a separate array if needed
        row_of_node[first] = row_id

    row_of_node = {}

    for idx in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        rows.append((a, b, c))
        add_row([a, b, c], idx)

    solution = []

    sys.setrecursionlimit(10000)

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
        R[L[col]] = col
        L[R[col]] = col

    found = False

    def search(k):
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
            solution.append(row_of_node[r])
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
            solution.pop()
            r = D[r]
        uncover(c)
        return False

    if search(0):
        out = ["YES"]
        for rid in solution:
            a, b, c = rows[rid]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()