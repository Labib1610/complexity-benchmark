import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    q = int(input_data[0])
    t = int(input_data[1])

    C = 3 * q
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        triples.append((a, b, c))

    max_nodes = C + 1 + 3 * t + 5
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    col = [0] * max_nodes
    row = [0] * max_nodes
    size = [0] * (C + 1)

    for c in range(C + 1):
        L[c] = c - 1
        R[c] = c + 1
        U[c] = c
        D[c] = c
        col[c] = c
    L[0] = C
    R[C] = 0

    node_count = C

    for r, (c1, c2, c3) in enumerate(triples):
        nodes_in_row = []
        for c in (c1, c2, c3):
            node_count += 1
            i = node_count
            col[i] = c
            row[i] = r
            size[c] += 1
            U[i] = U[c]
            D[i] = c
            D[U[c]] = i
            U[c] = i
            nodes_in_row.append(i)

        n1, n2, n3 = nodes_in_row
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
                size[col[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[col[j]] += 1
                U[D[j]] = j
                D[U[j]] = j
                j = L[j]
            i = U[i]
        L[R[c]] = c
        R[L[c]] = c

    ans = []
    sys.setrecursionlimit(max(2000, q + 100))

    def search():
        if R[0] == 0:
            return True

        c = R[0]
        min_size = size[c]
        curr = R[c]
        while curr != 0:
            if size[curr] < min_size:
                min_size = size[curr]
                c = curr
            curr = R[curr]

        if min_size == 0:
            return False

        cover(c)
        r = D[c]
        while r != c:
            ans.append(row[r])
            j = R[r]
            while j != r:
                cover(col[j])
                j = R[j]

            if search():
                return True

            ans.pop()
            j = L[r]
            while j != r:
                uncover(col[j])
                j = L[j]
            r = D[r]

        uncover(c)
        return False

    if search():
        out = ["YES"]
        for r_idx in ans:
            a, b, c = triples[r_idx]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    solve()