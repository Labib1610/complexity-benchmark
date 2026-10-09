import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    ncol = 3 * q                     # number of columns
    rows = []                        # list of triples (as tuple of ints)
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        rows.append((a, b, c))

    # ---------- DLX construction ----------
    max_nodes = t * 3 + ncol + 1      # +1 for header
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes               # column of node
    S = [0] * (ncol + 1)              # size of each column (1‑based)
    row_of_node = [0] * max_nodes

    head = 0
    # header links columns 1..ncol
    for i in range(ncol + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol + 1               # next free index

    for r_id, (a, b, c) in enumerate(rows, 1):
        cols = [a + 1, b + 1, c + 1]   # make columns 1‑based
        first = -1
        for col in cols:
            idx = node_cnt
            node_cnt += 1
            C[idx] = col
            row_of_node[idx] = r_id

            # vertical link into column
            U[idx] = U[col]
            D[idx] = col
            D[U[col]] = idx
            U[col] = idx
            S[col] += 1

            # horizontal link within the row
            if first == -1:
                first = idx
                L[idx] = R[idx] = idx
            else:
                L[idx] = L[first]
                R[idx] = first
                R[L[first]] = idx
                L[first] = idx

    # ---------- DLX operations ----------
    def cover(col: int) -> None:
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

    def uncover(col: int) -> None:
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

    answer_rows = []

    def search(k: int) -> bool:
        if R[head] == head:          # all columns covered
            return True
        # choose column with minimal size
        c = R[head]
        min_s = S[c]
        col = c
        j = R[c]
        while j != head:
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
            answer_rows.append(row_of_node[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            if search(k + 1):
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

    possible = search(0)

    out = []
    if possible:
        out.append("YES")
        # rows are stored by their original 1‑based id, retrieve triples
        for rid in answer_rows:
            a, b, c = rows[rid - 1]
            out.append(f"{a+1} {b+1} {c+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()