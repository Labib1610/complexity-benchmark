import sys

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

    C = 3 * k                     # number of columns
    max_nodes = 1 + C + 3 * t + 5

    # dancing links arrays
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    col = [0] * max_nodes
    row_id = [0] * max_nodes
    S = [0] * (C + 1)             # column sizes, 1‑based

    # header = 0, column headers 1..C
    for i in range(C + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = C
    R[C] = 0

    node_cnt = C + 1              # next free index

    # add rows
    for idx, (x, y, z) in enumerate(triples):
        cols = [x + 1, k + y + 1, 2 * k + z + 1]   # 1‑based column numbers
        first = -1
        for c in cols:
            nd = node_cnt
            node_cnt += 1
            col[nd] = c
            row_id[nd] = idx

            # vertical link
            U[nd] = U[c]
            D[nd] = c
            D[U[c]] = nd
            U[c] = nd
            S[c] += 1

            # horizontal link
            if first == -1:
                first = nd
                L[nd] = R[nd] = nd
            else:
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd

    solution_rows = []

    sys.setrecursionlimit(10000)

    def cover(c):
        # remove column header
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        # remove rows
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                S[col[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                S[col[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c

    def choose_column():
        # heuristic: column with smallest S
        c = R[0]
        min_s = S[c]
        cur = R[c]
        while cur != 0:
            if S[cur] < min_s:
                min_s = S[cur]
                c = cur
                if min_s == 0:
                    break
            cur = R[cur]
        return c

    found = False

    def search():
        nonlocal found
        if R[0] == 0:          # all columns covered
            found = True
            return True
        c = choose_column()
        if S[c] == 0:          # dead end
            return False
        cover(c)
        r = D[c]
        while r != c:
            solution_rows.append(row_id[r])
            j = R[r]
            while j != r:
                cover(col[j])
                j = R[j]
            if search():
                return True
            # backtrack
            j = L[r]
            while j != r:
                uncover(col[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(c)
        return False

    if search():
        out = ["YES"]
        for idx in solution_rows:
            x, y, z = triples[idx]
            out.append(f"{x+1} {y+1} {z+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()