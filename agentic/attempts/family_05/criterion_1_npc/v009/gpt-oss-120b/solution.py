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

    ncol = 3 * k
    max_nodes = t * 3 + ncol + 1

    # DLX structures
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes          # column header for each node
    S = [0] * (ncol + 1)         # size of each column (header 0..ncol-1)
    row_id = [0] * max_nodes     # which input row a node belongs to

    # header node is 0
    for i in range(ncol + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol + 1

    def add_node(col, r):
        nonlocal node_cnt
        idx = node_cnt
        node_cnt += 1
        C[idx] = col
        row_id[idx] = r

        # vertical links
        U[idx] = U[col]
        D[idx] = col
        D[U[col]] = idx
        U[col] = idx
        S[col] += 1

        # horizontal links (temporarily point to self)
        L[idx] = R[idx] = idx
        return idx

    # build rows
    row_head = [0] * t
    for r, (x, y, z) in enumerate(rows):
        cols = [x, k + y, 2 * k + z]
        first = None
        for col in cols:
            nd = add_node(col, r)
            if first is None:
                first = nd
            else:
                # link horizontally
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd
        row_head[r] = first

    solution = []
    found = False

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

    sys.setrecursionlimit(10000)

    def search(k_depth):
        nonlocal found
        if R[0] == 0:  # all columns covered
            found = True
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
            solution.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            if search(k_depth + 1):
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

    if search(0):
        out = ["YES"]
        for rid in solution:
            x, y, z = rows[rid]
            out.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()