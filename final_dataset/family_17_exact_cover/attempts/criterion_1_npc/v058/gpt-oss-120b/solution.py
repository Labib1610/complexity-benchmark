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

    ncol = 3 * q                     # columns 1..ncol
    # DLX structures
    max_nodes = 3 * t + ncol + 1     # + header
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes              # column of node
    row_id = [0] * max_nodes         # which input row the node belongs to
    size = [0] * (ncol + 1)          # column sizes, 1‑based

    header = 0
    # initialise header row (circular list of column headers)
    for i in range(ncol + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol + 1  # next free index

    # add rows
    for rid, (a, b, c) in enumerate(triples, 1):
        first = None
        for col in (a, b, c):
            node = node_cnt
            node_cnt += 1
            C[node] = col
            row_id[node] = rid
            # vertical links
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            size[col] += 1
            # horizontal links within the row
            if first is None:
                first = node
                L[node] = R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

    solution_rows = []
    answer = []

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
        nonlocal found, answer
        if R[header] == header:          # all columns covered
            answer = solution_rows.copy()
            found = True
            return
        # choose column with minimal size
        c = R[header]
        min_sz = size[c]
        col = c
        j = R[c]
        while j != header:
            if size[j] < min_sz:
                min_sz = size[j]
                col = j
                if min_sz == 0:
                    break
            j = R[j]
        if min_sz == 0:
            return
        cover(col)
        r = D[col]
        while r != col and not found:
            solution_rows.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            search(k + 1)
            # backtrack
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(col)

    search(0)

    out = []
    if found:
        out.append("YES")
        for rid in answer:
            out.append(' '.join(map(str, triples[rid - 1])))
    else:
        out.append("NO")
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()