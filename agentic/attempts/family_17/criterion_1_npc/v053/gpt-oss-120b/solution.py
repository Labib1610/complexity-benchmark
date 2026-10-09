import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    ncol = 3 * q                     # number of elements / columns

    # DLX arrays (0‑based indexing, but we keep column headers at 1..ncol)
    max_nodes = 1 + ncol + 3 * t + 5
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes
    S = [0] * (ncol + 1)             # size of each column
    row_id_of_node = [0] * max_nodes

    # header node = 0
    for i in range(ncol + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = ncol
    R[ncol] = 0

    node_cnt = ncol + 1
    rows = []                        # store triples for output, index = row number (1‑based)

    for rid in range(1, t + 1):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        rows.append((a, b, c))
        first = -1
        for col in (a, b, c):
            node = node_cnt
            node_cnt += 1
            C[node] = col
            row_id_of_node[node] = rid
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
                # insert to the left of first
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

    answer_rows = [0] * (q + 1)      # store chosen row ids, 1‑based depth

    # ----- DLX core operations -----
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

    # ----- recursive search -----
    def search(k: int) -> bool:
        if R[0] == 0:                # all columns covered
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
            answer_rows[k] = row_id_of_node[r]
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

    possible = search(0)

    out = []
    if possible:
        out.append("YES")
        for i in range(q):
            a, b, c = rows[answer_rows[i] - 1]
            out.append(f"{a} {b} {c}")
    else:
        out.append("NO")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()