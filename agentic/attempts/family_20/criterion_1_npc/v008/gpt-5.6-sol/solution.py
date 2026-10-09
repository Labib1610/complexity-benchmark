import sys
from collections import deque

sys.setrecursionlimit(1000000)


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

    # Find connected components, bipartitions, and detect bridges.
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

    for s in range(n):
        if tin[s] == -1:
            dfs_bridge(s, -1)

    if has_bridge:
        print("NO")
        return

    comp_id = [-1] * n
    bip_color = [-1] * n
    components = []

    for s in range(n):
        if comp_id[s] != -1:
            continue

        cid = len(components)
        vertices = []
        edge_set = set()
        is_bipartite = True

        q = deque([s])
        comp_id[s] = cid
        bip_color[s] = 0

        while q:
            v = q.popleft()
            vertices.append(v)

            for eid in adj[v]:
                edge_set.add(eid)
                a, b = edges[eid]
                to = b if a == v else a

                if comp_id[to] == -1:
                    comp_id[to] = cid
                    bip_color[to] = bip_color[v] ^ 1
                    q.append(to)
                elif bip_color[to] == bip_color[v]:
                    is_bipartite = False

        components.append((vertices, list(edge_set), is_bipartite))

    selected = [False] * m

    def bipartite_perfect_matching(vertices):
        left = [v for v in vertices if bip_color[v] == 0]
        pair_left = [-1] * n
        pair_right = [-1] * n
        match_edge = [-1] * n
        dist = [-1] * n

        def bfs():
            q = deque()
            found = False
            for u in left:
                if pair_left[u] == -1:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = -1

            while q:
                u = q.popleft()
                for eid in adj[u]:
                    a, b = edges[eid]
                    v = b if a == u else a
                    pu = pair_right[v]
                    if pu == -1:
                        found = True
                    elif dist[pu] == -1:
                        dist[pu] = dist[u] + 1
                        q.append(pu)
            return found

        def dfs(u):
            for eid in adj[u]:
                a, b = edges[eid]
                v = b if a == u else a
                pu = pair_right[v]

                if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                    pair_left[u] = v
                    pair_right[v] = u
                    match_edge[u] = eid
                    return True

            dist[u] = -1
            return False

        matched = 0
        while bfs():
            for u in left:
                if pair_left[u] == -1 and dfs(u):
                    matched += 1

        if matched != len(left):
            return False

        for u in left:
            selected[match_edge[u]] = True
        return True

    def solve_non_bipartite(vertices, component_edges):
        status = [-1] * m  # -1 unknown, 0 outside matching, 1 in matching
        trail = []

        parent = list(range(n))
        size = [1] * n
        parity = [0] * n
        dsu_trail = []

        def find(x):
            px = 0
            while parent[x] != x:
                px ^= parity[x]
                x = parent[x]
            return x, px

        def unite_opposite(a, b):
            ra, pa = find(a)
            rb, pb = find(b)

            if ra == rb:
                return (pa ^ pb) == 1

            if size[ra] < size[rb]:
                ra, rb = rb, ra
                pa, pb = pb, pa

            dsu_trail.append((rb, ra, size[ra]))
            parent[rb] = ra
            parity[rb] = pa ^ pb ^ 1
            size[ra] += size[rb]
            return True

        def rollback(status_checkpoint, dsu_checkpoint):
            while len(trail) > status_checkpoint:
                eid = trail.pop()
                status[eid] = -1

            while len(dsu_trail) > dsu_checkpoint:
                child, root, old_size = dsu_trail.pop()
                parent[child] = child
                parity[child] = 0
                size[root] = old_size

        def propagate(initial_eid, initial_value):
            pending = [(initial_eid, initial_value)]
            vertex_queue = deque()

            while pending or vertex_queue:
                while pending:
                    eid, value = pending.pop()
                    old = status[eid]

                    if old != -1:
                        if old != value:
                            return False
                        continue

                    status[eid] = value
                    trail.append(eid)

                    u, v = edges[eid]
                    if value == 0 and not unite_opposite(u, v):
                        return False

                    vertex_queue.append(u)
                    vertex_queue.append(v)

                if not vertex_queue:
                    continue

                v = vertex_queue.popleft()
                one_count = 0
                unknown = []

                for eid in adj[v]:
                    st = status[eid]
                    if st == 1:
                        one_count += 1
                    elif st == -1:
                        unknown.append(eid)

                if one_count > 1:
                    return False

                if one_count == 1:
                    for eid in unknown:
                        pending.append((eid, 0))
                else:
                    if not unknown:
                        return False
                    if len(unknown) == 1:
                        pending.append((unknown[0], 1))

            return True

        if not component_edges:
            return False

        if not propagate(component_edges[0], 1):
            return False

        def search():
            branch_vertex = -1
            branch_edges = None
            best_count = 4

            for v in vertices:
                has_one = False
                unknown = []

                for eid in adj[v]:
                    st = status[eid]
                    if st == 1:
                        has_one = True
                        break
                    if st == -1:
                        unknown.append(eid)

                if has_one:
                    continue

                if not unknown:
                    return False

                if len(unknown) < best_count:
                    best_count = len(unknown)
                    branch_vertex = v
                    branch_edges = unknown
                    if best_count == 2:
                        break

            if branch_vertex == -1:
                return True

            candidates = branch_edges[:]

            # Prefer choices whose rejected edges connect already-related
            # parity components, as they tend to propagate more strongly.
            def candidate_score(chosen):
                score = 0
                for eid in adj[branch_vertex]:
                    if eid == chosen or status[eid] != -1:
                        continue
                    a, b = edges[eid]
                    if find(a)[0] == find(b)[0]:
                        score += 1
                return -score

            candidates.sort(key=candidate_score)

            for eid in candidates:
                status_checkpoint = len(trail)
                dsu_checkpoint = len(dsu_trail)

                if propagate(eid, 1) and search():
                    return True

                rollback(status_checkpoint, dsu_checkpoint)

            return False

        if not search():
            return False

        for eid in component_edges:
            selected[eid] = (status[eid] == 1)
        return True

    for vertices, component_edges, is_bipartite in components:
        if is_bipartite:
            if not bipartite_perfect_matching(vertices):
                print("NO")
                return
        else:
            if not solve_non_bipartite(vertices, component_edges):
                print("NO")
                return

    answer = [0] * m
    for eid in range(m):
        if selected[eid]:
            answer[eid] = 1

    # The non-matching edges form disjoint even cycles; color each alternately.
    for start in range(m):
        if selected[start] or answer[start] != 0:
            continue

        u, _ = edges[start]
        previous_vertex = u
        current_edge = start
        color = 2

        while answer[current_edge] == 0:
            answer[current_edge] = color
            a, b = edges[current_edge]
            next_vertex = b if a == previous_vertex else a

            next_edge = -1
            for eid in adj[next_vertex]:
                if eid != current_edge and not selected[eid]:
                    next_edge = eid
                    break

            if next_edge == -1:
                print("NO")
                return

            previous_vertex = next_vertex
            current_edge = next_edge
            color = 5 - color

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()