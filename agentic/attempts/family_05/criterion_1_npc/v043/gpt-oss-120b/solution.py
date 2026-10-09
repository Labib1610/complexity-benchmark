import sys

sys.setrecursionlimit(1000000)

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

    # Exact cover with dancing links
    n_items = 3 * k  # A0..A{k-1}, B0..B{k-1}, C0..C{k-1}
    # column header nodes 0..n_items-1
    # build linked structure
    size = [0] * n_items
    col_head = list(range(n_items))

    # node arrays
    L = []
    R = []
    U = []
    D = []
    C = []  # column of node
    row_id = []  # which row this node belongs to

    # create column header nodes (they act as circular lists)
    for i in range(n_items):
        L.append(i - 1 if i else n_items - 1)
        R.append(i + 1 if i + 1 < n_items else 0)
        U.append(i)
        D.append(i)
        C.append(i)
        row_id.append(-1)

    header = n_items  # special header node
    L.append(n_items - 1)
    R.append(0)
    U.append(header)
    D.append(header)
    C.append(-1)
    row_id.append(-1)

    # link header into column list
    L[0] = header
    R[header] = 0

    node_cnt = n_items + 1

    def add_node(col):
        nonlocal node_cnt
        idx = node_cnt
        node_cnt += 1
        # vertical insertion at bottom of column
        U.append(U[col])
        D.append(col)
        C.append(col)
        row_id.append(-1)
        L.append(-1)
        R.append(-1)

        # fix vertical links
        D[U[col]] = idx
        U[col] = idx
        size[col] += 1
        return idx

    # add rows
    for rid, (a, b, c) in enumerate(rows):
        cols = [a, k + b, 2 * k + c]
        first = -1
        prev = -1
        for col in cols:
            nd = add_node(col)
            row_id[nd] = rid
            if first == -1:
                first = nd
            if prev != -1:
                R[prev] = nd
                L[nd] = prev
            prev = nd
        # close the row circularly
        R[prev] = first
        L[first] = prev

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
                size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                size[C[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[col]] = col
        R[L[col]] = col

    def search(k_depth):
        if R[header] == header:  # all columns covered
            return True
        # choose column with minimal size
        c = R[header]
        min_sz = size[c]
        col = c
        j = R[c]
        while j != header:
            if size[j] < min_sz:
                min_sz = size[j]
                col = j
                if min_sz == 0:
                    break
            j = R[j]
        if min_sz == 0:
            return False
        cover(col)
        r = D[col]
        while r != col:
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
        uncover(col)
        return False

    possible = search(0)
    out = []
    if possible and len(solution) == k:
        out.append("YES")
        for rid in solution:
            a, b, c = rows[rid]
            out.append(f"{a+1} {b+1} {c+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()