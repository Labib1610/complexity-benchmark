import sys

# Increase recursion depth for deep search trees
sys.setrecursionlimit(500)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    q = int(input_data[0])
    t = int(input_data[1])

    total_elements = 3 * q
    idx = 2

    # Node allocations
    # Column headers: 0 to total_elements (0 is root)
    # Total nodes <= 1 + total_elements + 3 * t
    max_nodes = 1 + total_elements + 3 * t + 10

    L = [0] * max_nodes
    R = [0] * max_nodes
    U = [0] * max_nodes
    D = [0] * max_nodes
    col = [0] * max_nodes
    row = [0] * max_nodes
    sz = [0] * (total_elements + 1)

    # Initialize column headers
    for i in range(total_elements + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = i
        D[i] = i
        sz[i] = 0
    L[0] = total_elements
    R[total_elements] = 0

    node_count = total_elements + 1

    recipes = []
    for r in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        recipes.append((a, b, c))

        cols = [a, b, c]
        first_node = node_count
        for i, c_idx in enumerate(cols):
            cur = node_count + i
            col[cur] = c_idx
            row[cur] = r
            sz[c_idx] += 1

            # Insert into column list
            U[cur] = U[c_idx]
            D[cur] = c_idx
            D[U[c_idx]] = cur
            U[c_idx] = cur

            # Insert into row list
            L[cur] = cur - 1
            R[cur] = cur + 1

        L[first_node] = first_node + 2
        R[first_node + 2] = first_node
        node_count += 3

    def cover(c):
        R[L[c]] = R[c]
        L[R[c]] = L[c]
        i = D[c]
        while i != c:
            j = R[i]
            while j != i:
                D[U[j]] = D[j]
                U[D[j]] = U[j]
                sz[col[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(c):
        i = U[c]
        while i != c:
            j = L[i]
            while j != i:
                sz[col[j]] += 1
                D[U[j]] = j
                U[D[j]] = j
                j = L[j]
            i = U[i]
        R[L[c]] = c
        L[R[c]] = c

    ans = []

    def search():
        if R[0] == 0:
            return True

        # Choose column with minimum size (MRV heuristic)
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
        row_node = D[c]
        while row_node != c:
            ans.append(row[row_node])
            j = R[row_node]
            while j != row_node:
                cover(col[j])
                j = R[j]

            if search():
                return True

            ans.pop()
            j = L[row_node]
            while j != row_node:
                uncover(col[j])
                j = L[j]

            row_node = D[row_node]

        uncover(c)
        return False

    if search():
        out = ["YES"]
        for r_idx in ans:
            a, b, c = recipes[r_idx]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    solve()