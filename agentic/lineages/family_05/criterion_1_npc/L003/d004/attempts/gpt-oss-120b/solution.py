import sys

sys.setrecursionlimit(1000000)

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

    # columns: 0..k-1 foundations, k..2k-1 columns, 2k..3k-1 capitals
    C = 3 * k
    # DLX structures
    max_nodes = C + 3 * t + 5
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    Ccol = [0] * max_nodes   # column of a node
    S = [0] * C               # size of each column
    row_id = [0] * max_nodes  # which input row a node belongs to

    # header node 0, column headers 1..C
    header = 0
    for i in range(C + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    R[C] = header
    L[header] = C

    node_cnt = C + 1  # next free index

    # add rows
    for idx, (x, y, z) in enumerate(triples):
        cols = [x, k + y, 2 * k + z]
        first = -1
        for col in cols:
            col_header = col + 1          # shift by 1 because header is 0
            node = node_cnt
            node_cnt += 1
            Ccol[node] = col_header
            row_id[node] = idx

            # vertical links
            U[node] = U[col_header]
            D[node] = col_header
            D[U[col_header]] = node
            U[col_header] = node
            S[col] += 1

            # horizontal links
            if first == -1:
                first = node
                L[node] = R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

    solution_rows = []

    def cover(col):
        # remove column header
        R[L[col]] = R[col]
        L[R[col]] = L[col]
        i = D[col]
        while i != col:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                S[Ccol[j] - 1] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                S[Ccol[j] - 1] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        R[L[col]] = col
        L[R[col]] = col

    def choose_column():
        # heuristic: column with minimal S
        c = R[header]
        min_s = 10**9
        chosen = -1
        while c != header:
            col_idx = c - 1
            if S[col_idx] < min_s:
                min_s = S[col_idx]
                chosen = c
                if min_s == 0:
                    break
            c = R[c]
        return chosen

    def search():
        if R[header] == header:
            return True
        col = choose_column()
        if col == -1 or S[col - 1] == 0:
            return False
        cover(col)
        r = D[col]
        while r != col:
            solution_rows.append(row_id[r])
            j = R[r]
            while j != r:
                cover(Ccol[j])
                j = R[j]
            if search():
                return True
            # backtrack
            j = L[r]
            while j != r:
                uncover(Ccol[j])
                j = L[j]
            solution_rows.pop()
            r = D[r]
        uncover(col)
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