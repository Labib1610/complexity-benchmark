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

    n = 3 * q                     # number of columns (elements)
    max_nodes = 1 + n + 3 * t + 5

    # arrays for dancing links
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes          # column of node
    S = [0] * (n + 1)            # column sizes

    # header = 0, column headers 1..n
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_cnt = n + 1  # next free index

    row_head = []     # store one node index per row to retrieve later

    for (a, b, c) in triples:
        # create three nodes and link them horizontally
        first = node_cnt
        nodes = []
        for col in (a, b, c):
            idx = node_cnt
            node_cnt += 1
            C[idx] = col
            # vertical insertion at bottom of column list
            U[idx] = U[col]
            D[idx] = col
            D[U[col]] = idx
            U[col] = idx
            S[col] += 1
            nodes.append(idx)
        # link horizontally (circular)
        for i in range(3):
            L[nodes[i]] = nodes[(i - 1) % 3]
            R[nodes[i]] = nodes[(i + 1) % 3]
        row_head.append(first)

    answer = [0] * q
    found = False

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

    def search(k: int) -> bool:
        nonlocal found
        if R[0] == 0:          # no columns left
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
            answer[k] = r
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
        uncover(c)
        return False

    if search(0):
        out = ["YES"]
        for i in range(q):
            # retrieve three elements from the stored row
            row_node = answer[i]
            elems = []
            j = row_node
            while True:
                elems.append(str(C[j]))
                j = R[j]
                if j == row_node:
                    break
            out.append(" ".join(elems))
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()