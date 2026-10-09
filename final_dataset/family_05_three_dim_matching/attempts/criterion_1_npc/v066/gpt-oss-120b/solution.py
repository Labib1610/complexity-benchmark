import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))

    n_cols = 3 * k  # specialist, facility, dossier

    # Dancing Links structures
    max_nodes = t * 3 + n_cols + 1
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes          # column header for each node
    S = [0] * (n_cols + 1)       # size of each column (header 0 unused)
    row_id = [0] * max_nodes     # which input row a node belongs to

    # header node is 0
    for i in range(n_cols + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n_cols
    R[n_cols] = 0

    node_cnt = n_cols + 1

    def add_node(col, rid):
        nonlocal node_cnt
        idx = node_cnt
        node_cnt += 1
        C[idx] = col
        row_id[idx] = rid
        # vertical links
        U[idx] = U[col]
        D[idx] = col
        D[U[col]] = idx
        U[col] = idx
        S[col] += 1
        return idx

    # add rows
    for rid, (x, y, z) in enumerate(triples, 1):
        first = None
        for col in (x, k + y, 2 * k + z):
            nd = add_node(col + 1, rid)   # columns are 1-indexed in DLX
            if first is None:
                first = nd
            else:
                # horizontal links
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd

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

    sys.setrecursionlimit(10000)

    def search(k_depth):
        if R[0] == 0:  # all columns covered
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
            solution_rows.append(row_id[r])
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
            solution_rows.pop()
            r = D[r]
        uncover(c)
        return False

    possible = search(0)

    out = []
    if possible:
        out.append("YES")
        # retrieve triples for selected rows
        selected = [triples[rid - 1] for rid in solution_rows]
        for x, y, z in selected:
            out.append(f"{x+1} {y+1} {z+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()