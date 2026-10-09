import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    rows = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        rows.append((a, b, c))

    n_cols = 3 * q

    # Dancing Links structures
    max_nodes = t * 3 + n_cols + 1
    U = [0] * max_nodes
    D = [0] * max_nodes
    L = [0] * max_nodes
    R = [0] * max_nodes
    C = [0] * max_nodes  # column header for each node
    S = [0] * (n_cols + 1)  # size of column, header 0 is root

    # header nodes: 0 is root, 1..n_cols are column headers
    for i in range(n_cols + 1):
        U[i] = D[i] = i
        L[i] = i - 1
        R[i] = i + 1
    L[0] = n_cols
    R[n_cols] = 0

    node_cnt = n_cols + 1  # next free index

    row_head = []  # store first node index of each row for solution retrieval

    for r_idx, (a, b, c) in enumerate(rows):
        first = -1
        for col in (a, b, c):
            col += 1  # shift to 1..n_cols
            node = node_cnt
            node_cnt += 1
            C[node] = col
            # link into column (vertical)
            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            S[col] += 1
            # link into row (horizontal)
            if first == -1:
                first = node
                L[node] = R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node
        row_head.append(first)

    solution = []
    answer_rows = []

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

    def search(k):
        if R[0] == 0:  # all columns covered
            return True
        # choose column with minimal S
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
            if search(k + 1):
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

    if search(0):
        # retrieve original row indices from nodes in solution
        used_rows = set()
        for node in solution:
            # any node in the row maps to its row index via row_head list
            # we can find by walking left until we hit the first node of that row (which is stored)
            # Simpler: store mapping node->row index during construction
            pass
        # Build mapping node->row index
        node_to_row = {}
        for idx, head in enumerate(row_head):
            if head == -1:
                continue
            cur = head
            while True:
                node_to_row[cur] = idx
                cur = R[cur]
                if cur == head:
                    break
        selected = [rows[node_to_row[node]] for node in solution]
        # output
        out = ["YES"]
        for triple in selected:
            out.append(f"{triple[0]+1} {triple[1]+1} {triple[2]+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()