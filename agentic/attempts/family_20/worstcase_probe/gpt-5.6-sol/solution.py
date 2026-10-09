import sys
from collections import deque
from itertools import permutations

sys.setrecursionlimit(100000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    if m != 3 * n // 2 or len(data) != 2 + 2 * m:
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

    # Find connected components, test bipartiteness, and retain roots.
    side = [-1] * n
    components = []
    all_bipartite = True

    for start in range(n):
        if side[start] != -1:
            continue
        side[start] = 0
        q = deque([start])
        comp = []
        bip = True

        while q:
            u = q.popleft()
            comp.append(u)
            for v, _ in adj[u]:
                if side[v] == -1:
                    side[v] = side[u] ^ 1
                    q.append(v)
                elif side[v] == side[u]:
                    bip = False

        components.append(comp)
        if not bip:
            all_bipartite = False

    # A bridge in a cubic graph makes a 3-edge-coloring impossible.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def bridge_dfs(u, parent_edge):
        nonlocal timer, has_bridge
        tin[u] = low[u] = timer
        timer += 1

        for v, eid in adj[u]:
            if eid == parent_edge:
                continue
            if tin[v] == -1:
                bridge_dfs(v, eid)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    has_bridge = True
            else:
                low[u] = min(low[u], tin[v])

    for v in range(n):
        if tin[v] == -1:
            bridge_dfs(v, -1)

    if has_bridge:
        print("NO")
        return

    # Every regular bipartite graph is 3-edge-colorable.
    if all_bipartite:
        left = [v for v in range(n) if side[v] == 0]
        pair_u = [-1] * n
        pair_v = [-1] * n
        pair_edge = [-1] * n
        dist = [-1] * n

        def hk_bfs():
            q = deque()
            found = False
            for u in left:
                if pair_u[u] == -1:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = -1

            while q:
                u = q.popleft()
                for v, _ in adj[u]:
                    pu = pair_v[v]
                    if pu == -1:
                        found = True
                    elif dist[pu] == -1:
                        dist[pu] = dist[u] + 1
                        q.append(pu)
            return found

        def hk_dfs(u):
            for v, eid in adj[u]:
                pu = pair_v[v]
                if pu == -1 or (dist[pu] == dist[u] + 1 and hk_dfs(pu)):
                    pair_u[u] = v
                    pair_v[v] = u
                    pair_edge[u] = eid
                    return True
            dist[u] = -1
            return False

        matching_size = 0
        while hk_bfs():
            for u in left:
                if pair_u[u] == -1 and hk_dfs(u):
                    matching_size += 1

        if matching_size * 2 != n:
            print("NO")
            return

        answer = [0] * m
        matched = [False] * m
        for u in left:
            eid = pair_edge[u]
            answer[eid] = 1
            matched[eid] = True

        residual = [[] for _ in range(n)]
        for eid, (u, v) in enumerate(edges):
            if not matched[eid]:
                residual[u].append(eid)
                residual[v].append(eid)

        for eid in range(m):
            if matched[eid] or answer[eid] != 0:
                continue

            answer[eid] = 2
            u, v = edges[eid]
            previous = eid
            vertex = v
            color = 3

            while True:
                e0, e1 = residual[vertex]
                nxt = e1 if e0 == previous else e0

                if nxt == eid:
                    if color != 2:
                        print("NO")
                        return
                    break

                if answer[nxt] != 0 and answer[nxt] != color:
                    print("NO")
                    return

                answer[nxt] = color
                a, b = edges[nxt]
                vertex = b if a == vertex else a
                previous = nxt
                color = 5 - color

        print("YES")
        print(*answer)
        return

    # General cubic graph: exact CSP solver with generalized arc consistency
    # on each degree-three all-different constraint.
    color_perms = list(permutations((1, 2, 4)))
    gac = [[[None] * 8 for _ in range(8)] for __ in range(8)]

    for a in range(1, 8):
        for b in range(1, 8):
            for c in range(1, 8):
                ua = ub = uc = 0
                valid = False
                for x, y, z in color_perms:
                    if (a & x) and (b & y) and (c & z):
                        valid = True
                        ua |= x
                        ub |= y
                        uc |= z
                if valid:
                    gac[a][b][c] = (ua, ub, uc)

    domains = [7] * m
    buckets = [set() for _ in range(8)]
    buckets[7] = set(range(m))
    trail = []

    def change_domain(eid, new_mask):
        old_mask = domains[eid]
        if old_mask == new_mask:
            return
        trail.append((eid, old_mask))
        buckets[old_mask].remove(eid)
        buckets[new_mask].add(eid)
        domains[eid] = new_mask

    def propagate(initial_vertices):
        queue = list(initial_vertices)
        qi = 0

        while qi < len(queue):
            v = queue[qi]
            qi += 1

            e0 = adj[v][0][1]
            e1 = adj[v][1][1]
            e2 = adj[v][2][1]

            result = gac[domains[e0]][domains[e1]][domains[e2]]
            if result is None:
                return False

            for eid, new_mask in ((e0, result[0]), (e1, result[1]), (e2, result[2])):
                if new_mask != domains[eid]:
                    change_domain(eid, new_mask)
                    a, b = edges[eid]
                    queue.append(a)
                    queue.append(b)

        return True

    def rollback(checkpoint):
        while len(trail) > checkpoint:
            eid, old_mask = trail.pop()
            current = domains[eid]
            buckets[current].remove(eid)
            buckets[old_mask].add(eid)
            domains[eid] = old_mask

    # Fix the global permutation of the three colors in each component.
    initial_vertices = []
    for comp in components:
        root = comp[0]
        for i, (_, eid) in enumerate(adj[root]):
            bit = 1 << i
            if not (domains[eid] & bit):
                print("NO")
                return
            change_domain(eid, bit)
            u, v = edges[eid]
            initial_vertices.append(u)
            initial_vertices.append(v)

    if not propagate(initial_vertices):
        print("NO")
        return

    def choose_edge():
        # Prefer binary choices.
        best_e = -1
        best_score = 10**9

        for mask in (3, 5, 6):
            for eid in buckets[mask]:
                u, v = edges[eid]
                score = 0
                for _, x in adj[u]:
                    score += domains[x].bit_count()
                for _, x in adj[v]:
                    score += domains[x].bit_count()
                if score < best_score:
                    best_score = score
                    best_e = eid
                    if score <= 8:
                        return best_e

        if best_e != -1:
            return best_e

        for mask in (7,):
            if buckets[mask]:
                return next(iter(buckets[mask]))

        return -1

    def search():
        eid = choose_edge()
        if eid == -1:
            return True

        mask = domains[eid]
        u, v = edges[eid]
        bit = 1

        while bit <= 4:
            if mask & bit:
                checkpoint = len(trail)
                change_domain(eid, bit)
                if propagate((u, v)) and search():
                    return True
                rollback(checkpoint)
            bit <<= 1

        return False

    if not search():
        print("NO")
        return

    answer = []
    for mask in domains:
        if mask == 1:
            answer.append(1)
        elif mask == 2:
            answer.append(2)
        elif mask == 4:
            answer.append(3)
        else:
            print("NO")
            return

    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()