import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # columns: 0..k-1   specialists X
    #          k..2k-1  machines Y
    #          2k..3k-1 time slots Z
    n_cols = 3 * k
    rows = []          # list of list of column indices
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        rows.append([x, k + y, 2 * k + z])

    # Build dancing links structure
    max_nodes = t * 3 + n_cols + 1
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes   # column header for each node
    S = [0] * (n_cols + 1)  # column sizes, header 0 is root
    row_id = [0] * max_nodes

    # header node 0 is root
    for i in range(n_cols + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n_cols
    R[n_cols] = 0

    node_cnt = n_cols + 1

    for r_idx, cols in enumerate(rows):
        first = -1
        for col in cols:
            node = node_cnt
            node_cnt += 1
            C[node] = col + 1          # column headers are 1..n_cols
            row_id[node] = r_idx

            # vertical links
            U[node] = U[C[node]]
            D[node] = C[node]
            D[U[node]] = node
            U[D[node]] = node
            S[C[node]] += 1

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

    sys.setrecursionlimit(10000)

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

    def search(depth=0):
        if R[0] == 0:          # all columns covered
            return True
        # choose column with minimal size
        c = R[0]
        min_s = S[c]
        col = c
        j = R[c]
        while j != 0:
            if S[j] < min_s:
                min_s = S[j]
                col = j
                if min_s == 0:
                    break
            j = R[j]
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
            if search(depth + 1):
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
        for rid in solution_rows:
            x, y, z = rows[rid]
            out.append(f"{x+1} {y - k +1} {z - 2*k +1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()