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

    n = 3 * q                     # number of columns
    # DLX structures using integer indices
    # node 0 is the header
    size = 1                      # current number of nodes
    max_nodes = 1 + n + t * 3 + 5

    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes           # column of a node (for data nodes)
    S = [0] * (n + 1)             # column sizes, index 1..n
    row_id = [0] * max_nodes      # which input row a node belongs to

    # header links
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = n
    R[n] = 0

    # add rows
    for idx, (a, b, c) in enumerate(triples, start=1):
        first = None
        for col in (a, b, c):
            node = size
            size += 1
            C[node] = col
            row_id[node] = idx
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

    solution = []

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
        if R[0] == 0:          # no columns left
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
        uncover(c)
        return False

    ok = search(0)
    out = []
    if ok:
        out.append("YES")
        # solution contains row indices, need to output the triples
        for idx in solution:
            a, b, c = triples[idx - 1]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()