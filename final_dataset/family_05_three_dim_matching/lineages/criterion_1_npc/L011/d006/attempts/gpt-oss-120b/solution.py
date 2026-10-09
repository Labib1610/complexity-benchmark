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

    if t < k:
        print("NO")
        return

    # ---------- DLX construction ----------
    num_cols = 3 * k                     # column id 1 .. num_cols
    max_nodes = t * 3 + num_cols + 5    # enough space

    # linked‑list structures
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes          # column of a node
    S = [0] * (num_cols + 1)     # column sizes, index 0 unused
    row_of_node = [0] * max_nodes

    # header 0, column headers 1..num_cols
    for i in range(num_cols + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = num_cols
    R[num_cols] = 0

    node_ptr = num_cols + 1        # next free node index
    row_to_triple = []             # row id -> (x,y,z)

    for (x, y, z) in triples:
        cols = [x + 1,                # frequency columns are 1..k
                k + y + 1,            # modulation columns are k+1 .. 2k
                2 * k + z + 1]        # key columns are 2k+1 .. 3k
        first = -1
        row_id = len(row_to_triple)
        row_to_triple.append((x + 1, y + 1, z + 1))
        for col in cols:
            idx = node_ptr
            node_ptr += 1
            C[idx] = col
            row_of_node[idx] = row_id

            # vertical insertion (above column header)
            U[idx] = U[col]
            D[idx] = col
            D[U[col]] = idx
            U[col] = idx
            S[col] += 1

            # horizontal linking within the row
            if first == -1:
                first = idx
                L[idx] = R[idx] = idx
            else:
                L[idx] = L[first]
                R[idx] = first
                R[L[first]] = idx
                L[first] = idx

    # ---------- DLX algorithm ----------
    solution_rows = []

    def cover(c: int) -> None:
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

    def uncover(c: int) -> None:
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

    def search() -> bool:
        if R[0] == 0:          # all columns covered
            return True
        # choose column with minimum size
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
            if search():
                return True
            # backtrack
            solution_rows.pop()
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            r = D[r]
        uncover(c)
        return False

    possible = search()
    if not possible:
        print("NO")
        return

    print("YES")
    out = sys.stdout
    for row_id in solution_rows:
        x, y, z = row_to_triple[row_id]
        out.write(f"{x} {y} {z}\n")

if __name__ == "__main__":
    solve()