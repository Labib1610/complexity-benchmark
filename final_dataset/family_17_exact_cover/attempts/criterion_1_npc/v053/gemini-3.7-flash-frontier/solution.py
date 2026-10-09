import sys


def solve():
    sys.setrecursionlimit(5000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    q = int(input_data[0])
    t = int(input_data[1])
    N = 3 * q

    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        triples.append((a, b, c))
        idx += 3

    total_nodes = N + 1 + 3 * t
    L = [0] * total_nodes
    R = [0] * total_nodes
    U = [0] * total_nodes
    D = [0] * total_nodes
    C = [0] * total_nodes
    row_id = [0] * total_nodes
    size = [0] * (N + 1)

    for i in range(N + 1):
        L[i] = (i - 1 + N + 1) % (N + 1)
        R[i] = (i + 1) % (N + 1)
        U[i] = i
        D[i] = i
        size[i] = 0

    node_count = N + 1
    for r_idx, (a, b, c) in enumerate(triples):
        nodes = [node_count, node_count + 1, node_count + 2]
        node_count += 3

        for k, col in enumerate((a, b, c)):
            n = nodes[k]
            C[n] = col
            row_id[n] = r_idx
            size[col] += 1

            U[n] = U[col]
            D[n] = col
            D[U[col]] = n
            U[col] = n

            L[n] = nodes[(k - 1) % 3]
            R[n] = nodes[(k + 1) % 3]

    def cover(c):
        L[R[c]] = L[c]
        R[L[c]] = R[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                U[D[j]] = U[j]
                D[U[j]] = D[j]
                size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[C[j]] += 1
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
        min_sz = size[c]
        curr = R[c]
        while curr != 0:
            if size[curr] < min_sz:
                min_sz = size[curr]
                c = curr
                if min_sz == 0:
                    break
            curr = R[curr]

        if min_sz == 0:
            return False

        cover(c)
        r = D[c]
        while r != c:
            ans.append(row_id[r])
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
        out = ["YES"]
        for r in ans:
            out.append(f"{triples[r][0]} {triples[r][1]} {triples[r][2]}")
        print("\n".join(out))
    else:
        print("NO")


if __name__ == "__main__":
    solve()