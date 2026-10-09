import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q  # number of elements
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    # ---- DLX structures ----
    # Header node is 0, column headers are 1..n
    # Each node: left, right, up, down, column, row_id
    max_nodes = t * 3 + n + 1
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes
    row_id = [0] * max_nodes

    size = [0] * (n + 1)  # column sizes, index 0 unused

    # initialize header and column headers
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = n
    R[n] = 0

    node_cnt = n + 1  # next free node index

    # add rows (triples)
    for rid, (a, b, c) in enumerate(triples):
        first = -1
        for col in (a, b, c):
            col += 1  # shift to 1..n
            node = node_cnt
            node_cnt += 1

            # vertical links
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node

            C[node] = col
            row_id[node] = rid

            size[col] += 1

            # horizontal links
            if first == -1:
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

    def uncover(col):
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

    def search(k):
        if R[0] == 0:  # all columns covered
            return True
        # choose column with minimal size
        c = R[0]
        min_sz = size[c]
        j = R[c]
        while j != 0:
            if size[j] < min_sz:
                c = j
                min_sz = size[j]
                if min_sz == 0:
                    break
            j = R[j]
        if min_sz == 0:
            return False

        cover(c)
        r = D[c]
        while r != c:
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
        uncover(c)
        return False

    possible = search(0)

    out = []
    if possible:
        out.append("YES")
        for rid in solution_rows:
            a, b, c = triples[rid]
            out.append(f"{a+1} {b+1} {c+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()