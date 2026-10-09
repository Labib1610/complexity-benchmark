import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    # columns: 0..k-1   primary
    #          k..2k-1 secondary
    #          2k..3k-1 tertiary
    ncol = 3 * k

    # DLX structures
    size = [0] * ncol          # number of nodes in column
    col_head = list(range(ncol))  # column header id (itself)
    # header list (circular doubly linked)
    L = [-1] * (ncol + 1)
    R = [-1] * (ncol + 1)
    for i in range(ncol + 1):
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    # node arrays
    U = []
    D = []
    C = []   # column of node
    row_id = []  # which original row this node belongs to

    # row header list (optional)
    row_head = [-1] * len(triples)

    def add_node(col, r):
        idx = len(U)
        U.append(idx)
        D.append(idx)
        C.append(col)
        row_id.append(r)
        # insert into column list (at bottom)
        if size[col] == 0:
            # first node in column, points to itself
            U[idx] = idx
            D[idx] = idx
        else:
            # insert before column header (which is not stored, we use first node)
            first = col_nodes[col][0]
            last = U[first]
            D[last] = idx
            U[idx] = last
            D[idx] = first
            U[first] = idx
        size[col] += 1
        return idx

    # To simplify, we will build column lists after all nodes are created.
    # We'll store nodes per column temporarily.
    col_nodes = [[] for _ in range(ncol)]

    # create nodes
    for r, (a, b, c) in enumerate(triples):
        cols = [a, k + b, 2 * k + c]
        first = -1
        prev = -1
        for col in cols:
            idx = len(U)
            U.append(-1)  # placeholder
            D.append(-1)
            C.append(col)
            row_id.append(r)
            col_nodes[col].append(idx)
            if first == -1:
                first = idx
            if prev != -1:
                L[idx] = prev
                R[prev] = idx
            prev = idx
        # close row circular links
        L[first] = prev
        R[prev] = first
        row_head[r] = first

    # now link column lists vertically
    for col in range(ncol):
        nodes = col_nodes[col]
        sz = len(nodes)
        size[col] = sz
        for i, idx in enumerate(nodes):
            up = nodes[i - 1] if i > 0 else nodes[-1]
            down = nodes[(i + 1) % sz]
            U[idx] = up
            D[idx] = down

    # header node 0 is dummy, columns are 1..ncol (shift by +1)
    # we will use column ids 1..ncol in the header list
    # map real column -> header id
    col_to_hdr = [i + 1 for i in range(ncol)]

    # adjust header links to include only columns with size>0
    # initially all columns are present
    # header node is 0
    # already set L,R above, but they include dummy at ncol+1; we need correct size
    # Actually we built L,R for 0..ncol, where 0 is dummy left of first column (col 0)
    # and ncol is dummy right of last column. That's fine.

    # functions for cover/uncover
    def cover(col):
        # remove column header
        c = col_to_hdr[col]
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        # for each row i in column
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                # remove node j from its column
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        c = col_to_hdr[col]
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[C[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c

    solution_rows = []
    found = False

    def search():
        nonlocal found
        if R[0] == 0:  # no columns left
            found = True
            return True
        # choose column with minimal size
        c = R[0]
        min_sz = size[col_to_hdr.index(c)-1]  # not efficient, we will compute differently
        # better: iterate columns
        best = -1
        best_sz = 10**9
        j = R[0]
        while j != 0:
            col = j - 1
            if size[col] < best_sz:
                best_sz = size[col]
                best = col
                if best_sz == 0:
                    break
            j = R[j]
        if best_sz == 0:
            return False
        cover(best)
        # iterate rows
        c_hdr = col_to_hdr[best]
        r = D[c_hdr]
        while r != c_hdr:
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
        uncover(best)
        return False

    # The above header handling is messy; rewrite with proper mapping.

    # Rebuild with proper DLX using classic implementation (simpler).

def solve():
    import sys
    sys.setrecursionlimit(1000000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it)); t = int(next(it))
    triples = []
    for _ in range(t):
        a = int(next(it))-1
        b = int(next(it))-1
        c = int(next(it))-1
        triples.append((a,b,c))

    ncol = 3*k
    # DLX structures
    max_nodes = t*3 + ncol + 1
    U = [0]*max_nodes
    D = [0]*max_nodes
    L = [0]*max_nodes
    R = [0]*max_nodes
    C = [0]*max_nodes
    S = [0]*ncol          # column sizes
    row_of = [0]*max_nodes

    header = 0
    # header list: 0 is root, columns are 1..ncol
    for i in range(ncol+1):
        L[i] = i-1
        R[i] = i+1
    L[0] = ncol
    R[ncol] = 0

    # column headers are nodes 1..ncol, each column i corresponds to element i-1
    for i in range(1, ncol+1):
        U[i] = D[i] = i

    node_cnt = ncol+1

    def add_row(rid, cols):
        nonlocal node_cnt
        first = -1
        for col in cols:
            col_id = col+1
            node = node_cnt
            node_cnt += 1
            C[node] = col_id
            row_of[node] = rid
            # vertical link
            U[node] = U[col_id]
            D[node] = col_id
            D[U[col_id]] = node
            U[col_id] = node
            S[col] += 1
            # horizontal link
            if first == -1:
                first = node
                L[node] = R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node
        return

    for idx, (a,b,c) in enumerate(triples):
        add_row(idx, [a, k+b, 2*k+c])

    solution = []
    found = False

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
                S[C[j]-1] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                S[C[j]-1] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[col]] = col
        R[L[col]] = col

    def search():
        nonlocal found
        if R[header] == header:
            found = True
            return True
        # choose column with minimal size
        c = R[header]
        min_s = S[C[c]-1]
        col = c
        j = R[c]
        while j != header:
            if S[C[j]-1] < min_s:
                min_s = S[C[j]-1]
                col = j
                if min_s == 0:
                    break
            j = R[j]
        if min_s == 0:
            return False
        cover(col)
        r = D[col]
        while r != col:
            solution.append(row_of[r])
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
            solution.pop()
            r = D[r]
        uncover(col)
        return False

    if search():
        out = ["YES"]
        for rid in solution:
            a,b,c = triples[rid]
            out.append(f"{a+1} {b+1} {c+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()