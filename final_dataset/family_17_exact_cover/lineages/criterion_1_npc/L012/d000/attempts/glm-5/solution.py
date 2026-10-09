import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0]); t = int(data[1])
    n = 3 * q
    idx = 2
    triples = []
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        triples.append((a, b, c))

    # Build adjacency: for each pair, list of third vertices
    adj = [[] for _ in range(n+1)]
    for tid, (a, b, c) in enumerate(triples):
        adj[a].append((b, c, tid))
        adj[b].append((a, c, tid))
        adj[c].append((a, b, tid))

    # For each vertex, sort neighbors by degree of the pair (b,c) to prefer low-degree pairs
    # We'll use a simple greedy with backtracking via iterative deepening is too slow.
    # Instead use exact cover with DLX-like approach but triples are size 3.
    # Given constraints q<=200, n<=600, t<=20000, we need efficient exact cover.
    # We'll implement Algorithm X with dancing links optimized for triples.

    # Map triples to columns 1..n
    # Build sparse matrix
    # We'll use arrays for DLX
    # Each node: left, right, up, down, col, row
    # Column headers: size
    # Since n<=600 and t<=20000, total nodes = 3*t <= 60000, manageable.

    # Build column array
    # columns 1..n
    col_size = [0] * (n + 1)
    # We'll build nodes
    # node arrays
    L = [0]; R = [0]; U = [0]; D = [0]; C = [0]; row_of = [0]
    # header node is 0
    # column headers nodes 1..n
    # We'll create column headers
    # Actually DLX: header is node 0, columns are 1..n
    # Initialize column headers linked in a circular list
    # We'll append nodes dynamically

    # Let's build using lists
    # node 0 = root
    L.append(0); R.append(0); U.append(0); D.append(0); C.append(0); row_of.append(-1)
    # columns 1..n
    for j in range(1, n+1):
        node = len(L)
        L.append(node); R.append(node); U.append(node); D.append(node); C.append(j); row_of.append(-1)
        col_size[j] = 0
        # link into header list
        # insert before root
        left_node = L[0]
        L[0] = node
        R[node] = 0
        L[node] = left_node
        R[left_node] = node

    # Now add rows
    # For each triple, create 3 nodes
    row_nodes = []  # list of list of node ids per row
    for tid, (a, b, c) in enumerate(triples):
        nodes = []
        for v in (a, b, c):
            node = len(L)
            # column header node is v
            # insert into column v
            up_node = U[v]
            D[up_node] = node
            U[node] = up_node
            U[v] = node
            D[node] = v
            C.append(v)
            L.append(node); R.append(node); U.append(node); D.append(node)
            row_of.append(tid)
            col_size[v] += 1
            nodes.append(node)
        # link nodes in row circularly
        for i in range(3):
            nodes[i] = nodes[i]
        # link
        for i in range(3):
            ni = nodes[i]
            nj = nodes[(i+1)%3]
            R[ni] = nj
            L[nj] = ni
        row_nodes.append(nodes)

    # DLX solve
    solution = []
    found = [False]

    def cover(col):
        # remove column header from header list
        Lc = L[col]; Rc = R[col]
        R[Lc] = Rc
        L[Rc] = Lc
        # for each node in column, remove rows
        i = D[col]
        while i != col:
            j = R[i]
            while j != i:
                Dn = D[j]; Un = U[j]
                U[Dn] = Un
                D[Un] = Dn
                col_size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                Dn = D[j]; Un = U[j]
                U[Dn] = j
                D[Un] = j
                col_size[C[j]] += 1
                j = L[j]
            i = U[i]
        Lc = L[col]; Rc = R[col]
        R[Lc] = col
        L[Rc] = col

    def search(k):
        if R[0] == 0:
            found[0] = True
            return True
        # choose column with smallest size
        c = R[0]
        best = col_size[c]
        j = R[c]
        while j != 0:
            s = col_size[j]
            if s < best:
                best = s
                c = j
                if best <= 1:
                    break
            j = R[j]
        if best == 0:
            return False
        cover(c)
        r = D[c]
        while r != c and not found[0]:
            # choose this row
            tid = row_of[r]
            solution.append(tid)
            # cover other columns in row
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            if search(k+1):
                # uncover not needed if found
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

    search(0)
    if found[0]:
        out = ["YES"]
        for tid in solution:
            a, b, c = triples[tid]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()