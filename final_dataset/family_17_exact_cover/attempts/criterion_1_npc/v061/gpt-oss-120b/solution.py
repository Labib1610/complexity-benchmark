import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    N = 3 * q                     # number of columns
    rows = []                     # list of triples (as ints)
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        rows.append((a, b, c))

    # ---------- DLX structures ----------
    # node 0 is the header
    max_nodes = 3 * t + N + 1
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes          # column of node
    S = [0] * (N + 1)            # size of column (header indices 1..N)
    row_id = [0] * max_nodes     # which input row a node belongs to

    # initialise column headers linked horizontally
    for i in range(N + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = N
    R[N] = 0

    node_cnt = N
    # add rows
    for idx, (a, b, c) in enumerate(rows, start=1):
        first = None
        for col in (a, b, c):
            node_cnt += 1
            col_header = col
            C[node_cnt] = col_header
            row_id[node_cnt] = idx

            # vertical links (insert at bottom of column)
            U[node_cnt] = U[col_header]
            D[node_cnt] = col_header
            D[U[col_header]] = node_cnt
            U[col_header] = node_cnt

            S[col_header] += 1

            # horizontal links within the row
            if first is None:
                first = node_cnt
                L[node_cnt] = R[node_cnt] = node_cnt
            else:
                # insert to the right of first
                L[node_cnt] = L[first]
                R[node_cnt] = first
                R[L[first]] = node_cnt
                L[first] = node_cnt

    # ---------- DLX operations ----------
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

    solution_rows = []

    def search(k):
        if R[0] == 0:          # no columns left
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

    ok = search(0)
    out = []
    if ok:
        out.append("YES")
        # solution_rows contains indices of chosen triples (1‑based)
        for idx in solution_rows:
            a, b, c = rows[idx - 1]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()