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
    triples = []
    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        if a <= n and c <= n:    # all numbers are within range by definition
            triples.append((a, b, c))

    # ---------- DLX structures ----------
    max_nodes = 3 * len(triples) + n + 1
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes          # column header for each node
    S = [0] * (n + 1)            # size of each column
    row_id = [0] * max_nodes     # which input row a node belongs to

    header = 0
    # link header horizontally with column headers 1..n
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_cnt = n
    # add rows
    for idx, (a, b, c) in enumerate(triples, 1):
        first = None
        for col in (a, b, c):
            node_cnt += 1
            col_header = col
            # vertical links
            U[node_cnt] = U[col_header]
            D[node_cnt] = col_header
            D[U[col_header]] = node_cnt
            U[col_header] = node_cnt
            C[node_cnt] = col_header
            S[col_header] += 1
            row_id[node_cnt] = idx
            # horizontal links within the row
            if first is None:
                first = node_cnt
                L[node_cnt] = R[node_cnt] = node_cnt
            else:
                L[node_cnt] = L[first]
                R[node_cnt] = first
                R[L[first]] = node_cnt
                L[first] = node_cnt

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

    def search(k=0):
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
        uncover(col)
        return False

    if search():
        out = ["YES"]
        # map row index to triple
        idx_to_trip = {i+1: triples[i] for i in range(len(triples))}
        for rid in solution_rows:
            a, b, c = idx_to_trip[rid]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()