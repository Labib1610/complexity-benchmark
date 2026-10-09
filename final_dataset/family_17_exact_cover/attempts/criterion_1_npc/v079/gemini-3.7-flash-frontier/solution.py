import sys

# Increase recursion depth for deep search trees
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    q = int(input_data[0])
    t = int(input_data[1])

    num_cols = 3 * q
    triads = []
    idx = 2
    for i in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        triads.append((a, b, c))

    max_nodes = 3 * t + num_cols + 5
    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    col = [0] * max_nodes
    row = [0] * max_nodes
    size = [0] * (num_cols + 1)

    for i in range(num_cols + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = i
        D[i] = i
    L[0] = num_cols
    R[num_cols] = 0

    node_idx = num_cols + 1
    for r_idx, (a, b, c) in enumerate(triads):
        first_node = node_idx
        for c_val in (a, b, c):
            curr = node_idx
            node_idx += 1
            col[curr] = c_val
            row[curr] = r_idx
            size[c_val] += 1

            U[curr] = U[c_val]
            D[curr] = c_val
            D[U[c_val]] = curr
            U[c_val] = curr

        L[first_node] = first_node + 2
        R[first_node] = first_node + 1
        L[first_node + 1] = first_node
        R[first_node + 1] = first_node + 2
        L[first_node + 2] = first_node + 1
        R[first_node + 2] = first_node

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

    def search():
        if R[0] == 0:
            return True

        c = R[0]
        min_size = size[c]
        j = R[c]
        while j != 0:
            if size[j] < min_size:
                min_size = size[j]
                c = j
            j = R[j]

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
            a, b, c = triads[r_idx]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    solve()