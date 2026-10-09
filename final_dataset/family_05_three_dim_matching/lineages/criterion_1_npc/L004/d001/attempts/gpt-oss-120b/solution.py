import sys

sys.setrecursionlimit(1000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # column ids: 0..3k-1  (A0..A(k-1), B0..B(k-1), C0..C(k-1))
    ncol = 3 * k
    rows = []          # each row: (x,y,z) and list of column ids
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        cols = [x, k + y, 2 * k + z]
        rows.append(((x, y, z), cols))

    # ---------- DLX construction ----------
    max_nodes = len(rows) * 3 + ncol + 5
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes          # column of node
    S = [0] * (ncol + 1)         # size of column, column 0 is header

    header = 0
    # header linked list of column headers 1..ncol
    for i in range(ncol + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    R[ncol] = header
    L[header] = ncol
    R[header] = 1
    L[1] = header

    node_id = ncol + 1
    row_node_ids = []   # first node id of each row (for answer retrieval)

    for (triple, cols) in rows:
        first = -1
        for col in cols:
            col_id = col + 1          # shift: column headers are 1..ncol
            nid = node_id
            node_id += 1
            C[nid] = col_id
            # vertical links
            U[nid] = U[col_id]
            D[nid] = col_id
            D[U[col_id]] = nid
            U[col_id] = nid
            S[col_id] += 1
            # horizontal links
            if first == -1:
                first = nid
                L[nid] = R[nid] = nid
            else:
                L[nid] = L[first]
                R[nid] = first
                R[L[first]] = nid
                L[first] = nid
        row_node_ids.append(first)

    answer_rows = []
    solution = []

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

    found = False

    def search():
        nonlocal found
        if R[header] == header:
            # all columns covered
            found = True
            return True
        # choose column with minimal S
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
            answer_rows.append(r)
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
            answer_rows.pop()
            r = D[r]
        uncover(col)
        return False

    if search():
        # retrieve triples from selected rows
        out = []
        for node in answer_rows:
            # node belongs to a row; find its row index
            # we stored rows in order, each row's first node id is in row_node_ids
            # map node -> row index via a dict
            pass
        # Build mapping from any node id to its row index
        node_to_row = {}
        for idx, first in enumerate(row_node_ids):
            cur = first
            while True:
                node_to_row[cur] = idx
                cur = R[cur]
                if cur == first:
                    break
        triples = []
        for node in answer_rows:
            triples.append(rows[node_to_row[node]][0])
        # output
        out_lines = ["YES"]
        for (x, y, z) in triples:
            out_lines.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()