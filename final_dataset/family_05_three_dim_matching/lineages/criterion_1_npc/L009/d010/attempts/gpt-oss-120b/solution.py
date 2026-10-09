import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    triples = []                     # (x,y,z)
    for _ in range(t):
        x = int(next(it)) - 1        # 0‑based
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        triples.append((x, y, z))

    # ---------- dancing links ----------
    C = 3 * k                        # number of columns
    max_nodes = 1 + C + 3 * t + 5    # root + column headers + each 1 in matrix

    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    col = [0] * max_nodes            # column of a node
    row_of_node = [0] * max_nodes    # which triple the node belongs to
    size = [0] * (C + 1)             # size of each column, indexed by header id (1..C)

    # root is 0
    for i in range(C + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = C
    R[C] = 0

    node_cnt = C + 1                 # next free node index

    # add rows
    for idx, (x, y, z) in enumerate(triples):
        cols = [x, k + y, 2 * k + z]     # column numbers 0..C-1
        first = -1
        for c in cols:
            header = c + 1                # column header id
            nid = node_cnt
            node_cnt += 1
            col[nid] = header
            row_of_node[nid] = idx

            # insert vertically just before header (i.e. at the bottom)
            U[nid] = U[header]
            D[nid] = header
            D[U[header]] = nid
            U[header] = nid
            size[header] += 1

            # link horizontally
            if first == -1:
                first = nid
                L[nid] = R[nid] = nid
            else:
                # insert to the left of first (circular list)
                L[nid] = L[first]
                R[nid] = first
                R[L[first]] = nid
                L[first] = nid

    # ---------- algorithm X ----------
    solution_rows = []          # list of triple indices forming the solution
    found = False

    def cover(c):
        # remove column header c
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        # remove rows
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                size[col[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[col[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c

    def choose_column():
        # heuristic: column with smallest size (>0)
        c = R[0]
        best = c
        min_sz = size[c]
        while c != 0:
            if size[c] < min_sz:
                min_sz = size[c]
                best = c
                if min_sz == 0:
                    break
            c = R[c]
        return best

    def search():
        nonlocal found
        if R[0] == 0:               # all columns covered
            found = True
            return True
        c = choose_column()
        if size[c] == 0:
            return False
        cover(c)
        r = D[c]
        while r != c:
            solution_rows.append(row_of_node[r])
            j = R[r]
            while j != r:
                cover(col[j])
                j = R[j]
            if search():
                return True
            # backtrack
            j = L[r]
            while j != r:
                uncover(col[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(c)
        return False

    if search():
        out = ['YES']
        for idx in solution_rows:
            x, y, z = triples[idx]
            out.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()