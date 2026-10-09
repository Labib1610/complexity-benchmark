import sys

sys.setrecursionlimit(20000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    edges = []
    adj = [[] for _ in range(n)]
    p = 2

    for eid in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        edges.append((u, v))
        adj[u].append(eid)
        adj[v].append(eid)

    if m * 2 != 3 * n or any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    def other(eid, v):
        a, b = edges[eid]
        return b if a == v else a

    # A cubic graph with a bridge cannot have a proper 3-edge-coloring.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def bridge_dfs(v, parent_edge):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1

        for eid in adj[v]:
            if eid == parent_edge:
                continue
            w = other(eid, v)
            if tin[w] == -1:
                bridge_dfs(w, eid)
                low[v] = min(low[v], low[w])
                if low[w] > tin[v]:
                    has_bridge = True
            else:
                low[v] = min(low[v], tin[w])

    for s in range(n):
        if tin[s] == -1:
            bridge_dfs(s, -1)

    if has_bridge:
        print("NO")
        return

    # Cubic bipartite graphs are always 3-edge-colorable.
    side = [-1] * n
    bipartite = True

    for s in range(n):
        if side[s] != -1:
            continue
        side[s] = 0
        stack = [s]
        while stack:
            v = stack.pop()
            for eid in adj[v]:
                w = other(eid, v)
                if side[w] == -1:
                    side[w] = side[v] ^ 1
                    stack.append(w)
                elif side[w] == side[v]:
                    bipartite = False

    if bipartite:
        left_vertices = [v for v in range(n) if side[v] == 0]
        match_right = [-1] * n
        match_edge_right = [-1] * n
        match_edge_left = [-1] * n
        seen = [0] * n
        stamp = 0

        def augment(v):
            nonlocal stamp
            if seen[v] == stamp:
                return False
            seen[v] = stamp

            for eid in adj[v]:
                w = other(eid, v)
                old = match_right[w]
                if old == -1 or augment(old):
                    match_right[w] = v
                    match_edge_right[w] = eid
                    match_edge_left[v] = eid
                    return True
            return False

        for v in left_vertices:
            stamp += 1
            if not augment(v):
                print("NO")
                return

        answer = [0] * m
        for v in left_vertices:
            answer[match_edge_left[v]] = 1

        edge_neighbors = [[] for _ in range(m)]
        for v in range(n):
            remaining = [eid for eid in adj[v] if answer[eid] == 0]
            if len(remaining) != 2:
                print("NO")
                return
            a, b = remaining
            edge_neighbors[a].append(b)
            edge_neighbors[b].append(a)

        for start in range(m):
            if answer[start] != 0:
                continue
            answer[start] = 2
            stack = [start]
            while stack:
                eid = stack.pop()
                wanted = 5 - answer[eid]
                for nxt in edge_neighbors[eid]:
                    if answer[nxt] == 0:
                        answer[nxt] = wanted
                        stack.append(nxt)
                    elif answer[nxt] != wanted:
                        print("NO")
                        return

        print("YES")
        print(*answer)
        return

    # Exact-cover formulation solved by Algorithm X with Dancing Links.
    # Columns:
    #   one for each edge (choose exactly one color),
    #   one for each (vertex, color) pair.
    # Rows:
    #   assigning a color to an edge.
    column_count = m + 3 * n

    L = [0] * (column_count + 1)
    R = [0] * (column_count + 1)
    U = [0] * (column_count + 1)
    D = [0] * (column_count + 1)
    C = list(range(column_count + 1))
    S = [0] * (column_count + 1)
    ROW = [-1] * (column_count + 1)

    for i in range(column_count + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
    L[0] = column_count
    R[column_count] = 0

    row_node = [-1] * (3 * m)

    def add_node(col, row_id):
        idx = len(L)
        L.append(idx)
        R.append(idx)
        U.append(U[col])
        D.append(col)
        C.append(col)
        S.append(0)
        ROW.append(row_id)

        D[U[col]] = idx
        U[col] = idx
        S[col] += 1
        return idx

    for eid, (u, v) in enumerate(edges):
        for color in range(3):
            row_id = 3 * eid + color
            columns = (
                1 + eid,
                1 + m + 3 * u + color,
                1 + m + 3 * v + color,
            )

            first = -1
            for col in columns:
                node = add_node(col, row_id)
                if first == -1:
                    first = node
                else:
                    last = L[first]
                    R[last] = node
                    L[node] = last
                    R[node] = first
                    L[first] = node
            row_node[row_id] = first

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

    solution_rows = []

    # Fix the color permutation independently in every connected component.
    visited = [False] * n
    fixed_rows = []

    for s in range(n):
        if visited[s]:
            continue

        visited[s] = True
        stack = [s]
        while stack:
            v = stack.pop()
            for eid in adj[v]:
                w = other(eid, v)
                if not visited[w]:
                    visited[w] = True
                    stack.append(w)

        for color, eid in enumerate(adj[s]):
            fixed_rows.append(3 * eid + color)

    for row_id in fixed_rows:
        solution_rows.append(row_id)
        start = row_node[row_id]
        x = start
        while True:
            cover(C[x])
            x = R[x]
            if x == start:
                break

    def search():
        if R[0] == 0:
            return True

        col = R[0]
        best_size = S[col]
        x = R[col]
        while x != 0:
            if S[x] < best_size:
                col = x
                best_size = S[x]
                if best_size <= 1:
                    break
            x = R[x]

        if best_size == 0:
            return False

        cover(col)
        row = D[col]

        while row != col:
            solution_rows.append(ROW[row])

            j = R[row]
            while j != row:
                cover(C[j])
                j = R[j]

            if search():
                return True

            j = L[row]
            while j != row:
                uncover(C[j])
                j = L[j]

            solution_rows.pop()
            row = D[row]

        uncover(col)
        return False

    if not search():
        print("NO")
        return

    answer = [0] * m
    for row_id in solution_rows:
        answer[row_id // 3] = row_id % 3 + 1

    if any(color == 0 for color in answer):
        print("NO")
        return

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()