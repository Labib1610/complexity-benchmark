import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    n = 3 * q
    idx = 2
    triples = []
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        triples.append((a, b, c))

    if n % 3 != 0:
        print("NO")
        return

    # Map each vertex to list of triple indices
    adj = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triples):
        adj[a].append(i)
        adj[b].append(i)
        adj[c].append(i)

    # Build edge list: for each triple, 3 edges among its vertices
    # We'll use vertex-based adjacency with edge ids
    # Edge id encodes triple index and pair
    edges = []
    edge_adj = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triples):
        e0 = len(edges); edges.append((a, b, i))
        e1 = len(edges); edges.append((b, c, i))
        e2 = len(edges); edges.append((a, c, i))
        edge_adj[a].append(e0)
        edge_adj[b].append(e0)
        edge_adj[b].append(e1)
        edge_adj[c].append(e1)
        edge_adj[a].append(e2)
        edge_adj[c].append(e2)

    # We need perfect matching in 3-uniform hypergraph -> reduce to perfect matching in graph?
    # Actually exact cover by 3-sets is NP-complete in general, but here n <= 600, t <= 20000.
    # Need exact algorithm. Use DLX (Dancing Links) for exact cover.
    # But n=600, t=20000 could be large for DLX worst case. However constraints suggest maybe special structure?
    # Let's implement DLX with heuristics.

    # Build DLX structure
    # Columns: 1..n (vertices)
    # Rows: triples
    # We need exact cover of all columns.

    # Represent as sparse matrix
    # Use arrays for dancing links

    num_cols = n
    num_rows = t

    # For DLX, we need column headers and nodes
    # Node: left, right, up, down, col, row
    # We'll use lists

    # size estimate: 3*t nodes + num_cols headers + 1 root
    max_nodes = 3 * t + num_cols + 10
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes  # column index
    row_of = [0] * max_nodes  # row index
    size = [0] * (num_cols + 1)  # column sizes, 1-indexed

    # root = 0
    # column headers: 1..num_cols
    # Initialize column headers
    for j in range(1, num_cols + 1):
        L[j] = j - 1 if j > 1 else num_cols
        R[j] = j + 1 if j < num_cols else 1
        # Actually circular with root
    # Let's redo with root=0
    # root's right points to first col, left to last col
    R[0] = 1
    L[0] = num_cols
    for j in range(1, num_cols + 1):
        L[j] = j - 1
        R[j] = j + 1
        U[j] = j
        D[j] = j
        C[j] = j
        row_of[j] = 0
        size[j] = 0
    R[num_cols] = 0
    L[1] = 0

    node_id = num_cols + 1

    # For each row, create nodes and link vertically
    # Also need row's first node to potentially remove entire row
    row_first = [0] * (num_rows + 1)  # 1-indexed rows

    for r in range(1, num_rows + 1):
        a, b, c = triples[r - 1]
        cols = [a, b, c]
        first = node_id
        prev = None
        for col in cols:
            nid = node_id
            node_id += 1
            # vertical links
            up = U[col]
            D[nid] = col
            U[nid] = up
            D[up] = nid
            U[col] = nid
            # horizontal links within row
            if prev is not None:
                L[nid] = prev
                R[prev] = nid
            else:
                first = nid
            prev = nid
            C[nid] = col
            row_of[nid] = r
            size[col] += 1
        # close the row circle
        L[first] = prev
        R[prev] = first
        row_first[r] = first

    solution = []
    found = [False]

    def cover(col):
        # remove column header from header list
        Lc = L[col]; Rc = R[col]
        R[Lc] = Rc
        L[Rc] = Lc
        i = D[col]
        while i != col:
            j = R[i]
            while j != i:
                Dj = D[j]; Uj = U[j]
                U[Dj] = Uj
                D[Uj] = Dj
                size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                Dj = D[j]; Uj = U[j]
                U[Dj] = j
                D[Uj] = j
                size[C[j]] += 1
                j = L[j]
            i = U[i]
        Lc = L[col]; Rc = R[col]
        R[Lc] = col
        L[Rc] = col

    def search(k):
        if R[0] == 0:
            found[0] = True
            return True
        # choose column with minimum size
        c = R[0]
        best = size[c]
        j = R[c]
        while j != 0:
            s = size[j]
            if s < best:
                best = s
                c = j
                if s <= 1:
                    break
            j = R[j]
        if best == 0:
            return False
        cover(c)
        r = D[c]
        while r != c and not found[0]:
            # cover all other columns in this row
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            solution.append(row_of[r])
            if search(k + 1):
                return True
            solution.pop()
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            r = D[r]
        uncover(c)
        return False

    # Quick pruning: if any vertex has no triples, impossible
    for v in range(1, n + 1):
        if not adj[v]:
            print("NO")
            return

    ok = search(0)
    if not ok:
        print("NO")
        return
    print("YES")
    for r in solution:
        a, b, c = triples[r - 1]
        print(f"{a} {b} {c}")

solve()