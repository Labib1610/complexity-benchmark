import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q  # number of elements to cover
    rows = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        rows.append((a, b, c))

    # Dancing Links structures
    max_nodes = t * 3 + n + 1
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes  # column header for each node
    S = [0] * (n + 1)    # size of each column (header 0 is root)
    row_id = [0] * max_nodes

    # header 0 is root
    for i in range(n + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n
    R[n] = 0

    node_cnt = n + 1

    def add_node(col, r):
        nonlocal node_cnt
        idx = node_cnt
        node_cnt += 1
        # vertical links
        U[idx] = U[col]
        D[idx] = col
        D[U[col]] = idx
        U[col] = idx
        # horizontal links (will be linked later)
        L[idx] = R[idx] = idx
        C[idx] = col
        row_id[idx] = r
        S[col] += 1
        return idx

    # build matrix
    row_nodes = []  # first node of each row
    for r, (a, b, c) in enumerate(rows):
        first = None
        for col in (a, b, c):
            nd = add_node(col + 1, r)  # columns are 1..n
            if first is None:
                first = nd
            else:
                # link horizontally
                L[nd] = L[first]
                R[nd] = first
                R[L[first]] = nd
                L[first] = nd
        row_nodes.append(first)

    ans_rows = []

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

    def search(k):
        if R[0] == 0:  # all columns covered
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
            ans_rows.append(row_id[r])
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
            ans_rows.pop()
            r = D[r]
        uncover(c)
        return False

    possible = search(0)

    if not possible:
        print("NO")
    else:
        print("YES")
        for rid in ans_rows:
            a, b, c = rows[rid]
            print(a + 1, b + 1, c + 1)

if __name__ == "__main__":
    solve()