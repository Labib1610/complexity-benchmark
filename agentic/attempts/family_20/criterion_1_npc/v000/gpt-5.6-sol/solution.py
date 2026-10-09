import sys

sys.setrecursionlimit(20000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    if len(data) != 2 + 2 * m:
        print("NO")
        return

    edges = []
    adj = [[] for _ in range(n)]
    p = 2

    for eid in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if not (0 <= u < n and 0 <= v < n) or u == v:
            print("NO")
            return
        edges.append((u, v))
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    if any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # A bridge cannot occur in a 3-edge-colorable cubic graph.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def bridge_dfs(v, parent_edge):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1

        for to, eid in adj[v]:
            if eid == parent_edge:
                continue
            if tin[to] == -1:
                bridge_dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True
            else:
                low[v] = min(low[v], tin[to])

    for start in range(n):
        if tin[start] == -1:
            bridge_dfs(start, -1)

    if has_bridge:
        print("NO")
        return

    # Find connected components and their bipartitions when possible.
    side = [-1] * n
    components = []

    for start in range(n):
        if side[start] != -1:
            continue

        side[start] = 0
        stack = [start]
        vertices = []
        bipartite = True

        while stack:
            v = stack.pop()
            vertices.append(v)
            for to, _ in adj[v]:
                if side[to] == -1:
                    side[to] = side[v] ^ 1
                    stack.append(to)
                elif side[to] == side[v]:
                    bipartite = False

        components.append((vertices, bipartite))

    forced = {}

    # Cubic bipartite components are colored directly by three perfect matchings.
    for vertices, bipartite in components:
        if not bipartite:
            root = vertices[0]
            for color, (_, eid) in enumerate(adj[root]):
                forced[eid] = color
            continue

        left = [v for v in vertices if side[v] == 0]

        def perfect_matching(excluded):
            matched_left = [-1] * n
            matched_edge = [-1] * n

            def augment(v, seen, token):
                for to, eid in adj[v]:
                    if eid in excluded or seen[to] == token:
                        continue
                    seen[to] = token
                    if matched_left[to] == -1 or augment(matched_left[to], seen, token):
                        matched_left[to] = v
                        matched_edge[to] = eid
                        return True
                return False

            seen = [0] * n
            token = 0
            result = set()

            for v in left:
                token += 1
                if not augment(v, seen, token):
                    return None

            for v in vertices:
                if side[v] == 1:
                    if matched_edge[v] == -1:
                        return None
                    result.add(matched_edge[v])
            return result

        first = perfect_matching(set())
        if first is None:
            print("NO")
            return

        second = perfect_matching(first)
        if second is None:
            print("NO")
            return

        component_edges = set()
        for v in vertices:
            for _, eid in adj[v]:
                component_edges.add(eid)

        for eid in component_edges:
            if eid in first:
                forced[eid] = 0
            elif eid in second:
                forced[eid] = 1
            else:
                forced[eid] = 2

    # Exact-cover formulation:
    # - one column for each edge (choose exactly one color),
    # - one column for each (vertex, color) pair.
    column_count = m + 3 * n

    L = [0] * (column_count + 1)
    R = [0] * (column_count + 1)
    U = [0] * (column_count + 1)
    D = [0] * (column_count + 1)
    C = [0] * (column_count + 1)
    S = [0] * (column_count + 1)
    row_id = [-1] * (column_count + 1)

    for i in range(column_count + 1):
        L[i] = i - 1
        R[i] = i + 1
        U[i] = D[i] = i
        C[i] = i

    L[0] = column_count
    R[column_count] = 0

    def add_row(rid, columns):
        nodes = []
        for col0 in columns:
            col = col0 + 1
            idx = len(L)

            L.append(idx)
            R.append(idx)
            U.append(U[col])
            D.append(col)
            C.append(col)
            S.append(0)
            row_id.append(rid)

            D[U[col]] = idx
            U[col] = idx
            S[col] += 1
            nodes.append(idx)

        k = len(nodes)
        for i, node in enumerate(nodes):
            L[node] = nodes[(i - 1) % k]
            R[node] = nodes[(i + 1) % k]

    for eid, (u, v) in enumerate(edges):
        if eid in forced:
            colors = (forced[eid],)
        else:
            colors = (0, 1, 2)

        for color in colors:
            add_row(
                eid * 3 + color,
                (
                    eid,
                    m + 3 * u + color,
                    m + 3 * v + color,
                ),
            )

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

    chosen = []

    def search():
        if R[0] == 0:
            return True

        col = R[0]
        best = col
        best_size = S[col]
        col = R[col]

        while col != 0:
            if S[col] < best_size:
                best = col
                best_size = S[col]
                if best_size <= 1:
                    break
            col = R[col]

        if best_size == 0:
            return False

        cover(best)
        r = D[best]

        while r != best:
            chosen.append(row_id[r])

            j = R[r]
            while j != r:
                cover(C[j])
                j = R[j]

            if search():
                return True

            j = L[r]
            while j != r:
                uncover(C[j])
                j = L[j]

            chosen.pop()
            r = D[r]

        uncover(best)
        return False

    if not search():
        print("NO")
        return

    answer = [0] * m
    for rid in chosen:
        eid, color = divmod(rid, 3)
        answer[eid] = color + 1

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()