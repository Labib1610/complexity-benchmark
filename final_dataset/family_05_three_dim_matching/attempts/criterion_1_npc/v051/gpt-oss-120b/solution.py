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

    n_cols = 3 * k  # linguist 0..k-1, manuscript k..2k-1, algorithm 2k..3k-1

    # Build DLX structures
    max_nodes = t * 3 + n_cols + 1
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes  # column header for each node
    S = [0] * (n_cols + 1)  # column sizes, header 0 is root

    # header node 0 is root
    for i in range(n_cols + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n_cols
    R[n_cols] = 0

    node_cnt = n_cols + 1

    # add rows
    row_id = []  # store triple index for each row's first node
    for idx, (x, y, z) in enumerate(triples):
        cols = [x, k + y, 2 * k + z]  # column numbers (1..n_cols)
        first = None
        for col in cols:
            col += 1  # shift to 1..n_cols for DLX
            node = node_cnt
            node_cnt += 1
            C[node] = col
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
        row_id.append(idx)

    solution = []
    answer = []

    sys.setrecursionlimit(10000)

    def cover(col):
        # remove column header
        L[R[col]] = L[col]
        R[L[col]] = R[col]
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

    def search():
        if R[0] == 0:  # all columns covered
            return True
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
            return False
        cover(c)
        r = D[c]
        while r != c:
            solution.append(r)
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            if search():
                return True
            # backtrack
            solution.pop()
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            r = D[r]
        uncover(c)
        return False

    if search():
        # reconstruct triples from solution nodes
        used_rows = set()
        for node in solution:
            # any node in the row gives the row index
            # walk left to find the first node of the row (could be itself)
            start = node
            while L[start] != start:
                start = L[start]
            # find row index by matching node to stored rows
            # we stored rows sequentially; we can map first node of each row to its index
            # Build a map from first node to row idx
        # Build map
        row_map = {}
        node_ptr = n_cols + 1
        for idx in range(len(triples)):
            # each row has 3 nodes
            first_node = node_ptr
            row_map[first_node] = idx
            node_ptr += 3
        result = []
        for node in solution:
            # find the first node of its row
            start = node
            while L[start] != start:
                start = L[start]
            result.append(triples[row_map[start]])
        print("YES")
        out = sys.stdout
        for x, y, z in result:
            out.write(f"{x+1} {y+1} {z+1}\n")
    else:
        print("NO")

if __name__ == "__main__":
    solve()