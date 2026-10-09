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
    max_nodes = 3 * t + n + 5

    # DLX arrays
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes           # column header of node
    S = [0] * (n + 1)             # column sizes, 1‑based
    row_id = [0] * max_nodes      # which triple a node belongs to

    head = 0
    # initialise column headers 1..n and link them left‑right
    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = n
    R[n] = 0

    node_cnt = n + 1  # next free index

    # add rows
    for idx, (a, b, c) in enumerate(triples, 1):
        first = -1
        for col in (a, b, c):
            nd = node_cnt
            node_cnt += 1
            C[nd] = col
            row_id[nd] = idx
            # vertical links (insert above header)
            U[nd] = U[col]
            D[nd] = col
            D[U[col]] = nd
            U[col] = nd
            S[col] += 1
            # horizontal links
            if first == -1:
                first = nd
                L[nd] = R[nd] = nd
            else:
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd

    answer_rows = []

    def cover(c):
        # remove column header
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        # remove rows
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                S[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                S[C[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c

    found = False

    def search(k):
        nonlocal found
        if R[head] == head:          # all columns covered
            found = True
            return True
        # choose column with minimal size
        c = R[head]
        min_s = S[c]
        cc = c
        j = R[c]
        while j != head:
            if S[j] < min_s:
                min_s = S[j]
                cc = j
                if min_s == 0:
                    break
            j = R[j]
        if min_s == 0:
            return False
        cover(cc)
        r = D[cc]
        while r != cc:
            answer_rows.append(row_id[r])
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
            answer_rows.pop()
            r = D[r]
        uncover(cc)
        return False

    if search(0):
        out = ["YES"]
        for idx in answer_rows:
            a, b, c = triples[idx - 1]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()