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
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))

    # Dancing Links for exact cover: columns 0..3k-1 (x0..x{k-1}, y0..y{k-1}, z0..z{k-1})
    ncol = 3 * k
    # header node 0, column headers 1..ncol
    size = 1  # next free node index
    U = [0] * (1 + t * 3 + ncol + 5)
    D = [0] * (1 + t * 3 + ncol + 5)
    L = [0] * (1 + t * 3 + ncol + 5)
    R = [0] * (1 + t * 3 + ncol + 5)
    C = [0] * (1 + t * 3 + ncol + 5)   # column of node
    S = [0] * (ncol + 1)               # column sizes, index 1..ncol
    row_id = [0] * (1 + t * 3 + ncol + 5)

    # init header list
    for i in range(ncol + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    # add rows
    for rid, (x, y, z) in enumerate(triples):
        cols = [x + 1, k + y + 1, 2 * k + z + 1]  # column numbers (1-indexed)
        first = None
        for col in cols:
            node = size
            size += 1
            C[node] = col
            row_id[node] = rid
            # vertical links
            D[node] = col
            U[node] = U[col]
            D[U[col]] = node
            U[col] = node
            S[col] += 1
            # horizontal links
            if first is None:
                first = node
                L[node] = R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

    solution_rows = []

    def cover(col):
        # remove column header
        L[R[col]] = L[col]
        R[L[col]] = R[col]
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

    def search(kdepth):
        if R[0] == 0:  # all columns covered
            return True
        # choose column with minimal S
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
            return False
        cover(c)
        r = D[c]
        while r != c:
            solution_rows.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            if search(kdepth + 1):
                return True
            # backtrack
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(c)
        return False

    found = search(0)
    if not found:
        print("NO")
        return
    print("YES")
    for rid in solution_rows:
        x, y, z = triples[rid]
        print(x + 1, y + 1, z + 1)

if __name__ == "__main__":
    solve()