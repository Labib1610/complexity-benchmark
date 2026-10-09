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

    ncol = 3 * q
    # DLX structures
    # node 0 is the head
    size = [0] * (ncol + 1)          # column sizes, index 1..ncol
    col = []                         # column of each node
    row_id = []                      # row index of each node
    L = []; R = []; U = []; D = []

    # create column headers 1..ncol
    for i in range(ncol + 1):
        L.append(i - 1)
        R.append(i + 1)
        U.append(i)
        D.append(i)
        col.append(i)   # header's own column number
        row_id.append(-1)
    L[0] = ncol
    R[ncol] = 0

    # function to add a node
    def add_node(c, r):
        idx = len(col)
        col.append(c)
        row_id.append(r)
        # vertical links
        U.append(U[c])
        D.append(c)
        L.append(0); R.append(0)   # temporary
        D[U[c]] = idx
        U[c] = idx
        size[c] += 1
        return idx

    # build rows
    for rid, (a, b, c) in enumerate(triples):
        nodes = [add_node(a, rid), add_node(b, rid), add_node(c, rid)]
        # link horizontally (circular)
        for i in range(3):
            L[nodes[i]] = nodes[(i - 1) % 3]
            R[nodes[i]] = nodes[(i + 1) % 3]

    # cover / uncover
    def cover(c):
        # remove column header
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        # for each row i in column c
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                # unlink node j from its column
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                size[col[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[col[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c

    solution_rows = []
    answer = []

    # heuristic: choose column with minimal size
    def choose_column():
        c = R[0]
        min_sz = size[c]
        best = c
        while c != 0:
            if size[c] < min_sz:
                min_sz = size[c]
                best = c
                if min_sz == 0:
                    break
            c = R[c]
        return best

    found = False

    def search(k):
        nonlocal found, answer
        if R[0] == 0:
            # all columns covered
            answer = [triples[r] for r in solution_rows]
            found = True
            return True
        c = choose_column()
        if size[c] == 0:
            return False
        cover(c)
        r = D[c]
        while r != c:
            solution_rows.append(row_id[r])
            j = R[r]
            while j != r:
                cover(col[j])
                j = R[j]
            if search(k + 1):
                return True
            # backtrack
            j = L[r]
            while j != r:
                uncover(col[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(c)
        return False

    if search(0):
        out = ["YES"]
        for a, b, c in answer:
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()