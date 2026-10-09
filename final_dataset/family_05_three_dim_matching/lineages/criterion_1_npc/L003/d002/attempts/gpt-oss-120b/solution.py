import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # columns: 0..3k-1  (L0..Lk-1, R0..Rk-1, K0..Kk-1)
    ncol = 3 * k
    rows = []                     # list of (left, right, key) 0‑based
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        rows.append((x, y + k, z + 2 * k))

    # ---------- DLX structures ----------
    max_nodes = 3 * t + ncol + 1
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes          # column header for each node
    S = [0] * (ncol + 1)         # size of each column (header 0 unused)
    row_id = [0] * max_nodes     # which original row a node belongs to

    # header node 0, column headers 1..ncol
    for i in range(ncol + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol + 1  # next free index

    for r_idx, cols in enumerate(rows):
        first = -1
        for col in cols:
            node = node_cnt
            node_cnt += 1
            C[node] = col + 1          # column header index (1‑based)
            row_id[node] = r_idx

            # insert into column (at bottom)
            D[node] = C[col + 1]
            U[node] = U[C[col + 1]]
            D[U[node]] = node
            U[D[node]] = node
            S[col + 1] += 1

            # link row horizontally
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

    sys.setrecursionlimit(10000)

    def search():
        if R[0] == 0:          # no columns left
            return True
        # choose column with minimal size
        c = R[0]
        min_s = S[c]
        col = c
        while c != 0:
            if S[c] < min_s:
                min_s = S[c]
                col = c
                if min_s == 0:
                    break
            c = R[c]
        if min_s == 0:
            return False

        cover(col)
        r = D[col]
        while r != col:
            solution_rows.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            if search():
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

    if search():
        out = ["YES"]
        for idx in solution_rows:
            x, y, z = rows[idx]
            out.append(f"{x+1} {y - k +1} {z - 2*k +1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()