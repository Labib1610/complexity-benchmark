import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    t = int(input_data[1])

    triples = []
    idx = 2
    for _ in range(t):
        c = int(input_data[idx]) - 1
        e = int(input_data[idx+1]) - 1
        g = int(input_data[idx+2]) - 1
        idx += 3
        triples.append((c, e, g))

    num_cols = 3 * k
    max_nodes = num_cols + 1 + 3 * t

    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    C = [0] * max_nodes
    row_id = [0] * max_nodes
    size = [0] * (num_cols + 1)

    # Initialize column headers
    for i in range(num_cols + 1):
        L[i] = (i - 1 + num_cols + 1) % (num_cols + 1)
        R[i] = (i + 1) % (num_cols + 1)
        U[i] = i
        D[i] = i
        C[i] = i

    node_count = num_cols + 1

    for t_idx, (c, e, g) in enumerate(triples):
        cols = [c + 1, k + e + 1, 2 * k + g + 1]
        nodes = []
        for col in cols:
            node = node_count
            node_count += 1

            U[node] = U[col]
            D[node] = col
            D[U[col]] = node
            U[col] = node
            C[node] = col
            row_id[node] = t_idx
            size[col] += 1
            nodes.append(node)

        # Link horizontally
        n1, n2, n3 = nodes
        L[n1] = n3; R[n1] = n2
        L[n2] = n1; R[n2] = n3
        L[n3] = n2; R[n3] = n1

    def cover(c):
        R[L[c]] = R[c]
        L[R[c]] = L[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                D[U[j]] = D[j]
                U[D[j]] = U[j]
                size[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[C[j]] += 1
                D[U[j]] = j
                U[D[j]] = j
                j = L[j]
            i = U[i]
        R[L[c]] = c
        L[R[c]] = c

    solution = []

    def search():
        if R[0] == 0:
            return True

        # Choose column with min size (MRV)
        min_size = float('inf')
        c = -1
        col = R[0]
        while col != 0:
            if size[col] < min_size:
                min_size = size[col]
                c = col
                if min_size == 0:
                    break
            col = R[col]

        if min_size == 0:
            return False

        cover(c)
        r = D[c]
        while r != c:
            solution.append(row_id[r])
            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]

            if search():
                return True

            solution.pop()
            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]
            r = D[r]

        uncover(c)
        return False

    if search():
        print("YES")
        out = []
        for r_id in solution:
            c, e, g = triples[r_id]
            out.append(f"{c + 1} {e + 1} {g + 1}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()