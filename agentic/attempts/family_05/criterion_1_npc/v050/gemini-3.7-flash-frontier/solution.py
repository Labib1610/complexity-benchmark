import sys


def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    k = int(data[0])
    t = int(data[1])

    if t < k:
        print("NO")
        return

    triples = []
    idx = 2
    for _ in range(t):
        x = int(data[idx]) - 1
        y = int(data[idx + 1]) - 1
        z = int(data[idx + 2]) - 1
        idx += 3
        triples.append((x, y, z))

    num_cols = 3 * k
    max_nodes = num_cols + 1 + 3 * t + 5

    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    col = [0] * max_nodes
    row_id = [0] * max_nodes
    sz = [0] * (num_cols + 1)

    for i in range(num_cols + 1):
        L[i] = (i - 1 + num_cols + 1) % (num_cols + 1)
        R[i] = (i + 1) % (num_cols + 1)
        U[i] = i
        D[i] = i

    node_cnt = num_cols + 1

    for r, (x, y, z) in enumerate(triples):
        cols = [x + 1, k + y + 1, 2 * k + z + 1]
        first = node_cnt
        for c in cols:
            cur = node_cnt
            node_cnt += 1
            col[cur] = c
            row_id[cur] = r
            sz[c] += 1
            D[cur] = c
            U[cur] = U[c]
            D[U[c]] = cur
            U[c] = cur

        for i in range(3):
            cur = first + i
            nxt = first + (i + 1) % 3
            prv = first + (i + 2) % 3
            R[cur] = nxt
            L[cur] = prv

    def cover(c):
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                sz[col[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                sz[col[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c

    solution = []

    def search():
        if R[0] == 0:
            return True

        c = R[0]
        min_sz = sz[c]
        temp = R[c]
        while temp != 0:
            if sz[temp] < min_sz:
                min_sz = sz[temp]
                c = temp
            temp = R[temp]

        if min_sz == 0:
            return False

        cover(c)
        i = D[c]
        while i != c:
            solution.append(row_id[i])
            j = R[i]
            while j != i:
                cover(col[j])
                j = R[j]

            if search():
                return True

            solution.pop()
            j = L[i]
            while j != i:
                uncover(col[j])
                j = L[j]
            i = D[i]

        uncover(c)
        return False

    sys.setrecursionlimit(2000)
    if search():
        print("YES")
        out = []
        for r in solution:
            x, y, z = triples[r]
            out.append(f"{x + 1} {y + 1} {z + 1}")
        print("\n".join(out))
    else:
        print("NO")


if __name__ == "__main__":
    solve()