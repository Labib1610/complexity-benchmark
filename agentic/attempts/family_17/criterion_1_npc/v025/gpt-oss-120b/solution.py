import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        triples.append((a, b, c))

    ncol = 3 * q                     # columns are 1..ncol
    max_nodes = 3 * t + ncol + 5

    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes
    S = [0] * (ncol + 1)             # column sizes, 1‑based
    H = [-1] * t                     # first node of each row

    # header node 0, columns 1..ncol linked in a circular list
    for i in range(ncol + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol
    for r, (a, b, c) in enumerate(triples):
        first = -1
        for col in (a, b, c):
            node_cnt += 1
            C[node_cnt] = col
            # insert node at bottom of column col
            U[node_cnt] = U[col]
            D[node_cnt] = col
            D[U[col]] = node_cnt
            U[col] = node_cnt
            S[col] += 1

            if first == -1:
                first = node_cnt
                L[node_cnt] = R[node_cnt] = node_cnt
            else:
                # insert to the right of first (circular)
                L[node_cnt] = L[first]
                R[node_cnt] = first
                R[L[first]] = node_cnt
                L[first] = node_cnt
        H[r] = first

    answer_rows = [0] * (q + 1)
    found = False

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

    def search(k: int) -> bool:
        nonlocal found
        if R[0] == 0:          # all columns covered
            # k must be q automatically
            found = True
            return True
        # choose column with minimal size
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
            answer_rows[k] = r
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
            r = D[r]
        uncover(c)
        return False

    if search(0):
        out = ["YES"]
        for i in range(q):
            row_node = answer_rows[i]
            # collect the three columns of this row
            cols = []
            j = row_node
            while True:
                cols.append(C[j])
                j = R[j]
                if j == row_node:
                    break
            out.append(f"{cols[0]} {cols[1]} {cols[2]}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()