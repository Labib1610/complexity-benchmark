import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    t = int(input_data[1])

    triples = []
    idx = 2
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        z = int(input_data[idx + 2])
        idx += 3
        triples.append((x, y, z))

    num_cols = 3 * k

    # Pre-allocate DLX arrays
    # 1 root + num_cols headers + 3 * t nodes
    max_nodes = 1 + num_cols + 3 * t + 10
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    Col = [0] * max_nodes
    Row = [0] * max_nodes
    size = [0] * (num_cols + 1)

    # Initialize headers
    for i in range(num_cols + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = i
        D[i] = i
    L[0] = num_cols
    R[num_cols] = 0

    node_cnt = num_cols + 1

    for t_idx, (x, y, z) in enumerate(triples):
        cols = [x, k + y, 2 * k + z]
        row_nodes = []
        for c in cols:
            node = node_cnt
            node_cnt += 1
            Col[node] = c
            Row[node] = t_idx
            size[c] += 1

            # Insert node at bottom of column c
            U[node] = U[c]
            D[node] = c
            D[U[c]] = node
            U[c] = node

            row_nodes.append(node)

        # Link row nodes horizontally
        for i in range(3):
            L[row_nodes[i]] = row_nodes[(i - 1) % 3]
            R[row_nodes[i]] = row_nodes[(i + 1) % 3]

    def cover(c):
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                size[Col[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[Col[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c

    ans = []

    def search():
        if R[0] == 0:
            return True

        # Choose column with minimum size
        c = R[0]
        min_s = size[c]
        curr = R[c]
        while curr != 0:
            if size[curr] < min_s:
                min_s = size[curr]
                c = curr
            curr = R[curr]

        if min_s == 0:
            return False

        cover(c)
        r = D[c]
        while r != c:
            ans.append(Row[r])
            j = R[r]
            while j != r:
                cover(Col[j])
                j = R[j]
            if search():
                return True
            j = L[r]
            while j != r:
                uncover(Col[j])
                j = L[j]
            ans.pop()
            r = D[r]
        uncover(c)
        return False

    sys.setrecursionlimit(200000)
    if search():
        print("YES")
        for t_idx in ans:
            x, y, z = triples[t_idx]
            print(f"{x} {y} {z}")
    else:
        print("NO")


if __name__ == "__main__":
    solve()