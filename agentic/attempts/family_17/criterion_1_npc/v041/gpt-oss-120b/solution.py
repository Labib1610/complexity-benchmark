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
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))

    n = 3 * q                     # number of columns
    # ---------- DLX structures ----------
    max_nodes = 3 * t + n + 1     # header + column headers + all nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes           # column of node
    row_id = [0] * max_nodes      # which triple this node belongs to
    size = [0] * (n + 1)          # column sizes, column 0 is header

    # header is 0
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_cnt = n  # last used index

    # add rows
    for rid, (a, b, c) in enumerate(triples):
        first = -1
        for col in (a, b, c):
            node_cnt += 1
            idx = node_cnt
            C[idx] = col + 1          # columns are 1..n
            row_id[idx] = rid

            # vertical links
            U[idx] = U[C[idx]]
            D[idx] = C[idx]
            D[U[idx]] = idx
            U[C[idx]] = idx
            size[col + 1] += 1

            # horizontal links
            if first == -1:
                first = idx
                L[idx] = R[idx] = idx
            else:
                L[idx] = L[first]
                R[idx] = first
                R[L[first]] = idx
                L[first] = idx

    solution_rows = []

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
        L[R[col]] = col
        R[L[col]] = col

    def search(k):
        if R[0] == 0:          # all columns covered
            return True
        # choose column with minimal size
        c = R[0]
        min_sz = size[c]
        j = R[c]
        while j != 0:
            if size[j] < min_sz:
                min_sz = size[j]
                c = j
                if min_sz == 0:
                    break
            j = R[j]
        if min_sz == 0:
            return False

        cover(c)
        r = D[c]
        while r != c:
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
        uncover(c)
        return False

    ok = search(0)
    out = []
    if ok:
        out.append("YES")
        # solution_rows may contain duplicates because each row appears three times,
        # we need unique rows in order of selection.
        used = set()
        for rid in solution_rows:
            if rid not in used:
                used.add(rid)
                a, b, c = triples[rid]
                out.append(f"{a+1} {b+1} {c+1}")
        # ensure exactly q lines
        # (the algorithm guarantees this)
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()