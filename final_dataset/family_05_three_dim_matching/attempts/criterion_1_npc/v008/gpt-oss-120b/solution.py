import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # columns: 0..k-1   specialists
    #          k..2k-1  machines
    #          2k..3k-1 time slots
    ncol = 3 * k

    rows = []          # list of triples (x,y,z)
    row_cols = []      # list of column indices for each row

    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        cols = [x, k + y, 2 * k + z]
        rows.append((x + 1, y + 1, z + 1))
        row_cols.append(cols)

    # ---------- DLX structures ----------
    # header node is 0, column nodes are 1..ncol
    max_nodes = 1 + ncol + len(row_cols) * 3 + 5
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes          # column of a node
    S = [0] * (ncol + 1)         # size of column (only for column headers)

    # initialise column headers linked horizontally
    for i in range(ncol + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    node_id = ncol + 1

    # add rows
    for r, cols in enumerate(row_cols):
        first = -1
        for col in cols:
            col_node = col + 1          # column header index (1‑based)
            # create node
            C[node_id] = col_node
            # vertical links
            U[node_id] = U[col_node]
            D[node_id] = col_node
            D[U[col_node]] = node_id
            U[col_node] = node_id
            S[col_node] += 1
            # horizontal links within the row
            if first == -1:
                first = node_id
                L[node_id] = R[node_id] = node_id
            else:
                L[node_id] = L[first]
                R[node_id] = first
                R[L[first]] = node_id
                L[first] = node_id
            node_id += 1

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

    found = False

    def search():
        nonlocal found
        if R[0] == 0:          # no columns left
            found = True
            return True
        # choose column with minimal size
        c = R[0]
        min_s = S[c]
        j = R[c]
        while j != 0:
            if S[j] < min_s:
                min_s = S[j]
                c = j
                if min_s == 0:
                    break
            j = R[j]
        if min_s == 0:
            return False
        cover(c)
        r = D[c]
        while r != c:
            solution_rows.append(r)   # store a node belonging to the row
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
        uncover(c)
        return False

    if search():
        # translate stored nodes back to row indices
        # each stored node belongs to a row; we can retrieve the row by walking left until column header
        output = []
        for node in solution_rows:
            cols = []
            j = node
            while True:
                col = C[j] - 1
                cols.append(col)
                j = R[j]
                if j == node:
                    break
            # cols contains three column indices
            # map back to (x,y,z)
            x = cols[0] if cols[0] < k else (cols[1] if cols[1] < k else cols[2])
            # find which is specialist, machine, time
            spec = next(c for c in cols if c < k)
            mach = next(c for c in cols if k <= c < 2 * k) - k
            tim  = next(c for c in cols if 2 * k <= c) - 2 * k
            output.append((spec + 1, mach + 1, tim + 1))
        sys.stdout.write("YES\n")
        for triple in output:
            sys.stdout.write(f"{triple[0]} {triple[1]} {triple[2]}\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()