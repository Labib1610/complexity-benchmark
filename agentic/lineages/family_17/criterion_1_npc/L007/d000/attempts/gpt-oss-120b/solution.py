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
    # DLX structures (0 is the header)
    max_nodes = 1 + n + 3 * t + 5
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes          # column of a node
    row_id = [0] * max_nodes     # which triple this node belongs to
    size = [0] * (n + 1)         # size of each column (1..n)

    # header links
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = n
    R[n] = 0

    node_cnt = n + 1  # next free index

    # add rows
    for idx, (a, b, c) in enumerate(triples, 1):
        first = None
        for col in (a, b, c):
            nd = node_cnt
            node_cnt += 1
            C[nd] = col
            row_id[nd] = idx
            # vertical insert at bottom of column
            U[nd] = U[col]
            D[nd] = col
            D[U[col]] = nd
            U[col] = nd
            size[col] += 1
            # horizontal links within the row
            if first is None:
                first = nd
                L[nd] = R[nd] = nd
            else:
                # insert to the left of first
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd

    solution_rows = []

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
                size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col: int) -> None:
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                size[C[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[col]] = col
        R[L[col]] = col

    found = False

    def search(k: int) -> None:
        nonlocal found
        if R[0] == 0:          # all columns covered
            found = True
            return
        # choose column with minimal size
        c = R[0]
        min_sz = size[c]
        j = R[c]
        while j != 0:
            if size[j] < min_sz:
                min_sz = size[j]
                c = j
                if min_sz == 0:
                    break
            j = R[j]
        if min_sz == 0:
            return
        cover(c)
        r = D[c]
        while r != c:
            solution_rows.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            search(k + 1)
            if found:
                return
            # backtrack
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(c)

    search(0)

    out = []
    if found:
        out.append("YES")
        # solution_rows may be in any order; we need exactly q rows
        # they are already distinct because of exact cover property
        for rid in solution_rows:
            a, b, c = triples[rid - 1]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()