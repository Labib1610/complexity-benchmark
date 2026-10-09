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
        y = int(next(it)) - 1 + k
        z = int(next(it)) - 1 + 2 * k
        triples.append((x, y, z))

    n_cols = 3 * k

    # Dancing Links structures
    max_nodes = t * 3 + n_cols + 1
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes  # column header for each node
    S = [0] * (n_cols + 1)  # column sizes, header 0 is root

    # header nodes: 0 is root, 1..n_cols are column headers
    for i in range(n_cols + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n_cols
    R[n_cols] = 0

    node_id = n_cols + 1

    # add rows
    for row_idx, (a, b, c) in enumerate(triples):
        first = None
        for col in (a, b, c):
            nid = node_id
            node_id += 1
            C[nid] = col + 1  # column header index (1‑based)
            # vertical links
            U[nid] = U[col + 1]
            D[nid] = col + 1
            D[U[col + 1]] = nid
            U[col + 1] = nid
            S[col + 1] += 1
            # horizontal links
            if first is None:
                first = nid
                L[nid] = R[nid] = nid
            else:
                L[nid] = L[first]
                R[nid] = first
                R[L[first]] = nid
                L[first] = nid

    solution = []
    answer = []

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

    sys.setrecursionlimit(10000)

    def search():
        if R[0] == 0:  # all columns covered
            answer.extend(solution)
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
        # reconstruct triples from node ids in answer
        used = set()
        out = []
        for node in answer:
            # each node belongs to a row; collect its three columns
            cols = []
            cur = node
            while True:
                col = C[cur] - 1
                cols.append(col)
                cur = R[cur]
                if cur == node:
                    break
            # map back to (x,y,z)
            a, b, c = sorted(cols)  # order not important
            # convert to original indices
            x = a + 1
            y = b - k + 1
            z = c - 2 * k + 1
            out.append((x, y, z))
        print("YES")
        for triple in out:
            print(*triple)
    else:
        print("NO")

if __name__ == "__main__":
    solve()