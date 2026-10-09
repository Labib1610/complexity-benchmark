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

    if any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # Any bridge makes a cubic graph impossible to 3-edge-color.
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

    for s in range(n):
        if tin[s] == -1:
            bridge_dfs(s, -1)

    if has_bridge:
        print("NO")
        return

    # Find connected components and test which are bipartite.
    side = [-1] * n
    components = []
    bipartite_component = []

    for start in range(n):
        if side[start] != -1:
            continue

        q = deque([start])
        side[start] = 0
        comp = []
        bip = True

        while q:
            v = q.popleft()
            comp.append(v)
            for eid in adj[v]:
                a, b = edges[eid]
                to = b if a == v else a
                if side[to] == -1:
                    side[to] = side[v] ^ 1
                    q.append(to)
                elif side[to] == side[v]:
                    bip = False

        components.append(comp)
        bipartite_component.append(bip)

    answer = [-1] * m

    # Bipartite cubic components can be colored by repeatedly taking
    # perfect matchings.
    def extract_perfect_matching(comp, color):
        left = [v for v in comp if side[v] == 0]
        pair_left = [-1] * n
        pair_right = [-1] * n
        pair_edge = [-1] * n
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
                    if answer[eid] != -1:
                        continue
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
                if answer[eid] != -1:
                    continue
                a, b = edges[eid]
                v = b if a == u else a
                pu = pair_right[v]
                if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                    pair_left[u] = v
                    pair_right[v] = u
                    pair_edge[u] = eid
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
            answer[pair_edge[u]] = color
        return True

    non_bip_components = []

    for comp, bip in zip(components, bipartite_component):
        if bip:
            if not extract_perfect_matching(comp, 1):
                print("NO")
                return
            if not extract_perfect_matching(comp, 2):
                print("NO")
                return
            for v in comp:
                for eid in adj[v]:
                    if answer[eid] == -1:
                        answer[eid] = 3
        else:
            non_bip_components.append(comp)

    if not non_bip_components:
        print("YES")
        print(*answer)
        return

    # Exact constraint search for non-bipartite components.
    # Domain bits: color 1 -> 1, color 2 -> 2, color 3 -> 4.
    domains = [7] * m
    for eid, color in enumerate(answer):
        if color != -1:
            domains[eid] = 1 << (color - 1)

    permutations = (
        (1, 2, 4), (1, 4, 2),
        (2, 1, 4), (2, 4, 1),
        (4, 1, 2), (4, 2, 1)
    )

    # Color names may be permuted independently in every component.
    for comp in non_bip_components:
        v = comp[0]
        domains[adj[v][0]] = 1
        domains[adj[v][1]] = 2
        domains[adj[v][2]] = 4

    trail = []

    def propagate(initial_vertices):
        q = deque(initial_vertices)
        in_queue = [False] * n
        for v in initial_vertices:
            in_queue[v] = True

        while q:
            v = q.popleft()
            in_queue[v] = False
            e0, e1, e2 = adj[v]
            d0, d1, d2 = domains[e0], domains[e1], domains[e2]

            valid = []
            for perm in permutations:
                if (d0 & perm[0]) and (d1 & perm[1]) and (d2 & perm[2]):
                    valid.append(perm)

            if not valid:
                return False

            new_masks = [0, 0, 0]
            for perm in valid:
                new_masks[0] |= perm[0]
                new_masks[1] |= perm[1]
                new_masks[2] |= perm[2]

            for eid, new_domain in zip((e0, e1, e2), new_masks):
                old = domains[eid]
                if new_domain != old:
                    trail.append((eid, old))
                    domains[eid] = new_domain
                    a, b = edges[eid]
                    if not in_queue[a]:
                        in_queue[a] = True
                        q.append(a)
                    if not in_queue[b]:
                        in_queue[b] = True
                        q.append(b)

        return True

    if not propagate(range(n)):
        print("NO")
        return

    def valid_patterns(v):
        e0, e1, e2 = adj[v]
        d0, d1, d2 = domains[e0], domains[e1], domains[e2]
        return [
            perm for perm in permutations
            if (d0 & perm[0]) and (d1 & perm[1]) and (d2 & perm[2])
        ]

    def search():
        best_v = -1
        best_patterns = None
        best_count = 7
        best_domain_sum = 100

        for comp in non_bip_components:
            for v in comp:
                pats = valid_patterns(v)
                count = len(pats)
                if count == 0:
                    return False
                if count > 1:
                    e0, e1, e2 = adj[v]
                    domain_sum = (
                        domains[e0].bit_count()
                        + domains[e1].bit_count()
                        + domains[e2].bit_count()
                    )
                    if (count < best_count or
                            (count == best_count and domain_sum < best_domain_sum)):
                        best_v = v
                        best_patterns = pats
                        best_count = count
                        best_domain_sum = domain_sum

        if best_v == -1:
            return True

        vertex_edges = adj[best_v]

        for perm in best_patterns:
            checkpoint = len(trail)
            changed_vertices = []

            consistent = True
            for eid, value in zip(vertex_edges, perm):
                if not (domains[eid] & value):
                    consistent = False
                    break
                if domains[eid] != value:
                    trail.append((eid, domains[eid]))
                    domains[eid] = value
                    a, b = edges[eid]
                    changed_vertices.append(a)
                    changed_vertices.append(b)

            if consistent and propagate(changed_vertices) and search():
                return True

            while len(trail) > checkpoint:
                eid, old_domain = trail.pop()
                domains[eid] = old_domain

        return False

    if not search():
        print("NO")
        return

    bit_to_color = {1: 1, 2: 2, 4: 3}
    result = []
    for domain in domains:
        if domain not in bit_to_color:
            print("NO")
            return
        result.append(bit_to_color[domain])

    print("YES")
    print(*result)

if __name__ == "__main__":
    main()