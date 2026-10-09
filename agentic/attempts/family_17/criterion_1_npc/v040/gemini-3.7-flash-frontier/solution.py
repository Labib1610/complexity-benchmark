import sys

# Increase recursion depth for deep search trees
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    t = int(input_data[1])
    n = 3 * q

    triplets = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        triplets.append((a, b, c))

    # DLX arrays
    MAX_NODES = (n + 1) + t * 3 + 100
    L = [0] * MAX_NODES
    R = [0] * MAX_NODES
    U = [0] * MAX_NODES
    D = [0] * MAX_NODES
    col = [0] * MAX_NODES
    row = [0] * MAX_NODES
    size = [0] * (n + 1)

    # Initialize column headers
    for i in range(n + 1):
        L[i] = (i - 1 + n + 1) % (n + 1)
        R[i] = (i + 1) % (n + 1)
        U[i] = i
        D[i] = i
        col[i] = i

    node_cnt = n + 1

    for r_idx, (a, b, c) in enumerate(triplets):
        first_node = node_cnt
        for c_idx in (a, b, c):
            cur = node_cnt
            node_cnt += 1

            col[cur] = c_idx
            row[cur] = r_idx
            size[c_idx] += 1

            # Insert into column list (at bottom, above header)
            U[cur] = U[c_idx]
            D[cur] = c_idx
            D[U[c_idx]] = cur
            U[c_idx] = cur

        # Link row horizontally
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

        # Choose column with minimum size (MRV heuristic)
        c = R[0]
        min_size = size[c]
        cur = R[0]
        while cur != 0:
            if size[cur] < min_size:
                min_size = size[cur]
                c = cur
            cur = R[cur]

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
        print("YES")
        out = []
        for r_idx in ans:
            a, b, c = triplets[r_idx]
            out.append(f"{a} {b} {c}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == "__main__":
    solve()