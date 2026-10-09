import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []
    for _ in range(t):
        x = int(next(it)) - 1  # zero based
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))

    # columns: 0..k-1   frequencies
    #          k..2k-1 amplitudes
    #          2k..3k-1 phases
    ncol = 3 * k

    # DLX structures
    # header node 0, columns 1..ncol
    size = 1 + ncol
    U = [0] * (size + 3 * t)
    D = [0] * (size + 3 * t)
    L = [0] * (size + 3 * t)
    R = [0] * (size + 3 * t)
    C = [0] * (size + 3 * t)   # column of node
    S = [0] * (ncol + 1)       # column sizes, 1‑based

    # init column headers linked horizontally
    for i in range(ncol + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol + 1
    row_node = []          # first node index of each row (for answer)

    for idx, (x, y, z) in enumerate(triples):
        cols = [x + 1, k + y + 1, 2 * k + z + 1]   # column numbers (1‑based)
        first = None
        for col in cols:
            node = node_cnt
            node_cnt += 1
            C[node] = col
            # vertical links
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            S[col] += 1
            # horizontal links within the row
            if first is None:
                first = node
                L[node] = R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node
        row_node.append(first)

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

    def search(depth: int) -> None:
        nonlocal solved
        if R[0] == 0:          # all columns covered
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
        while r != c and not solved:
            answer_rows.append(r)
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            search(depth + 1)
            if solved:
                return
            # backtrack
            answer_rows.pop()
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            r = D[r]
        uncover(c)

    search(0)

    if not solved:
        print("NO")
        return

    # retrieve original triples from selected rows
    used = set()
    result = []
    for node in answer_rows:
        # each row consists of three nodes; we can walk the row to collect columns
        cols = []
        j = node
        while True:
            cols.append(C[j] - 1)   # zero based column index
            j = R[j]
            if j == node:
                break
        # decode to (x,y,z)
        fx = cols[0] if cols[0] < k else (cols[1] if cols[1] < k else cols[2])
        # find which column belongs to which type
        x = y = z = -1
        for col in cols:
            if col < k:
                x = col
            elif col < 2 * k:
                y = col - k
            else:
                z = col - 2 * k
        result.append((x + 1, y + 1, z + 1))

    print("YES")
    for triple in result:
        print(*triple)


if __name__ == "__main__":
    solve()