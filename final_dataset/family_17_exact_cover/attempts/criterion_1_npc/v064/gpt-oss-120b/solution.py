import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q                     # number of columns (vertices)

    rows = []                     # list of triples (0‑based)
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        rows.append((a, b, c))

    # ---------- DLX construction ----------
    max_nodes = 3 * t + n + 1      # +1 for header
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes           # column of node
    S = [0] * (n + 1)             # column sizes, 0‑based, column 0 is dummy head
    row_id = [0] * max_nodes      # which input row a node belongs to

    head = 0
    # link column headers (0 is head, 1..n are real columns)
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = n
    R[n] = 0

    node_cnt = n + 1  # next free index

    for rid, (a, b, c) in enumerate(rows):
        first = -1
        for col in (a, b, c):
            col += 1                     # shift because column 0 is dummy
            node = node_cnt
            node_cnt += 1
            C[node] = col
            row_id[node] = rid

            # insert into column (at bottom, before header)
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            S[col] += 1

            # link row horizontally
            if first == -1:
                first = node
                L[node] = R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

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

    solution = []
    answer = None

    def search(k: int) -> None:
        nonlocal answer
        if R[head] == head:          # all columns covered
            answer = solution.copy()
            return
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
            return                     # dead end
        cover(col)
        r = D[col]
        while r != col:
            solution.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            search(k + 1)
            if answer is not None:
                return
            # backtrack
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            solution.pop()
            r = D[r]
        uncover(col)

    search(0)

    out = []
    if answer is None:
        out.append("NO")
    else:
        out.append("YES")
        for rid in answer:
            a, b, c = rows[rid]
            out.append(f"{a+1} {b+1} {c+1}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()