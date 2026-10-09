import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q                     # number of columns
    rows = []                     # list of triples (0‑based column indices)
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        rows.append((a, b, c))

    # ---------- build dancing links ----------
    max_nodes = t * 3 + n + 1      # +1 for head
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes            # column of node
    row_of = [0] * max_nodes

    S = [0] * (n + 1)              # column sizes, column 0 is head
    head = 0

    # initialise column headers (0 is head, 1..n are real columns)
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_id = n + 1                # next free node index
    for r_idx, (a, b, c) in enumerate(rows):
        first = None
        for col in (a + 1, b + 1, c + 1):   # columns are 1‑based in DLX
            nid = node_id
            node_id += 1
            C[nid] = col
            row_of[nid] = r_idx

            # insert into column list (at bottom)
            U[nid] = U[col]
            D[nid] = col
            D[U[col]] = nid
            U[col] = nid
            S[col] += 1

            # link row horizontally
            if first is None:
                first = nid
                L[nid] = R[nid] = nid
            else:
                L[nid] = L[first]
                R[nid] = first
                R[L[first]] = nid
                L[first] = nid

    # ---------- DLX operations ----------
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

    answer_rows = []

    def search(k: int) -> bool:
        if R[head] == head:          # all columns covered
            return True
        # choose column with minimal size
        c = R[head]
        min_s = S[c]
        j = R[c]
        while j != head:
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
            answer_rows.append(row_of[r])
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
        uncover(c)
        return False

    possible = search(0)

    out = []
    if possible:
        out.append("YES")
        # translate stored row indices back to original triples (1‑based)
        for rid in answer_rows:
            a, b, c = rows[rid]
            out.append(f"{a+1} {b+1} {c+1}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()