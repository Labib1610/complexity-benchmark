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
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))

    # columns: 0..k-1 bases, k..2k-1 catalysts, 2k..3k-1 thermals
    C = 3 * k                     # number of columns
    max_nodes = 3 * t + C + 1     # header + column heads + all nodes

    # dancing links arrays
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    Ccol = [0] * max_nodes        # column of a node
    S = [0] * (C + 1)             # column sizes, 1‑based for columns
    row_of_node = [0] * max_nodes # which row a node belongs to

    header = 0
    # initialise header list of column heads (1‑based indices for columns)
    for i in range(C + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = C
    R[C] = 0

    node_id = C + 1               # next free node index
    row_id = 0

    # add rows
    for (x, y, z) in triples:
        cols = [x + 1, k + y + 1, 2 * k + z + 1]   # columns are 1‑based
        first = -1
        row_id += 1
        for col in cols:
            nid = node_id
            node_id += 1
            Ccol[nid] = col
            row_of_node[nid] = row_id

            # vertical links
            U[nid] = U[col]
            D[nid] = col
            D[U[col]] = nid
            U[col] = nid
            S[col] += 1

            # horizontal links
            if first == -1:
                first = nid
                L[nid] = R[nid] = nid
            else:
                L[nid] = L[first]
                R[nid] = first
                R[L[first]] = nid
                L[first] = nid

    solution_rows = []

    # ----- DLX core operations -----
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
                S[Ccol[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                S[Ccol[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[col]] = col
        R[L[col]] = col

    # ----- recursive search -----
    def search():
        if R[header] == header:          # all columns covered
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
            solution_rows.append(row_of_node[r])
            j = R[r]
            while j != r:
                cover(Ccol[j])
                j = R[j]
            if search():
                return True
            # backtrack
            j = L[r]
            while j != r:
                uncover(Ccol[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(col)
        return False

    possible = search()

    out = []
    if possible:
        out.append("YES")
        # map row id back to triple
        row_to_trip = {}
        for idx, tr in enumerate(triples, start=1):
            row_to_trip[idx] = tr
        for rid in solution_rows:
            x, y, z = row_to_trip[rid]
            out.append(f"{x+1} {y+1} {z+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()