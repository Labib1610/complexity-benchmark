import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q                     # number of columns
    rows = []                     # list of triples
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        rows.append((a, b, c))

    # ---------- DLX construction ----------
    max_nodes = 3 * t + n + 5
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes
    row_id = [0] * max_nodes

    size = [0] * (n + 1)          # column sizes, column headers are 1..n
    head = 0

    # header list (circular)
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = n
    R[n] = 0

    node_cnt = n + 1              # next free index

    for rid, (a, b, c) in enumerate(rows, 1):
        cols = [a + 1, b + 1, c + 1]   # shift to 1..n
        first = None
        for col in cols:
            idx = node_cnt
            node_cnt += 1
            C[idx] = col
            row_id[idx] = rid

            # vertical links
            U[idx] = U[col]
            D[idx] = col
            D[U[col]] = idx
            U[col] = idx
            size[col] += 1

            # horizontal links
            if first is None:
                first = idx
                L[idx] = R[idx] = idx
            else:
                L[idx] = L[first]
                R[idx] = first
                R[L[first]] = idx
                L[first] = idx

    # ---------- DLX operations ----------
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

    solution = []

    # heuristic: choose column with minimal size
    def choose_column():
        c = R[head]
        min_sz = size[c]
        cur = c
        while cur != head:
            if size[cur] < min_sz:
                min_sz = size[cur]
                c = cur
                if min_sz == 0:
                    break
            cur = R[cur]
        return c

    found = False

    def search(k):
        nonlocal found
        if R[head] == head:
            # all columns covered
            found = True
            return True
        c = choose_column()
        if size[c] == 0:
            return False
        cover(c)
        r = D[c]
        while r != c:
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
        uncover(c)
        return False

    if search(0):
        out = ['YES']
        # solution rows are stored as original indices (1‑based)
        for rid in solution:
            a, b, c = rows[rid - 1]
            out.append(f"{a+1} {b+1} {c+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()