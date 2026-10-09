import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    t = int(input_data[1])

    triads = []
    idx = 2
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        z = int(input_data[idx + 2])
        idx += 3
        triads.append((x, y, z))

    num_cols = 3 * k
    root = num_cols

    # DLX arrays
    # Nodes 0 .. num_cols-1 are column headers
    # Node root (num_cols) is the master root
    max_nodes = num_cols + 1 + 3 * t + 10

    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    col = [0] * max_nodes
    row_id = [0] * max_nodes
    size = [0] * (num_cols + 1)

    # Initialize column headers
    for i in range(num_cols + 1):
        L[i] = (i - 1) % (num_cols + 1)
        R[i] = (i + 1) % (num_cols + 1)
        U[i] = i
        D[i] = i
        col[i] = i

    node_count = num_cols + 1

    for r_idx, (x, y, z) in enumerate(triads):
        cols = [x - 1, k + (y - 1), 2 * k + (z - 1)]
        first = -1
        for c in cols:
            node = node_count
            node_count += 1

            col[node] = c
            row_id[node] = r_idx
            size[c] += 1

            # Insert vertically at bottom of column c
            U[node] = U[c]
            D[node] = c
            D[U[c]] = node
            U[c] = node

            # Insert horizontally into current row
            if first == -1:
                first = node
                L[node] = node
                R[node] = node
            else:
                L[node] = L[first]
                R[node] = first
                R[L[first]] = node
                L[first] = node

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

    solution = []

    def search():
        if R[root] == root:
            return True

        # Choose column with minimum size (MRV heuristic)
        min_size = float('inf')
        c = -1
        cur = R[root]
        while cur != root:
            if size[cur] < min_size:
                min_size = size[cur]
                c = cur
                if min_size == 0:
                    break
            cur = R[cur]

        if min_size == 0:
            return False

        cover(c)
        r = D[c]
        while r != c:
            solution.append(row_id[r])
            j = R[r]
            while j != r:
                cover(col[j])
                j = R[j]

            if search():
                return True

            j = L[r]
            while j != r:
                uncover(col[j])
                j = L[j]
            solution.pop()
            r = D[r]

        uncover(c)
        return False

    if search():
        out = ["YES"]
        for r_idx in solution:
            x, y, z = triads[r_idx]
            out.append(f"{x} {y} {z}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    main()