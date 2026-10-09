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

    # ----- build DLX -----
    cols = 3 * k                     # column count
    max_nodes = 3 * t + cols + 5

    # link arrays
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes               # column of node
    S = [0] * (cols + 1)              # size of column (header at 0..cols-1)

    # header node 0, column headers 1..cols
    for i in range(cols + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = cols
    R[cols] = 0

    node_cnt = cols + 1               # next free index

    row_of_node = [0] * max_nodes    # to retrieve triple index
    row_nodes = []                    # list of node indices per row

    for rid, (x, y, z) in enumerate(triples):
        cols_idx = [x, k + y, 2 * k + z]   # 0‑based column numbers
        first = -1
        nodes_this_row = []
        for col in cols_idx:
            col_id = col + 1                # header index (1‑based)
            node = node_cnt
            node_cnt += 1

            C[node] = col_id
            row_of_node[node] = rid

            # vertical links
            U[node] = U[col_id]
            D[node] = col_id
            D[U[col_id]] = node
            U[col_id] = node

            S[col_id] += 1

            # horizontal links
            if first == -1:
                first = node
                L[node] = R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

            nodes_this_row.append(node)
        row_nodes.append(nodes_this_row)

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

    def search():
        if R[0] == 0:          # all columns covered
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
            solution_rows.append(row_of_node[r])
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

    found = search()
    out = []
    if found:
        out.append("YES")
        for rid in solution_rows:
            x, y, z = triples[rid]
            out.append(f"{x+1} {y+1} {z+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()