import sys

sys.setrecursionlimit(10000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    edges = []
    adj = [[] for _ in range(n)]
    pos = 2

    for eid in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        edges.append((u, v))
        adj[u].append(eid)
        adj[v].append(eid)

    if any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # A cubic graph with a bridge cannot have a 3-edge-coloring.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    roots = []
    has_bridge = False

    def dfs_bridge(u, parent_edge):
        nonlocal timer, has_bridge
        tin[u] = low[u] = timer
        timer += 1

        for eid in adj[u]:
            if eid == parent_edge:
                continue
            a, b = edges[eid]
            v = b if a == u else a

            if tin[v] == -1:
                dfs_bridge(v, eid)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    has_bridge = True
            else:
                low[u] = min(low[u], tin[v])

    for v in range(n):
        if tin[v] == -1:
            roots.append(v)
            dfs_bridge(v, -1)

    if has_bridge:
        print("NO")
        return

    # Exact cover columns:
    #   one column for every edge (choose exactly one color),
    #   one column for every (vertex, color) pair.
    column_count = m + 3 * n

    L = list(range(column_count + 1))
    R = list(range(column_count + 1))
    U = list(range(column_count + 1))
    D = list(range(column_count + 1))
    C = list(range(column_count + 1))
    S = [0] * (column_count + 1)
    row_of_node = [-1] * (column_count + 1)

    for c in range(column_count + 1):
        L[c] = c - 1
        R[c] = c + 1
    L[0] = column_count
    R[column_count] = 0

    row_anchor = [-1] * (3 * m)

    def append_node(col, row_id):
        idx = len(C)
        C.append(col)
        row_of_node.append(row_id)

        last = U[col]
        U.append(last)
        D.append(col)
        D[last] = idx
        U[col] = idx
        S[col] += 1

        L.append(idx)
        R.append(idx)
        return idx

    def add_row(row_id, columns):
        first = -1
        for col in columns:
            node = append_node(col, row_id)
            if first == -1:
                first = node
            else:
                last = L[first]
                R[last] = node
                L[node] = last
                R[node] = first
                L[first] = node
        row_anchor[row_id] = first

    for eid, (u, v) in enumerate(edges):
        edge_col = 1 + eid
        for color in range(3):
            vertex_u_col = 1 + m + 3 * u + color
            vertex_v_col = 1 + m + 3 * v + color
            add_row(3 * eid + color,
                    (edge_col, vertex_u_col, vertex_v_col))

    def cover(col):
        R[L[col]] = R[col]
        L[R[col]] = L[col]

        i = D[col]
        while i != col:
            j = R[i]
            while j != i:
                D[U[j]] = D[j]
                U[D[j]] = U[j]
                S[C[j]] -= 1
                j = R[j]
            i = D[i]

    def uncover(col):
        i = U[col]
        while i != col:
            j = L[i]
            while j != i:
                S[C[j]] += 1
                D[U[j]] = j
                U[D[j]] = j
                j = L[j]
            i = U[i]

        R[L[col]] = col
        L[R[col]] = col

    fixed_rows = []

    # Break the global color-permutation symmetry independently in each
    # connected component.
    for root in roots:
        root_edges = sorted(adj[root])
        for color, eid in enumerate(root_edges):
            rid = 3 * eid + color
            fixed_rows.append(rid)
            node = row_anchor[rid]
            start = node
            while True:
                cover(C[node])
                node = R[node]
                if node == start:
                    break

    chosen_rows = []

    def search():
        if R[0] == 0:
            return True

        col = R[0]
        best_size = S[col]
        cur = R[col]

        while cur != 0:
            size = S[cur]
            if size < best_size:
                col = cur
                best_size = size
                if size == 0:
                    break
            cur = R[cur]

        if best_size == 0:
            return False

        cover(col)
        row_node = D[col]

        while row_node != col:
            chosen_rows.append(row_of_node[row_node])

            j = R[row_node]
            while j != row_node:
                cover(C[j])
                j = R[j]

            if search():
                return True

            j = L[row_node]
            while j != row_node:
                uncover(C[j])
                j = L[j]

            chosen_rows.pop()
            row_node = D[row_node]

        uncover(col)
        return False

    if not search():
        print("NO")
        return

    colors = [0] * m
    for rid in fixed_rows:
        colors[rid // 3] = rid % 3 + 1
    for rid in chosen_rows:
        colors[rid // 3] = rid % 3 + 1

    print("YES")
    print(*colors)


if __name__ == "__main__":
    main()