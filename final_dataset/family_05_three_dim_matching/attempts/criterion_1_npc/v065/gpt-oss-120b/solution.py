import sys
sys.setrecursionlimit(10000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    rows = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        rows.append((x, y, z))

    n_cols = 3 * k
    # DLX structures
    max_nodes = t * 3 + n_cols + 5
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes  # column header for each node
    S = [0] * (n_cols)   # size of column
    row_id = [0] * max_nodes

    header = n_cols  # index of master header
    # init column headers 0..n_cols-1
    for i in range(n_cols):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
        C[i] = i
    L[0] = header
    R[n_cols - 1] = header
    L[header] = n_cols - 1
    R[header] = 0

    node_cnt = n_cols
    # add rows
    for rid, (x, y, z) in enumerate(rows):
        cols = [x, k + y, 2 * k + z]
        first = -1
        for col in cols:
            node = node_cnt
            node_cnt += 1
            C[node] = col
            row_id[node] = rid
            # vertical links
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            S[col] += 1
            # horizontal links
            if first == -1:
                first = node
                L[node] = R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

    solution = []
    ans_rows = []

    def cover(col):
        # remove column header
        R[L[col]] = R[col]
        L[R[col]] = L[col]
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
        R[L[col]] = col
        L[R[col]] = col

    def search(k_sel):
        if R[header] == header:
            # all columns covered
            ans_rows.extend(solution)
            return True
        # choose column with minimal size
        c = R[header]
        min_s = S[c]
        col = c
        j = R[c]
        while j != header:
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
            solution.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            if search(k_sel + 1):
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

    possible = search(0)
    if not possible:
        print("NO")
    else:
        print("YES")
        for rid in ans_rows:
            x, y, z = rows[rid]
            print(x + 1, y + 1, z + 1)

if __name__ == "__main__":
    solve()