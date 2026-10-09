import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    n_cols = 3 * q

    # Dancing Links structures
    max_nodes = t * 3 + n_cols + 1
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes  # column header for each node
    S = [0] * (n_cols + 1)  # size of column, header 0 is root

    # header nodes: 0 is root, 1..n_cols are column headers
    for i in range(n_cols + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n_cols
    R[n_cols] = 0

    node_cnt = n_cols + 1

    # add rows
    row_nodes = []  # store first node index of each row for solution retrieval
    for r, (a, b, c) in enumerate(triples):
        first = -1
        for col in (a, b, c):
            col += 1  # shift to header index
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
            if first == -1:
                first = node
                L[node] = R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node
        row_nodes.append(first)

    solution = []
    answer_rows = []

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

    def search(k):
        if R[0] == 0:
            # all columns covered
            answer_rows.extend(solution)
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
            if search(k + 1):
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

    if search(0):
        sys.stdout.write("YES\n")
        # retrieve triples from row nodes
        used = set()
        for node in answer_rows:
            # find the row index
            # each row's first node is stored in row_nodes list order
            # we can map node to row by scanning row_nodes
            # build a dict first
            pass
    else:
        sys.stdout.write("NO\n")
        return

    # Build mapping from any node to its row index
    node_to_row = {}
    for idx, first in enumerate(row_nodes):
        if first == -1:
            continue
        cur = first
        while True:
            node_to_row[cur] = idx
            cur = R[cur]
            if cur == first:
                break

    selected = []
    for node in answer_rows:
        selected.append(triples[node_to_row[node]])

    for a, b, c in selected:
        sys.stdout.write(f"{a+1} {b+1} {c+1}\n")

if __name__ == "__main__":
    solve()