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
    rows = []                     # list of triples (as ints 1‑based)
    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        rows.append((a, b, c))

    # ---------- Dancing Links ----------
    # column headers: 0 .. n-1
    # node arrays
    max_nodes = 3 * t + n + 5
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes          # column of node
    S = [0] * (n + 1)            # size of column (header 1..n)
    row_id = [0] * max_nodes     # which input row a node belongs to

    # header node 0, column headers 1..n
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_cnt = n
    for rid, (a, b, c) in enumerate(rows, start=1):
        for col in (a, b, c):
            node_cnt += 1
            C[node_cnt] = col
            row_id[node_cnt] = rid
            # insert node at bottom of column col
            D[node_cnt] = col
            U[node_cnt] = U[col]
            D[U[col]] = node_cnt
            U[col] = node_cnt
            S[col] += 1
        # link the three nodes horizontally
        first = node_cnt - 2
        second = node_cnt - 1
        third = node_cnt
        L[first] = third
        R[first] = second
        L[second] = first
        R[second] = third
        L[third] = second
        R[third] = first

    answer_rows = []

    def cover(col: int) -> None:
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

    def uncover(col: int) -> None:
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

    solved = False

    def search(k: int) -> None:
        nonlocal solved
        if solved:
            return
        if R[0] == 0:          # no columns left
            solved = True
            return
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
            return
        cover(c)
        r = D[c]
        while r != c:
            answer_rows.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            search(k + 1)
            if solved:
                return
            # backtrack
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            answer_rows.pop()
            r = D[r]
        uncover(c)

    search(0)

    out = []
    if solved:
        out.append("YES")
        for rid in answer_rows:
            a, b, c = rows[rid - 1]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()