import sys

# Increase recursion depth for search
sys.setrecursionlimit(5000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    n = 3 * q

    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        triples.append((a, b, c))

    max_nodes = n + 1 + 3 * t + 10

    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes
    row_idx = [0] * max_nodes
    sz = [0] * (n + 1)

    for i in range(n + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = i
        D[i] = i
    L[0] = n
    R[n] = 0

    node_cnt = n

    for r, (a, b, c) in enumerate(triples):
        first_node = node_cnt + 1
        for col in (a, b, c):
            node_cnt += 1
            cur = node_cnt
            C[cur] = col
            row_idx[cur] = r
            sz[col] += 1

            U[cur] = U[col]
            D[cur] = col
            D[U[col]] = cur
            U[col] = cur

        n1, n2, n3 = first_node, first_node + 1, first_node + 2
        L[n1] = n3
        R[n1] = n2
        L[n2] = n1
        R[n2] = n3
        L[n3] = n2
        R[n3] = n1

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
        temp = R[c]
        while temp != 0:
            if sz[temp] < min_sz:
                min_sz = sz[temp]
                c = temp
            temp = R[temp]

        if min_sz == 0:
            return False

        cover(c)

        r = D[c]
        while r != c:
            ans.append(row_idx[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]

            if search():
                return True

            ans.pop()
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            r = D[r]

        uncover(c)
        return False

    if search():
        print("YES")
        for r in ans:
            a, b, c = triples[r]
            print(f"{a} {b} {c}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()