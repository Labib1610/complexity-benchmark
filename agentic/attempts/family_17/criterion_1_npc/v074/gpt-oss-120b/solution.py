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
    max_nodes = 3 * t + n + 1     # plus column headers
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes           # column of a node
    S = [0] * (n + 1)             # size of column (header 1..n)
    row_id = [0] * max_nodes      # which input triple a node belongs to

    # header node 0, column headers 1..n
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = n
    R[n] = 0

    node_cnt = n + 1  # next free index

    # add rows
    for idx, (a, b, c) in enumerate(triples, 1):
        first = -1
        for col in (a, b, c):
            node = node_cnt
            node_cnt += 1
            C[node] = col
            row_id[node] = idx
            # insert into column (at bottom, before header)
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            S[col] += 1
            # link within the row
            if first == -1:
                first = node
                L[node] = R[node] = node
            else:
                # insert to the right of first
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

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
        # answer_rows may be in any order, but we need exactly q rows
        # they are already distinct because each row corresponds to a triple
        for idx in answer_rows:
            a, b, c = triples[idx - 1]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()