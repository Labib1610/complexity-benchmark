import sys

sys.setrecursionlimit(1000000)


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

    # A bridge makes a 3-edge-coloring of a cubic graph impossible.
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

    for start in range(n):
        if tin[start] == -1:
            bridge_dfs(start, -1)

    if has_bridge:
        print("NO")
        return

    # Find connected components and test each for bipartiteness.
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
            for eid in adj[v]:
                a, b = edges[eid]
                to = b if a == v else a
                if side[to] == -1:
                    side[to] = side[v] ^ 1
                    stack.append(to)
                elif side[to] == side[v]:
                    bipartite = False

        components.append((vertices, bipartite))

    color = [0] * m

    # Bipartite cubic components can be decomposed into three perfect matchings.
    def color_bipartite_component(vertices):
        left = [v for v in vertices if side[v] == 0]

        for c in range(1, 4):
            mate_right = [-1] * n
            chosen_edge = [-1] * n
            seen = [0] * n
            stamp = 0

            def augment(u):
                nonlocal stamp
                for eid in adj[u]:
                    if color[eid] != 0:
                        continue
                    a, b = edges[eid]
                    v = b if a == u else a
                    if seen[v] == stamp:
                        continue
                    seen[v] = stamp

                    old_u = mate_right[v]
                    if old_u == -1 or augment(old_u):
                        mate_right[v] = u
                        chosen_edge[u] = eid
                        return True
                return False

            for u in left:
                stamp += 1
                if not augment(u):
                    return False

            for u in left:
                eid = chosen_edge[u]
                if eid == -1:
                    return False
                color[eid] = c

        return True

    non_bipartite_components = []

    for vertices, bipartite in components:
        if bipartite:
            if not color_bipartite_component(vertices):
                print("NO")
                return
        else:
            non_bipartite_components.append(vertices)

    used = [0] * n
    for eid, c in enumerate(color):
        if c:
            bit = 1 << (c - 1)
            u, v = edges[eid]
            if (used[u] & bit) or (used[v] & bit):
                print("NO")
                return
            used[u] |= bit
            used[v] |= bit

    trail = []

    def rollback(mark):
        while len(trail) > mark:
            eid = trail.pop()
            c = color[eid]
            bit = 1 << (c - 1)
            u, v = edges[eid]
            used[u] &= ~bit
            used[v] &= ~bit
            color[eid] = 0

    def propagate(initial):
        queue = list(initial)
        head = 0

        while head < len(queue):
            eid, c = queue[head]
            head += 1

            if color[eid] != 0:
                if color[eid] != c:
                    return False
                continue

            bit = 1 << (c - 1)
            u, v = edges[eid]

            if (used[u] & bit) or (used[v] & bit):
                return False

            color[eid] = c
            used[u] |= bit
            used[v] |= bit
            trail.append(eid)

            for x in (u, v):
                for ne in adj[x]:
                    if color[ne] != 0:
                        continue

                    a, b = edges[ne]
                    allowed = 7 & ~(used[a] | used[b])

                    if allowed == 0:
                        return False
                    if allowed & (allowed - 1) == 0:
                        forced_color = allowed.bit_length()
                        queue.append((ne, forced_color))

        return True

    # Fix color symmetry independently in every non-bipartite component.
    for vertices in non_bipartite_components:
        root = vertices[0]
        root_edges = adj[root]
        if len(root_edges) != 3:
            print("NO")
            return

        if not propagate([
            (root_edges[0], 1),
            (root_edges[1], 2),
            (root_edges[2], 3)
        ]):
            print("NO")
            return

    def search():
        best_edge = -1
        best_allowed = 0
        best_size = 4
        best_score = -1

        for eid in range(m):
            if color[eid] != 0:
                continue

            u, v = edges[eid]
            allowed = 7 & ~(used[u] | used[v])
            size = allowed.bit_count()

            if size == 0:
                return False

            score = used[u].bit_count() + used[v].bit_count()

            if size < best_size or (size == best_size and score > best_score):
                best_size = size
                best_score = score
                best_edge = eid
                best_allowed = allowed

        if best_edge == -1:
            return True

        mask = best_allowed
        while mask:
            bit = mask & -mask
            mask -= bit
            c = bit.bit_length()

            mark = len(trail)
            if propagate([(best_edge, c)]) and search():
                return True
            rollback(mark)

        return False

    if not search():
        print("NO")
        return

    print("YES")
    print(*color)


if __name__ == "__main__":
    main()