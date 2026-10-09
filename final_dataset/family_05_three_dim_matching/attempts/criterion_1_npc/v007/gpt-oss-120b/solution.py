import sys

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

    # DLX structures
    n_cols = 3 * k  # columns: X0..Xk-1, Y0..Yk-1, Z0..Zk-1
    # column headers
    size = [0] * n_cols
    col_head = list(range(n_cols))
    # node links
    U = []
    D = []
    L = []
    R = []
    C = []  # column of node
    row_id = []  # which row this node belongs to

    # header node 0..n_cols-1 are column headers, plus a root at index n_cols
    root = n_cols
    total_nodes = n_cols + 1
    U = list(range(total_nodes))
    D = list(range(total_nodes))
    L = list(range(total_nodes))
    R = list(range(total_nodes))
    C = [-1] * total_nodes
    row_id = [-1] * total_nodes

    # link column headers circularly
    for i in range(n_cols):
        L[i] = i - 1 if i > 0 else root
        R[i] = i + 1 if i + 1 < n_cols else root
    L[root] = n_cols - 1
    R[root] = 0

    def add_row(rid, cols):
        first = None
        for col in cols:
            node = len(U)
            U.append(U[col])
            D.append(col)
            L.append(0)
            R.append(0)
            C.append(col)
            row_id.append(rid)

            # insert into column
            D[U[col]] = node
            U[col] = node

            size[col] += 1

            if first is None:
                first = node
                L[node] = R[node] = node
            else:
                # link into row list
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

    for idx, (x, y, z) in enumerate(rows):
        add_row(idx, [x, k + y, 2 * k + z])

    solution = []

    def cover(col):
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
        R[L[col]] = col
        L[R[col]] = col

    def search():
        if R[root] == root:
            return True
        # choose column with minimal size
        c = R[root]
        min_sz = size[c]
        col = c
        j = R[c]
        while j != root:
            if size[j] < min_sz:
                min_sz = size[j]
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
            if search():
                return True
            # backtrack
            solution.pop()
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            r = D[r]
        uncover(col)
        return False

    if search():
        out = ["YES"]
        for rid in solution:
            x, y, z = rows[rid]
            out.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()