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

    n = 3 * q                     # number of columns (elements)
    max_nodes = 3 * t + n + 1     # plus column headers and head

    # DLX arrays
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes           # column of node
    row_id = [0] * max_nodes      # which triple this node belongs to
    size = [0] * (n + 1)          # column sizes, 1..n

    head = 0
    # initialise header list of columns
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = n
    R[n] = 0

    node_cnt = n + 1  # next free index

    # add rows
    for idx, (a, b, c) in enumerate(triples):
        cols = [a, b, c]
        first = -1
        for col in cols:
            node = node_cnt
            node_cnt += 1
            C[node] = col
            row_id[node] = idx

            # vertical link (insert at bottom of column)
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            size[col] += 1

            # horizontal link
            if first == -1:
                first = node
                L[node] = R[node] = node
            else:
                # insert to the right of first
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

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

    def search(k: int) -> bool:
        if R[head] == head:          # all columns covered
            return True
        # choose column with minimal size
        c = R[head]
        min_sz = size[c]
        col = c
        j = R[c]
        while j != head:
            if size[j] < min_sz:
                min_sz = size[j]
                col = j
                if min_sz == 0:
                    break
            j = R[j]
        if min_sz == 0:
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

    ok = search(0)
    out = []
    if ok:
        out.append("YES")
        for idx in solution_rows:
            a, b, c = triples[idx]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()