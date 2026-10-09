import sys

sys.setrecursionlimit(10000)

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

    # columns: 0..k-1 -> X, k..2k-1 -> Y, 2k..3k-1 -> Z
    col_cnt = 3 * k

    # dancing links arrays (0 is the master header)
    U = [0]   # up
    D = [0]   # down
    L = [0]   # left
    R = [0]   # right
    C = [0]   # column of node
    S = [0] * (col_cnt + 1)   # size of each column, index 0 unused

    # create column header nodes (1 .. col_cnt)
    for i in range(col_cnt):
        node = i + 1
        U.append(node)
        D.append(node)
        L.append(node - 1 if i > 0 else 0)
        R.append(node + 1 if i < col_cnt - 1 else 0)
        C.append(i + 1)   # column header points to itself (not used)
    # fix links of master header (0)
    L[0] = col_cnt
    R[0] = 1
    L[1] = 0
    R[col_cnt] = 0

    # store for each row the index of its first node (to retrieve later)
    row_first_node = []
    # mapping from node index to row index
    node_to_row = []

    # add rows
    for idx, (x, y, z) in enumerate(triples):
        cols = [x + 1, k + y + 1, 2 * k + z + 1]   # column numbers (1‑based)
        first = None
        prev = None
        for col in cols:
            node = len(U)
            U.append(U[col])
            D.append(col)
            L.append(0)
            R.append(0)
            C.append(col)
            # vertical links
            D[U[col]] = node
            U[col] = node
            S[col] += 1

            if first is None:
                first = node
            if prev is not None:
                # horizontal links
                R[prev] = node
                L[node] = prev
            prev = node
            node_to_row.append(idx)
        # close the row circle
        R[prev] = first
        L[first] = prev
        row_first_node.append(first)

    answer_rows = []
    solved = False

    def cover(col):
        # remove column header
        R[L[col]] = R[col]
        L[R[col]] = L[col]
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
        R[L[col]] = col
        L[R[col]] = col

    def search():
        nonlocal solved
        if R[0] == 0:          # all columns covered
            solved = True
            return True
        # choose column with minimal size
        c = R[0]
        min_s = S[c]
        col = c
        j = R[c]
        while j != 0:
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
            answer_rows.append(node_to_row[r])
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
        out = ["YES"]
        for row_idx in answer_rows:
            x, y, z = triples[row_idx]
            out.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()