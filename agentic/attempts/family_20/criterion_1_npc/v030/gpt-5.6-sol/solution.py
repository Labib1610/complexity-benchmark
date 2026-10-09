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

    if any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # A cubic graph containing a bridge cannot have a 3-edge-coloring.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def dfs_bridge(v, parent_edge):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1

        for eid in adj[v]:
            if eid == parent_edge:
                continue
            a, b = edges[eid]
            to = b if a == v else a
            if tin[to] == -1:
                dfs_bridge(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True
            else:
                low[v] = min(low[v], tin[to])

    for start in range(n):
        if tin[start] == -1:
            dfs_bridge(start, -1)

    if has_bridge:
        print("NO")
        return

    # Split into connected components and test bipartiteness.
    component_vertices = []
    component_bipartite = []
    side = [-1] * n

    for start in range(n):
        if side[start] != -1:
            continue

        queue = [start]
        side[start] = 0
        vertices = []
        bipartite = True

        for v in queue:
            vertices.append(v)
            for eid in adj[v]:
                a, b = edges[eid]
                to = b if a == v else a
                if side[to] == -1:
                    side[to] = side[v] ^ 1
                    queue.append(to)
                elif side[to] == side[v]:
                    bipartite = False

        component_vertices.append(vertices)
        component_bipartite.append(bipartite)

    answer = [0] * m
    used_mask = [0] * n

    # Color bipartite cubic components by extracting one perfect matching.
    for vertices, bipartite in zip(component_vertices, component_bipartite):
        if not bipartite:
            continue

        left = [v for v in vertices if side[v] == 0]
        match_left = [-1] * n
        match_right = [-1] * n

        def augment(v, seen):
            for eid in adj[v]:
                a, b = edges[eid]
                to = b if a == v else a
                if seen[to]:
                    continue
                seen[to] = True

                old_eid = match_right[to]
                if old_eid == -1:
                    match_left[v] = eid
                    match_right[to] = eid
                    return True

                x, y = edges[old_eid]
                old_left = x if side[x] == 0 else y
                if augment(old_left, seen):
                    match_left[v] = eid
                    match_right[to] = eid
                    return True
            return False

        for v in left:
            seen = [False] * n
            if not augment(v, seen):
                print("NO")
                return

        for v in left:
            eid = match_left[v]
            answer[eid] = 1

        # The remaining edges form disjoint even cycles.
        for start_eid in range(m):
            if answer[start_eid] != 0:
                continue
            u, v = edges[start_eid]
            if side[u] == -1 or not bipartite:
                continue
            if u not in vertices and v not in vertices:
                continue

            answer[start_eid] = 2
            queue = [start_eid]
            for eid in queue:
                color = answer[eid]
                opposite = 5 - color  # 2 <-> 3
                a, b = edges[eid]
                for x in (a, b):
                    for ne in adj[x]:
                        if ne == eid or answer[ne] == 1:
                            continue
                        if answer[ne] == 0:
                            answer[ne] = opposite
                            queue.append(ne)
                        elif answer[ne] != opposite:
                            print("NO")
                            return

        for v in vertices:
            used_mask[v] = 7

    FULL = 7
    trail = []

    def assign_and_propagate(initial_edge, initial_color):
        pending = [(initial_edge, initial_color)]

        while pending:
            eid, color = pending.pop()

            if answer[eid]:
                if answer[eid] != color:
                    return False
                continue

            bit = 1 << (color - 1)
            u, v = edges[eid]

            if (used_mask[u] & bit) or (used_mask[v] & bit):
                return False

            answer[eid] = color
            used_mask[u] |= bit
            used_mask[v] |= bit
            trail.append(eid)

            for x in (u, v):
                for ne in adj[x]:
                    if answer[ne]:
                        continue
                    a, b = edges[ne]
                    available = FULL & ~(used_mask[a] | used_mask[b])
                    if available == 0:
                        return False
                    if available & (available - 1) == 0:
                        forced_color = available.bit_length()
                        pending.append((ne, forced_color))

        return True

    def rollback(mark):
        while len(trail) > mark:
            eid = trail.pop()
            color = answer[eid]
            bit = 1 << (color - 1)
            u, v = edges[eid]
            used_mask[u] ^= bit
            used_mask[v] ^= bit
            answer[eid] = 0

    # Break color symmetry in every non-bipartite component.
    for vertices, bipartite in zip(component_vertices, component_bipartite):
        if bipartite:
            continue

        root = vertices[0]
        root_edges = adj[root]
        for i, eid in enumerate(root_edges):
            mark = len(trail)
            if not assign_and_propagate(eid, i + 1):
                rollback(mark)
                print("NO")
                return

    def search():
        best_edge = -1
        best_domain = 4
        best_score = -1
        best_available = 0

        for eid in range(m):
            if answer[eid]:
                continue

            u, v = edges[eid]
            available = FULL & ~(used_mask[u] | used_mask[v])
            count = available.bit_count()

            if count == 0:
                return False

            score = used_mask[u].bit_count() + used_mask[v].bit_count()
            if count < best_domain or (count == best_domain and score > best_score):
                best_edge = eid
                best_domain = count
                best_score = score
                best_available = available

        if best_edge == -1:
            return True

        available = best_available
        while available:
            bit = available & -available
            available -= bit
            color = bit.bit_length()
            mark = len(trail)

            if assign_and_propagate(best_edge, color) and search():
                return True

            rollback(mark)

        return False

    if not search():
        print("NO")
        return

    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()