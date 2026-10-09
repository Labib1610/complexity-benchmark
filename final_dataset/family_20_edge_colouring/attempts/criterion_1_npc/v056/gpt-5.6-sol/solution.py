import sys

sys.setrecursionlimit(10000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)

    edges = []
    adj = [[] for _ in range(n)]

    for eid in range(m):
        u = next(it) - 1
        v = next(it) - 1
        edges.append((u, v))
        adj[u].append(eid)
        adj[v].append(eid)

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
            a, b = edges[eid]
            to = b if a == v else a

            if tin[to] == -1:
                bridge_dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True
            else:
                low[v] = min(low[v], tin[to])

    for v in range(n):
        if tin[v] == -1:
            bridge_dfs(v, -1)

    if has_bridge:
        print("NO")
        return

    # Find connected components and test bipartiteness.
    side = [-1] * n
    components = []

    for start in range(n):
        if side[start] != -1:
            continue

        side[start] = 0
        stack = [start]
        vertices = []
        edge_set = set()
        bipartite = True

        while stack:
            v = stack.pop()
            vertices.append(v)

            for eid in adj[v]:
                edge_set.add(eid)
                a, b = edges[eid]
                to = b if a == v else a

                if side[to] == -1:
                    side[to] = side[v] ^ 1
                    stack.append(to)
                elif side[to] == side[v]:
                    bipartite = False

        components.append((vertices, list(edge_set), bipartite))

    # Colors are represented internally by bits 1, 2, 4.
    color = [0] * m

    def color_bipartite(vertices, component_edges):
        left = [v for v in vertices if side[v] == 0]
        pair_right = [-1] * n
        match_edge_left = [-1] * n
        seen = [0] * n
        stamp = 0

        def augment(u):
            nonlocal stamp
            for eid in adj[u]:
                a, b = edges[eid]
                r = b if a == u else a
                if side[r] != 1 or seen[r] == stamp:
                    continue

                seen[r] = stamp
                old_u = pair_right[r]
                if old_u == -1 or augment(old_u):
                    pair_right[r] = u
                    match_edge_left[u] = eid
                    return True
            return False

        for u in left:
            stamp += 1
            if not augment(u):
                return False

        for u in left:
            eid = match_edge_left[u]
            if eid < 0:
                return False
            color[eid] = 1

        # The remaining edges form disjoint even cycles.
        for start_eid in component_edges:
            if color[start_eid] != 0:
                continue

            u, v = edges[start_eid]
            current_edge = start_eid
            current_vertex = v
            current_color = 2

            while True:
                color[current_edge] = current_color
                next_color = 4 if current_color == 2 else 2
                next_edge = -1

                for eid in adj[current_vertex]:
                    if eid != current_edge and color[eid] != 1:
                        next_edge = eid
                        break

                if next_edge == -1:
                    return False

                if color[next_edge] != 0:
                    if color[next_edge] != next_color:
                        return False
                    break

                a, b = edges[next_edge]
                next_vertex = b if a == current_vertex else a
                current_edge = next_edge
                current_vertex = next_vertex
                current_color = next_color

        return True

    used = [0] * n

    def color_non_bipartite(vertices, component_edges):
        trail = []

        def rollback(mark):
            while len(trail) > mark:
                eid = trail.pop()
                c = color[eid]
                u, v = edges[eid]
                used[u] ^= c
                used[v] ^= c
                color[eid] = 0

        def assign(initial_edge, initial_color):
            queue = [(initial_edge, initial_color)]
            qpos = 0

            while qpos < len(queue):
                eid, c = queue[qpos]
                qpos += 1

                if color[eid] != 0:
                    if color[eid] != c:
                        return False
                    continue

                u, v = edges[eid]
                if (used[u] & c) or (used[v] & c):
                    return False

                color[eid] = c
                used[u] |= c
                used[v] |= c
                trail.append(eid)

                for x in (u, v):
                    if used[x].bit_count() == 2:
                        missing = 7 ^ used[x]
                        forced = -1
                        for ie in adj[x]:
                            if color[ie] == 0:
                                if forced != -1:
                                    return False
                                forced = ie
                        if forced != -1:
                            queue.append((forced, missing))

                    for ie in adj[x]:
                        if color[ie] != 0:
                            continue
                        a, b = edges[ie]
                        domain = 7 & ~(used[a] | used[b])
                        if domain == 0:
                            return False
                        if domain & (domain - 1) == 0:
                            queue.append((ie, domain))

            return True

        def dfs():
            best_edge = -1
            best_domain = 0
            best_size = 4

            for eid in component_edges:
                if color[eid] != 0:
                    continue
                u, v = edges[eid]
                domain = 7 & ~(used[u] | used[v])
                size = domain.bit_count()

                if size == 0:
                    return False
                if size < best_size:
                    best_size = size
                    best_edge = eid
                    best_domain = domain
                    if size == 1:
                        break

            if best_edge == -1:
                return True

            domain = best_domain
            while domain:
                c = domain & -domain
                domain -= c
                mark = len(trail)

                if assign(best_edge, c) and dfs():
                    return True

                rollback(mark)

            return False

        # Remove global color symmetry by fixing the colors at one vertex.
        root = vertices[0]
        root_edges = adj[root]
        mark = len(trail)

        for eid, c in zip(root_edges, (1, 2, 4)):
            if not assign(eid, c):
                rollback(mark)
                return False

        if dfs():
            return True

        rollback(mark)
        return False

    # Bipartite cubic components can be colored in polynomial time.
    # Other components are solved by exact constraint propagation and search.
    for vertices, component_edges, bipartite in components:
        if bipartite:
            if not color_bipartite(vertices, component_edges):
                print("NO")
                return
        else:
            if not color_non_bipartite(vertices, component_edges):
                print("NO")
                return

    answer = []
    for c in color:
        if c == 1:
            answer.append("1")
        elif c == 2:
            answer.append("2")
        elif c == 4:
            answer.append("3")
        else:
            print("NO")
            return

    print("YES")
    print(" ".join(answer))

if __name__ == "__main__":
    main()