import sys
sys.setrecursionlimit(10000000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q

    # DLX structures
    max_nodes = t * 3 + n + 1
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes          # column header for each node
    S = [0] * (n + 1)            # size of each column
    row_id = [0] * max_nodes     # which triple (index) this node belongs to

    # header is 0
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_cnt = n + 1

    triples = []
    for idx in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        triples.append((a, b, c))
        first = -1
        for col in (a, b, c):
            node = node_cnt
            node_cnt += 1
            C[node] = col
            row_id[node] = idx
            # vertical links
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            S[col] += 1
            # horizontal links
            if first == -1:
                L[node] = R[node] = node
                first = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

    solution = []
    found = False

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

    def heuristic():
        # simple lower bound: remaining columns / 3
        cnt = 0
        c = R[0]
        while c != 0:
            cnt += 1
            c = R[c]
        return (cnt + 2) // 3

    def dfs(k):
        nonlocal found
        if found:
            return
        if R[0] == 0:  # all columns covered
            found = True
            return
        # prune by lower bound
        if k + heuristic() > q:
            return
        # choose column with minimal size
        c = R[0]
        min_s = S[c]
        col = c
        while c != 0:
            if S[c] < min_s:
                min_s = S[c]
                col = c
                if min_s == 0:
                    break
            c = R[c]
        if min_s == 0:
            return
        cover(col)
        r = D[col]
        while r != col:
            solution.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]
            dfs(k + 1)
            if found:
                return
            # backtrack
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            solution.pop()
            r = D[r]
        uncover(col)

    dfs(0)

    out = []
    if found:
        out.append("YES")
        for idx in solution:
            a, b, c = triples[idx]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()