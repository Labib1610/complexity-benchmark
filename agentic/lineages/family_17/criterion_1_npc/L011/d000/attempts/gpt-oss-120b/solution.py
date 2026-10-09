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
    # Dancing Links structures
    # node 0 is the header
    size = [0] * (n + 1)          # column sizes, index 1..n
    U = [0] * (3 * t + n + 1)
    D = [0] * (3 * t + n + 1)
    L = [0] * (3 * t + n + 1)
    R = [0] * (3 * t + n + 1)
    C = [0] * (3 * t + n + 1)     # column of each node
    row_id = [0] * (3 * t + n + 1)

    # header links columns in a circular list
    head = 0
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_cnt = n
    # add rows
    for rid, (a, b, c) in enumerate(triples, 1):
        first = None
        for col in (a, b, c):
            node_cnt += 1
            C[node_cnt] = col
            row_id[node_cnt] = rid
            # insert into column list (at bottom)
            D[node_cnt] = col
            U[node_cnt] = U[col]
            D[U[col]] = node_cnt
            U[col] = node_cnt
            size[col] += 1
            # link row horizontally
            if first is None:
                first = node_cnt
                L[node_cnt] = R[node_cnt] = node_cnt
            else:
                # insert to the right of first
                L[node_cnt] = L[first]
                R[node_cnt] = first
                R[L[first]] = node_cnt
                L[first] = node_cnt

    solution_rows = []

    def cover(col):
        # remove column header
        R[L[col]] = R[col]
        L[R[col]] = L[col]
        # remove rows
        i = D[col]
        while i != col:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                size[C[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        R[L[col]] = col
        L[R[col]] = col

    def search(k):
        if R[head] == head:   # all columns covered
            return True
        # choose column with minimal size
        c = R[head]
        min_sz = size[c]
        col = c
        j = R[c]
        while j != head:
            if size[j] < min_sz:
                min_sz = size[j]
                col = j
                if min_sz == 0:
                    break
            j = R[j]
        if min_sz == 0:
            return False
        cover(col)
        r = D[col]
        while r != col:
            solution_rows.append(row_id[r])
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
            solution_rows.pop()
            r = D[r]
        uncover(col)
        return False

    ok = search(0)
    out = []
    if ok:
        out.append("YES")
        # retrieve triples in order of solution_rows
        chosen = [triples[i - 1] for i in solution_rows]
        for a, b, c in chosen:
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()