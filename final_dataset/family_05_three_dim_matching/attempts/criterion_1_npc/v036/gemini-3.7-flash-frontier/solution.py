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
    max_nodes = num_cols + 1 + 3 * t + 10

    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes
    Row = [0] * max_nodes
    sz = [0] * (num_cols + 1)

    for c in range(num_cols + 1):
        sz[c] = 0
        U[c] = c
        D[c] = c
        L[c] = (c - 1) % (num_cols + 1)
        R[c] = (c + 1) % (num_cols + 1)

    node_cnt = num_cols + 1

    for r, (x, y, z) in enumerate(triples):
        cols = [x, k + y, 2 * k + z]
        first_node = node_cnt
        for j, col in enumerate(cols):
            node = node_cnt
            node_cnt += 1
            C[node] = col
            Row[node] = r
            sz[col] += 1

            D[node] = col
            U[node] = U[col]
            D[U[col]] = node
            U[col] = node

            if j == 0:
                L[node] = node
                R[node] = node
            else:
                L[node] = node - 1
                R[node] = first_node
                R[node - 1] = node
                L[first_node] = node

    def cover(c):
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                sz[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                sz[C[j]] += 1
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

        c = R[0]
        min_sz = sz[c]
        curr = R[c]
        while curr != 0:
            if sz[curr] < min_sz:
                min_sz = sz[curr]
                c = curr
            curr = R[curr]

        if min_sz == 0:
            return False

        cover(c)
        i = D[c]
        while i != c:
            ans.append(Row[i])
            j = R[i]
            while j != i:
                cover(C[j])
                j = R[j]

            if search():
                return True

            j = L[i]
            while j != i:
                uncover(C[j])
                j = L[j]
            ans.pop()
            i = D[i]

        uncover(c)
        return False

    sys.setrecursionlimit(2000)

    if search():
        print("YES")
        for r in ans:
            print(f"{triples[r][0]} {triples[r][1]} {triples[r][2]}")
    else:
        print("NO")


if __name__ == "__main__":
    solve()