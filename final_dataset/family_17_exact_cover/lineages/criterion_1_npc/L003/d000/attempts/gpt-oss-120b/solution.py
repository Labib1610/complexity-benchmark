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
    max_nodes = 3 * t + n + 1     # header + column headers + all nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes           # column of a node
    S = [0] * (n + 1)             # size of each column (1‑based)
    row_id = [0] * max_nodes      # which input triple a node belongs to

    header = 0
    # initialise column headers 1..n
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_cnt = n
    # add rows
    for idx, (a, b, c) in enumerate(triples, 1):
        first = -1
        for col in (a, b, c):
            node_cnt += 1
            C[node_cnt] = col
            row_id[node_cnt] = idx
            # insert into column list (at bottom)
            D[node_cnt] = col
            U[node_cnt] = U[col]
            D[U[col]] = node_cnt
            U[col] = node_cnt
            S[col] += 1
            # link row horizontally
            if first == -1:
                first = node_cnt
                L[node_cnt] = R[node_cnt] = node_cnt
            else:
                L[node_cnt] = L[first]
                R[node_cnt] = first
                R[L[first]] = node_cnt
                L[first] = node_cnt

    solution = []

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

    def search(k: int) -> bool:
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
            solution.append(row_id[r])
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
        uncover(col)
        return False

    ok = search(0)
    out = []
    if ok:
        out.append("YES")
        # solution may be in any order; we need exactly q rows
        # (search guarantees covering all columns, thus exactly q rows)
        for idx in solution:
            a, b, c = triples[idx - 1]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()