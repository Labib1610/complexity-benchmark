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
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    # ---------- DLX construction ----------
    max_nodes = 3 * t + n + 5
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes
    S = [0] * (n + 1)          # column sizes, columns are 1..n
    H = [-1] * t               # head node of each row

    # header node 0, column headers 1..n
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_cnt = n
    for r, (a, b, c) in enumerate(triples):
        cols = [a + 1, b + 1, c + 1]   # shift to 1‑based column ids
        first = -1
        for col in cols:
            node_cnt += 1
            C[node_cnt] = col
            # insert into column (at bottom, before header)
            U[node_cnt] = U[col]
            D[node_cnt] = col
            D[U[col]] = node_cnt
            U[col] = node_cnt
            S[col] += 1
            if first == -1:
                first = node_cnt
                L[node_cnt] = R[node_cnt] = node_cnt
            else:
                # insert into row list (to the left of first)
                L[node_cnt] = L[first]
                R[node_cnt] = first
                R[L[first]] = node_cnt
                L[first] = node_cnt
        H[r] = first

    # ---------- DLX operations ----------
    def cover(col: int) -> None:
        # remove column header
        R[L[col]] = R[col]
        L[R[col]] = L[col]
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
        R[L[col]] = col
        L[R[col]] = col

    solution_rows = [0] * q
    found = False

    # ---------- recursive search ----------
    def search(k: int) -> bool:
        nonlocal found
        if R[0] == 0:          # all columns covered
            return True
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
            return False
        cover(c)
        r = D[c]
        while r != c:
            solution_rows[k] = r
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
            r = D[r]
        uncover(c)
        return False

    if search(0):
        out = ["YES"]
        for idx in range(q):
            row_node = solution_rows[idx]
            # collect three columns of this row
            cols = []
            j = row_node
            while True:
                cols.append(C[j] - 1)   # back to 0‑based badge numbers
                j = R[j]
                if j == row_node:
                    break
            cols.sort()
            out.append(f"{cols[0]+1} {cols[1]+1} {cols[2]+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()