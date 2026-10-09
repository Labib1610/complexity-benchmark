import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # columns: 0..k-1 operators, k..2k-1 hardware, 2k..3k-1 phases
    ncol = 3 * k

    # dancing links structures
    # header node is 0, column headers are 1..ncol
    size = ncol + 1                     # total nodes for headers
    U = [0] * (1 + 3 * t + ncol + 5)    # enough space
    D = [0] * (1 + 3 * t + ncol + 5)
    L = [0] * (1 + 3 * t + ncol + 5)
    R = [0] * (1 + 3 * t + ncol + 5)
    C = [0] * (1 + 3 * t + ncol + 5)    # column of each node
    col_size = [0] * (ncol + 1)         # size of each column

    # initialise header list (circular)
    for i in range(ncol + 1):
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    # initialise column headers vertical links to themselves
    for i in range(1, ncol + 1):
        U[i] = D[i] = i

    node_cnt = ncol + 1                 # next free index
    row_of_node = []                    # to retrieve triple later
    triples = []                        # store triples per row index

    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        cols = [x + 1, k + y + 1, 2 * k + z + 1]   # column numbers (1‑based)
        triples.append((x + 1, y + 1, z + 1))
        first = None
        for col in cols:
            node = node_cnt
            node_cnt += 1
            C[node] = col
            # insert node at bottom of column col
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            col_size[col] += 1

            if first is None:
                first = node
                L[node] = R[node] = node
            else:
                # link into the row circular list
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node
        row_of_node.append(first)   # store one node of the row

    solution_rows = []

    # ----- dancing‑links operations -----
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
                col_size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                col_size[C[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[col]] = col
        R[L[col]] = col

    # ----- recursive search -----
    def search():
        if R[0] == 0:          # all columns covered
            return True
        # choose column with minimal size
        c = R[0]
        min_sz = col_size[c]
        j = R[c]
        while j != 0:
            if col_size[j] < min_sz:
                c = j
                min_sz = col_size[j]
                if min_sz == 0:
                    break
            j = R[j]
        if min_sz == 0:
            return False

        cover(c)
        r = D[c]
        while r != c:
            solution_rows.append(r)
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

    found = search()
    out = []
    if found:
        out.append("YES")
        for node in solution_rows:
            # retrieve the row index (its first node is stored)
            # we stored rows in order, so we can map node -> row index
            # row_of_node list aligns with triples order
            # find index where row_of_node[idx] == node (or any node in same row)
            # easier: store mapping node->row index while building
            pass
    else:
        out.append("NO")
        sys.stdout.write("\n".join(out))
        return

    # Build mapping from any node to its row index
    node_to_row = {}
    for idx, first_node in enumerate(row_of_node):
        # walk the row circular list and map each node
        cur = first_node
        while True:
            node_to_row[cur] = idx
            cur = R[cur]
            if cur == first_node:
                break

    for node in solution_rows:
        row_idx = node_to_row[node]
        out.append("{} {} {}".format(*triples[row_idx]))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()