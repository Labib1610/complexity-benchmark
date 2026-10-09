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
    # DLX arrays (0 is header)
    max_nodes = 3 * t + n + 1    # safe upper bound
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes          # column of node
    row_id = [0] * max_nodes     # which triple (index) the node belongs to
    S = [0] * (n + 1)            # column sizes, 1..n

    # header links columns 1..n in a circular list
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    # column headers point to themselves vertically
    for i in range(1, n + 1):
        U[i] = D[i] = i

    node_cnt = n  # last used index

    def add_row(ridx, cols):
        nonlocal node_cnt
        first = None
        for col in cols:
            node_cnt += 1
            nd = node_cnt
            C[nd] = col
            row_id[nd] = ridx
            # insert into column (at bottom, before header)
            U[nd] = U[col]
            D[nd] = col
            D[U[col]] = nd
            U[col] = nd
            S[col] += 1
            # link horizontally
            if first is None:
                first = nd
                L[nd] = R[nd] = nd
            else:
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd

    for idx, (a, b, c) in enumerate(triples, 1):
        add_row(idx, (a, b, c))

    answer_rows = []

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

    solved = False

    def search(k):
        nonlocal solved
        if R[0] == 0:          # no columns left
            solved = True
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
            answer_rows.append(row_id[r])
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
            answer_rows.pop()
            r = D[r]
        uncover(c)
        return False

    if search(0):
        out = ["YES"]
        for idx in answer_rows:
            a, b, c = triples[idx - 1]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()