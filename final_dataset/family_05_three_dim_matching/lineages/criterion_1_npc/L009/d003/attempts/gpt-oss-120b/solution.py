import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # column indices
    # 0..k-1          inputs
    # k..2k-1         encryptors
    # 2k..3k-1        outputs
    ncol = 3 * k

    rows = []          # each element: (cols list, original triple)
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        cols = [x, k + y, 2 * k + z]
        rows.append((cols, (x + 1, y + 1, z + 1)))

    # ---------- Dancing Links structures ----------
    # node 0 is the header
    max_nodes = 1 + ncol + 3 * len(rows) + 5
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes          # column of node
    S = [0] * (ncol + 1)         # size of column, column headers are 1..ncol
    row_id = [0] * max_nodes     # which input row a node belongs to

    # header links columns in a doubly linked list
    header = 0
    for i in range(ncol + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol + 1          # next free index

    # add rows
    for rid, (cols, triple) in enumerate(rows):
        first = -1
        for col in cols:
            col_hdr = col + 1      # column headers are 1‑based
            nd = node_cnt
            node_cnt += 1

            C[nd] = col_hdr
            row_id[nd] = rid

            # vertical links (insert at bottom of column)
            U[nd] = U[col_hdr]
            D[nd] = col_hdr
            D[U[col_hdr]] = nd
            U[col_hdr] = nd
            S[col_hdr] += 1

            # horizontal links within the row
            if first == -1:
                first = nd
                L[nd] = R[nd] = nd
            else:
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
        uncover(col)
        return False

    ok = search()
    if not ok:
        print("NO")
        return
    # solution_rows contains indices of selected rows (may have duplicates because each row has 3 nodes)
    # we need unique rows, they are stored three times each; deduplicate preserving order
    seen = set()
    final = []
    for rid in solution_rows:
        if rid not in seen:
            seen.add(rid)
            final.append(rows[rid][1])
    # final must have k triples
    print("YES")
    for triple in final:
        print(*triple)

if __name__ == "__main__":
    solve()