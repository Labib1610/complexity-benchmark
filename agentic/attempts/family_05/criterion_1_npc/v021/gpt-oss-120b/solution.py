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

    ncol = 3 * k                     # columns: X0..Xk-1, Y0..Yk-1, Z0..Zk-1
    # DLX structures
    max_nodes = 3 * t + ncol + 1     # + header
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes
    S = [0] * (ncol + 1)             # column sizes, 0..ncol-1, header at ncol

    head = ncol                      # index of header node
    # initialise column headers
    for i in range(ncol):
        U[i] = D[i] = i
        L[i] = i - 1 if i > 0 else head
        R[i] = i + 1 if i + 1 < ncol else head
        C[i] = i
    L[head] = ncol - 1
    R[head] = 0
    U[head] = D[head] = head
    C[head] = head

    node_cnt = ncol + 1  # next free index

    row_id_of_node = [0] * max_nodes   # to retrieve original triple
    # add rows
    for rid, (x, y, z) in enumerate(triples):
        cols = [x, k + y, 2 * k + z]
        first = -1
        for col in cols:
            nd = node_cnt
            node_cnt += 1
            C[nd] = col
            row_id_of_node[nd] = rid

            # vertical links
            U[nd] = U[col]
            D[nd] = col
            D[U[col]] = nd
            U[col] = nd
            S[col] += 1

            # horizontal links
            if first == -1:
                L[nd] = R[nd] = nd
                first = nd
            else:
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd

    # if any column has size 0, impossible
    for col in range(ncol):
        if S[col] == 0:
            print("NO")
            return

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

    def search():
        nonlocal found
        if R[head] == head:
            found = True
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
            solution_rows.append(row_id_of_node[r])
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
            solution_rows.pop()
            r = D[r]
        uncover(col)
        return False

    if search():
        print("YES")
        for rid in solution_rows:
            x, y, z = triples[rid]
            print(x + 1, y + 1, z + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()