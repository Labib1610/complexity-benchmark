import sys
sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q                     # number of columns
    rows = []                     # list of triples (as ints)
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        rows.append((a, b, c))

    # ---------- DLX construction ----------
    max_nodes = 3 * t + n + 1      # +1 for header
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes           # column of node
    row_id = [0] * max_nodes      # which original row this node belongs to
    col_size = [0] * (n + 1)      # size of each column, 1..n

    header = 0
    # link header with column headers 1..n
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = n
    R[n] = 0

    node_cnt = n + 1  # next free index

    for rid, (a, b, c) in enumerate(rows, 1):
        first = None
        for col in (a, b, c):
            col += 1                     # shift to 1..n
            node = node_cnt
            node_cnt += 1
            C[node] = col
            row_id[node] = rid

            # insert into column (at bottom, before header)
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            col_size[col] += 1

            # link row horizontally
            if first is None:
                first = node
                L[node] = R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

    solution = []

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
                col_size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                col_size[C[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[col]] = col
        R[L[col]] = col

    def search(k):
        if R[header] == header:          # all columns covered
            return True
        # choose column with minimal size
        c = R[header]
        min_sz = col_size[c]
        col = c
        j = R[c]
        while j != header:
            if col_size[j] < min_sz:
                min_sz = col_size[j]
                col = j
                if min_sz == 0:
                    break
            j = R[j]
        if min_sz == 0:
            return False
        cover(col)
        r = D[col]
        while r != col:
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
        uncover(col)
        return False

    ok = search(0)
    out = sys.stdout
    if not ok:
        out.write("NO")
        return
    out.write("YES\n")
    # output triples in any order
    for rid in solution:
        a, b, c = rows[rid - 1]
        out.write(f"{a+1} {b+1} {c+1}\n")

if __name__ == "__main__":
    solve()