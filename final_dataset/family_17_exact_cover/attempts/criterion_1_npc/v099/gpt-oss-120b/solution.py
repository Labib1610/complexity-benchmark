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
    # DLX structures
    max_nodes = 3 * t + ncol + 5
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes              # column of node
    row_id = [0] * max_nodes         # which triple (index) the node belongs to
    S = [0] * (ncol + 1)             # size of each column

    header = 0
    # create column headers 1..ncol
    for i in range(ncol + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol
    # add rows
    for idx, (a, b, c) in enumerate(triples, 1):
        first = 0
        for col in (a, b, c):
            node_cnt += 1
            col_head = col
            # vertical links
            U[node_cnt] = U[col_head]
            D[node_cnt] = col_head
            D[U[col_head]] = node_cnt
            U[col_head] = node_cnt
            C[node_cnt] = col_head
            row_id[node_cnt] = idx
            S[col_head] += 1
            # horizontal links
            if first == 0:
                L[node_cnt] = R[node_cnt] = node_cnt
                first = node_cnt
            else:
                L[node_cnt] = L[first]
                R[node_cnt] = first
                R[L[first]] = node_cnt
                L[first] = node_cnt

    solution = []

    def cover(col):
        # remove column header
        R[L[col]] = R[col]
        L[R[col]] = L[col]
        # remove rows
        i = D[col]
        while i != col:
            j = R[i]
            while j != i:
                D[U[j]] = D[j]
                U[D[j]] = U[j]
                S[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                S[C[j]] += 1
                D[U[j]] = j
                U[D[j]] = j
                j = L[j]
            i = U[i]
        R[L[col]] = col
        L[R[col]] = col

    found = False

    def search(k):
        nonlocal found
        if R[header] == header:   # all columns covered
            found = True
            return True
        # choose column with minimal size
        c = R[header]
        min_s = S[c]
        col = c
        j = R[c]
        while j != header:
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
            solution.append(row_id[r])
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
            solution.pop()
            r = D[r]
        uncover(col)
        return False

    if search(0):
        out = ["YES"]
        # solution contains indices of triples, need to output the triples themselves
        for idx in solution:
            a, b, c = triples[idx - 1]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()