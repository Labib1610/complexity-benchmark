import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    q = int(input_data[0])
    t = int(input_data[1])
    n = 3 * q

    if t < q:
        print("NO")
        return

    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        triples.append((a, b, c))
        idx += 3

    # Dancing Links (DLX) Setup
    # Node 0 is root.
    # Nodes 1..n are column headers.
    # Subsequent nodes are 3 per triple: total nodes = n + 1 + 3 * t.

    total_nodes = n + 1 + 3 * t
    L = [0] * total_nodes
    R = [0] * total_nodes
    U = [0] * total_nodes
    D = [0] * total_nodes
    col = [0] * total_nodes
    row = [0] * total_nodes
    size = [0] * (n + 1)

    # Initialize column headers
    for i in range(n + 1):
        L[i] = (i - 1 + n + 1) % (n + 1)
        R[i] = (i + 1) % (n + 1)
        U[i] = i
        D[i] = i

    node_idx = n + 1
    for r_idx, (a, b, c) in enumerate(triples):
        nodes_in_row = [node_idx, node_idx + 1, node_idx + 2]
        node_idx += 3
        cols = (a, b, c)

        for i in range(3):
            curr = nodes_in_row[i]
            c_col = cols[i]
            col[curr] = c_col
            row[curr] = r_idx
            size[c_col] += 1

            # Insert into column circular list (at bottom)
            U[curr] = U[c_col]
            D[curr] = c_col
            D[U[c_col]] = curr
            U[c_col] = curr

            # Insert into row circular list
            L[curr] = nodes_in_row[(i - 1) % 3]
            R[curr] = nodes_in_row[(i + 1) % 3]

    def cover(c):
        R[L[c]] = R[c]
        L[R[c]] = L[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                D[U[j]] = D[j]
                U[D[j]] = U[j]
                size[col[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                size[col[j]] += 1
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

        # Choose column with minimum size
        c = R[0]
        min_size = size[c]
        curr = R[c]
        while curr != 0:
            if size[curr] < min_size:
                min_size = size[curr]
                c = curr
                if min_size == 0:
                    break
            curr = R[curr]

        if min_size == 0:
            return False

        cover(c)
        r = D[c]
        while r != c:
            solution.append(row[r])
            j = R[r]
            while j != r:
                cover(col[j])
                j = R[j]

            if search():
                return True

            solution.pop()
            j = L[r]
            while j != r:
                uncover(col[j])
                j = L[j]

            r = D[r]

        uncover(c)
        return False

    if search():
        out = ["YES"]
        for r_idx in solution:
            a, b, c = triples[r_idx]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        print("NO")

if __name__ == '__main__':
    solve()