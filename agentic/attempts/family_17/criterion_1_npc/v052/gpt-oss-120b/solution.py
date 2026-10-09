import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    ncol = 3 * q                     # number of columns (elements)
    # dancing links arrays
    max_nodes = ncol + 3 * t + 5
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes               # column header of a node
    S = [0] * (ncol + 1)              # size of each column
    row_vals = {}                     # row_id -> tuple of three numbers

    # initialise column headers 1..ncol and head 0
    head = 0
    for i in range(ncol + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = ncol
    R[ncol] = 0

    node_id = ncol + 1                # next free node index
    row_id = 0

    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        row_id += 1
        cols = (a, b, c)
        first = None
        for col in cols:
            nid = node_id
            node_id += 1
            C[nid] = col
            # vertical links
            U[nid] = U[col]
            D[nid] = col
            D[U[col]] = nid
            U[col] = nid
            S[col] += 1
            # horizontal links within the row
            if first is None:
                first = nid
                L[nid] = R[nid] = nid
            else:
                # insert to the left of first
                L[nid] = L[first]
                R[nid] = first
                R[L[first]] = nid
                L[first] = nid
        row_vals[row_id] = cols

    # store mapping from node to its row id (needed for output)
    node_to_row = {}
    # we can assign row ids by scanning rows again, but easier: during creation we
    # know the three node ids; we can store them now.
    # Re‑iterate triples to fill node_to_row (small overhead)
    node_id = ncol + 1
    row_id = 0
    # rebuild reading input again is impossible; instead we stored row_vals only.
    # We'll later retrieve row id from a node by walking its row (any node) and
    # using a dict that maps the first node of each row to its id.
    # Simpler: store for each node its row id during creation.
    # Let's redo creation with that in mind.

def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it)); t = int(next(it))
    ncol = 3 * q
    max_nodes = ncol + 3 * t + 5
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes
    S = [0] * (ncol + 1)
    row_of_node = [0] * max_nodes
    row_vals = {}

    # initialise column headers
    for i in range(ncol + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = ncol
    R[ncol] = 0

    node_id = ncol + 1
    row_id = 0
    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        row_id += 1
        cols = (a, b, c)
        first = None
        for col in cols:
            nid = node_id
            node_id += 1
            C[nid] = col
            row_of_node[nid] = row_id
            # vertical
            U[nid] = U[col]
            D[nid] = col
            D[U[col]] = nid
            U[col] = nid
            S[col] += 1
            # horizontal
            if first is None:
                first = nid
                L[nid] = R[nid] = nid
            else:
                L[nid] = L[first]
                R[nid] = first
                R[L[first]] = nid
                L[first] = nid
        row_vals[row_id] = cols

    solution_rows = []

    def cover(c):
        # remove column header
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                S[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                S[C[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c

    sys.setrecursionlimit(10000)
    found = False

    def search(k):
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
            solution_rows.append(row_of_node[r])
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

    if search(0):
        out = ['YES']
        for rid in solution_rows:
            out.append(' '.join(map(str, row_vals[rid])))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    solve()