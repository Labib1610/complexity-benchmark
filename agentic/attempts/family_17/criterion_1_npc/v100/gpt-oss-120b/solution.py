import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q  # number of columns
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    # ---------- DLX structures ----------
    max_nodes = t * 3 + n + 1
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes  # column header for each node
    S = [0] * (n + 1)    # size of each column, header 0 is root
    row_id = [0] * max_nodes

    # header nodes: 0 is root, 1..n are column headers
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_cnt = n + 1

    def add_row(rid, cols):
        nonlocal node_cnt
        first = None
        for col in cols:
            col += 1  # shift to header index
            node = node_cnt
            node_cnt += 1
            C[node] = col
            row_id[node] = rid

            # vertical links
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            S[col] += 1

            # horizontal links
            if first is None:
                first = node
                L[node] = R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

    for idx, (a, b, c) in enumerate(triples):
        add_row(idx, (a, b, c))

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

    found = False

    def search(k):
        nonlocal found
        if R[0] == 0:  # all columns covered
            found = True
            return
        # choose column with minimal size
        c = R[0]
        min_s = S[c]
        j = R[c]
        while j != 0:
            if S[j] < min_s:
                c = j
                min_s = S[j]
                if min_s == 0:
                    break
            j = R[j]
        if min_s == 0:
            return  # dead end

        cover(c)
        r = D[c]
        while r != c:
            solution_rows.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            search(k + 1)
            if found:
                return
            # backtrack
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(c)

    search(0)

    if not found:
        print("NO")
    else:
        print("YES")
        for rid in solution_rows:
            a, b, c = triples[rid]
            print(a + 1, b + 1, c + 1)

if __name__ == "__main__":
    solve()