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
        d = int(input_data[idx])
        f = int(input_data[idx + 1])
        m = int(input_data[idx + 2])
        idx += 3
        triples.append((d, f, m))

    num_cols = 3 * k

    # Pre-allocate arrays for DLX
    # Max nodes: num_cols + 1 (header) + 3 * t
    max_nodes = num_cols + 1 + 3 * t + 10
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes
    row_idx = [0] * max_nodes
    sz = [0] * (num_cols + 1)

    for i in range(num_cols + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = i
        D[i] = i
        C[i] = i
    L[0] = num_cols
    R[num_cols] = 0

    node_count = num_cols

    for r, (d, f, m) in enumerate(triples):
        cols = [d, k + f, 2 * k + m]
        first = node_count + 1
        for c in cols:
            node_count += 1
            cur = node_count
            C[cur] = c
            row_idx[cur] = r
            sz[c] += 1

            U[cur] = U[c]
            D[cur] = c
            D[U[c]] = cur
            U[c] = cur

            L[cur] = cur - 1
            R[cur] = cur + 1

        L[first] = node_count
        R[node_count] = first

    def cover(c):
        R[L[c]] = R[c]
        L[R[c]] = L[c]
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
        R[L[c]] = c
        L[R[c]] = c

    ans = []

    def search():
        if R[0] == 0:
            return True

        c = R[0]
        min_sz = sz[c]
        cur = R[c]
        while cur != 0:
            if sz[cur] < min_sz:
                min_sz = sz[cur]
                c = cur
            cur = R[cur]

        if min_sz == 0:
            return False

        cover(c)
        i = D[c]
        while i != c:
            ans.append(row_idx[i])
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

    if search():
        print("YES")
        out = []
        for r in ans:
            d, f, m = triples[r]
            out.append(f"{d} {f} {m}")
        print("\n".join(out))
    else:
        print("NO")


if __name__ == "__main__":
    solve()