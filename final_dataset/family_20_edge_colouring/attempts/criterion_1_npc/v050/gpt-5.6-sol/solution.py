import sys
from collections import deque
from itertools import permutations

sys.setrecursionlimit(100000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
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

    # A cubic graph with a bridge cannot have a proper 3-edge-coloring.
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

    # Find connected components and identify bipartite components.
    side = [-1] * n
    components = []
    component_is_bipartite = []

    for start in range(n):
        if side[start] != -1:
            continue

        q = deque([start])
        side[start] = 0
        vertices = []
        bipartite = True

        while q:
            v = q.popleft()
            vertices.append(v)
            for eid in adj[v]:
                a, b = edges[eid]
                to = b if a == v else a
                if side[to] == -1:
                    side[to] = side[v] ^ 1
                    q.append(to)
                elif side[to] == side[v]:
                    bipartite = False

        components.append(vertices)
        component_is_bipartite.append(bipartite)

    # domain bits: color 1 -> 1, color 2 -> 2, color 3 -> 4
    domains = [7] * m

    # Color bipartite cubic components in polynomial time:
    # one perfect matching gets color 1, remaining even cycles get colors 2 and 3.
    match_left = [-1] * n
    match_right = [-1] * n
    visit = [0] * n
    stamp = 0

    def augment(u):
        nonlocal stamp
        if visit[u] == stamp:
            return False
        visit[u] = stamp

        for eid in adj[u]:
            a, b = edges[eid]
            v = b if a == u else a
            if side[v] != 1:
                continue

            old_eid = match_right[v]
            if old_eid == -1:
                match_left[u] = eid
                match_right[v] = eid
                return True

            x, y = edges[old_eid]
            old_u = x if side[x] == 0 else y
            if augment(old_u):
                match_left[u] = eid
                match_right[v] = eid
                return True

        return False

    for comp, is_bip in zip(components, component_is_bipartite):
        if not is_bip:
            continue

        for u in comp:
            if side[u] == 0:
                stamp += 1
                if not augment(u):
                    print("NO")
                    return

        for u in comp:
            if side[u] == 0:
                domains[match_left[u]] = 1

        edge_queue = deque()
        for u in comp:
            for eid in adj[u]:
                if domains[eid] == 7:
                    domains[eid] = 2
                    edge_queue.append(eid)
                    break
            if edge_queue:
                break

        while edge_queue:
            eid = edge_queue.popleft()
            color = domains[eid]
            opposite = 4 if color == 2 else 2
            u, v = edges[eid]

            for x in (u, v):
                for other in adj[x]:
                    if other == eid or domains[other] == 1:
                        continue
                    if domains[other] == 7:
                        domains[other] = opposite
                        edge_queue.append(other)
                    elif domains[other] != opposite:
                        print("NO")
                        return

        # In case the component has multiple remaining cycles.
        for u in comp:
            for eid in adj[u]:
                if domains[eid] == 7:
                    domains[eid] = 2
                    edge_queue.append(eid)

                    while edge_queue:
                        cur = edge_queue.popleft()
                        color = domains[cur]
                        opposite = 4 if color == 2 else 2
                        a, b = edges[cur]

                        for x in (a, b):
                            for other in adj[x]:
                                if other == cur or domains[other] == 1:
                                    continue
                                if domains[other] == 7:
                                    domains[other] = opposite
                                    edge_queue.append(other)
                                elif domains[other] != opposite:
                                    print("NO")
                                    return

    # Fix color symmetry in each non-bipartite component.
    for comp, is_bip in zip(components, component_is_bipartite):
        if not is_bip:
            root = comp[0]
            domains[adj[root][0]] = 1
            domains[adj[root][1]] = 2
            domains[adj[root][2]] = 4

    # Precompute generalized arc-consistency transitions for a degree-3 vertex.
    support_table = [None] * 512
    color_permutations = list(permutations((1, 2, 4)))

    for d0 in range(1, 8):
        for d1 in range(1, 8):
            for d2 in range(1, 8):
                s0 = s1 = s2 = 0
                for c0, c1, c2 in color_permutations:
                    if (d0 & c0) and (d1 & c1) and (d2 & c2):
                        s0 |= c0
                        s1 |= c1
                        s2 |= c2
                if s0:
                    support_table[d0 | (d1 << 3) | (d2 << 6)] = (s0, s1, s2)

    trail = []

    def propagate(initial_vertices):
        q = deque(initial_vertices)

        while q:
            v = q.popleft()
            e0, e1, e2 = adj[v]
            d0, d1, d2 = domains[e0], domains[e1], domains[e2]
            supported = support_table[d0 | (d1 << 3) | (d2 << 6)]

            if supported is None:
                return False

            for eid, allowed in ((e0, supported[0]),
                                 (e1, supported[1]),
                                 (e2, supported[2])):
                new_domain = domains[eid] & allowed
                if new_domain == 0:
                    return False
                if new_domain != domains[eid]:
                    trail.append((eid, domains[eid]))
                    domains[eid] = new_domain
                    a, b = edges[eid]
                    q.append(a)
                    q.append(b)

        return True

    def solve():
        chosen = -1
        best_size = 4
        best_score = 10**9

        for eid, d in enumerate(domains):
            count = d.bit_count()
            if count <= 1:
                continue

            u, v = edges[eid]
            score = 0
            for x in adj[u]:
                score += domains[x].bit_count()
            for x in adj[v]:
                score += domains[x].bit_count()

            if count < best_size or (count == best_size and score < best_score):
                best_size = count
                best_score = score
                chosen = eid

        if chosen == -1:
            return True

        old_domain = domains[chosen]
        u, v = edges[chosen]
        bits = []
        x = old_domain
        while x:
            bit = x & -x
            bits.append(bit)
            x -= bit

        for bit in bits:
            checkpoint = len(trail)
            trail.append((chosen, domains[chosen]))
            domains[chosen] = bit

            if propagate((u, v)) and solve():
                return True

            while len(trail) > checkpoint:
                eid, old = trail.pop()
                domains[eid] = old

        return False

    if not propagate(range(n)) or not solve():
        print("NO")
        return

    answer = [d.bit_length() for d in domains]
    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()