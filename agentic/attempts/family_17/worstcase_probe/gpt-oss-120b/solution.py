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

    n = 3 * q                     # number of columns
    # DLX structures
    max_nodes = 3 * t + n + 1     # plus column headers and head
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes
    S = [0] * (n + 1)             # column sizes, 1‑based
    row_of_node = [0] * max_nodes

    head = 0
    # header list (0 is head, 1..n are column headers)
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = n
    R[n] = 0

    node_cnt = n + 1  # next free index

    # add rows
    for rid, (a, b, c) in enumerate(triples, start=1):
        cols = (a, b, c)
        first = None
        for col in cols:
            nd = node_cnt
            node_cnt += 1
            C[nd] = col
            row_of_node[nd] = rid
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
        if R[head] == head:
            return True
        # choose column with minimal size
        c = R[head]
        min_s = S[c]
        col = c
        j = R[c]
        while j != head:
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
            solution_rows.append(row_of_node[r])
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
        # solution_rows may contain duplicates because each row appears multiple times in traversal,
        # but we added exactly once per chosen row. Ensure we output exactly q rows.
        # The algorithm picks exactly q rows.
        for rid in solution_rows:
            out.append(' '.join(map(str, triples[rid - 1])))
    else:
        out.append("NO")
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()