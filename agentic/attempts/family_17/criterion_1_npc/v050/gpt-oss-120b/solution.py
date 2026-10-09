import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q                     # number of columns
    triples = []                 # store original triples
    rows = []                    # each row: list of column indices (0‑based)

    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a + 1, b + 1, c + 1))
        rows.append([a, b, c])

    # ---------- Dancing Links ----------
    max_nodes = 3 * t + n + 5
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes          # column header of a node
    S = [0] * (n + 1)            # size of each column
    row_id = [0] * max_nodes     # which input row a node belongs to

    header = 0
    # initialise column headers 1..n
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_cnt = n
    # add rows
    for r_idx, cols in enumerate(rows):
        first = None
        for col in cols:
            node_cnt += 1
            col_header = col + 1          # column headers are 1‑based
            C[node_cnt] = col_header
            row_id[node_cnt] = r_idx

            # vertical links
            U[node_cnt] = U[col_header]
            D[node_cnt] = col_header
            D[U[col_header]] = node_cnt
            U[col_header] = node_cnt
            S[col_header] += 1

            # horizontal links
            if first is None:
                first = node_cnt
                L[node_cnt] = R[node_cnt] = node_cnt
            else:
                L[node_cnt] = L[first]
                R[node_cnt] = first
                R[L[first]] = node_cnt
                L[first] = node_cnt

    answer_rows = [0] * q
    solved = False

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

    def choose_column():
        # heuristic: column with minimal size
        c = R[header]
        min_s = 10**9
        best = c
        while c != header:
            if S[c] < min_s:
                min_s = S[c]
                best = c
                if min_s == 0:
                    break
            c = R[c]
        return best

    def search(k):
        nonlocal solved
        if R[header] == header:          # all columns covered
            solved = True
            return True
        col = choose_column()
        if S[col] == 0:
            return False
        cover(col)
        r = D[col]
        while r != col:
            answer_rows[k] = row_id[r]
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
        uncover(col)
        return False

    if search(0):
        out = ["YES"]
        for idx in answer_rows[:q]:
            a, b, c = triples[idx]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()