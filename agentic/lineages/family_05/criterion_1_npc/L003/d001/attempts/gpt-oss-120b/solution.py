import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # column indices: 0..k-1 actuators, k..2k-1 scanners, 2k..3k-1 processors
    ncol = 3 * k
    # dancing links structures
    # node 0 is the root header
    U = [0]
    D = [0]
    L = [0]
    R = [0]
    C = [0]          # column of node
    size = [0] * ncol   # size of each column
    col_head = []    # header node index for each column

    # create column header nodes (1..ncol)
    for col in range(ncol):
        idx = len(U)
        U.append(idx)   # up points to itself initially
        D.append(idx)
        L.append(idx - 1 if col > 0 else 0)   # linked in header list
        R.append(idx + 1 if col < ncol - 1 else 0)
        C.append(col)
        col_head.append(idx)
        size[col] = 0

    # close the header list circularly
    # root is node 0, its right points to first column header, left to last
    R[0] = col_head[0]
    L[0] = col_head[-1]
    L[col_head[0]] = 0
    R[col_head[-1]] = 0

    # store rows for output later
    rows = []   # each element: (node_index_of_first_node, (x,y,z))

    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        cols = [x, k + y, 2 * k + z]

        first = None
        prev = None
        nodes = []
        for col in cols:
            idx = len(U)
            U.append(0)
            D.append(0)
            L.append(0)
            R.append(0)
            C.append(col)
            # vertical link into column
            head = col_head[col]
            # insert just above head (i.e. at the bottom)
            U[idx] = U[head]
            D[idx] = head
            D[U[head]] = idx
            U[head] = idx
            size[col] += 1

            nodes.append(idx)

        # horizontal links (circular)
        for i in range(3):
            cur = nodes[i]
            left = nodes[(i - 1) % 3]
            right = nodes[(i + 1) % 3]
            L[cur] = left
            R[cur] = right

        rows.append( (nodes[0], (x + 1, y + 1, z + 1)) )

    # ---------- dancing links operations ----------
    def cover(col_head_idx):
        # remove column header
        R[L[col_head_idx]] = R[col_head_idx]
        L[R[col_head_idx]] = L[col_head_idx]
        # for each row i in this column
        i = D[col_head_idx]
        while i != col_head_idx:
            j = R[i]
            while j != i:
                # remove node j from its column
                D[U[j]] = D[j]
                U[D[j]] = U[j]
                size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col_head_idx):
        i = U[col_head_idx]
        while i != col_head_idx:
            j = L[i]
            while j != i:
                size[C[j]] += 1
                D[U[j]] = j
                U[D[j]] = j
                j = L[j]
            i = U[i]
        R[L[col_head_idx]] = col_head_idx
        L[R[col_head_idx]] = col_head_idx

    # map from column header node to column index
    col_of_head = {}
    for col in range(ncol):
        col_of_head[col_head[col]] = col

    answer_nodes = []

    def search():
        if R[0] == 0:          # no columns left
            return True
        # choose column with minimal size
        c = R[0]
        min_sz = size[col_of_head[c]]
        col = c
        j = R[c]
        while j != 0:
            sz = size[col_of_head[j]]
            if sz < min_sz:
                min_sz = sz
                col = j
                if sz == 0:
                    break
            j = R[j]
        if min_sz == 0:
            return False
        cover(col)
        r = D[col]
        while r != col:
            answer_nodes.append(r)
            j = R[r]
            while j != r:
                cover(col_head[C[j]])
                j = R[j]
            if search():
                return True
            # backtrack
            j = L[r]
            while j != r:
                uncover(col_head[C[j]])
                j = L[j]
            answer_nodes.pop()
            r = D[r]
        uncover(col)
        return False

    if search():
        # translate answer_nodes to original triples
        # each node belongs to a row; we stored rows list with a representative node
        node_to_trip = {}
        for rep, trip in rows:
            node_to_trip[rep] = trip
        # build mapping from any node in the row to its trip
        # we can walk the row to find its representative
        used = set()
        output = []
        for node in answer_nodes:
            # find the representative (any node of the same row)
            # walk left until we hit a node that is a key in node_to_trip
            cur = node
            while cur not in node_to_trip:
                cur = L[cur]
            trip = node_to_trip[cur]
            if trip not in used:
                used.add(trip)
                output.append(trip)
        # output
        out_lines = ["YES"]
        out_lines += ["{} {} {}".format(*trip) for trip in output]
        sys.stdout.write("\n".join(out_lines))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()