import sys
from collections import deque
from itertools import permutations

sys.setrecursionlimit(100000)

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
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    if m * 2 != 3 * n or any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # A bridge in a cubic graph makes a 3-edge-coloring impossible.
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

    for s in range(n):
        if tin[s] == -1:
            bridge_dfs(s, -1)

    if has_bridge:
        print("NO")
        return

    components = []
    comp_id = [-1] * n
    bipartite = []
    side = [-1] * n

    for start in range(n):
        if comp_id[start] != -1:
            continue

        cid = len(components)
        vertices = []
        ok = True
        q = deque([start])
        comp_id[start] = cid
        side[start] = 0

        while q:
            v = q.popleft()
            vertices.append(v)
            for to, _ in adj[v]:
                if comp_id[to] == -1:
                    comp_id[to] = cid
                    side[to] = side[v] ^ 1
                    q.append(to)
                elif side[to] == side[v]:
                    ok = False

        components.append(vertices)
        bipartite.append(ok)

    answer = [-1] * m

    def color_bipartite_component(vertices):
        left = [v for v in vertices if side[v] == 0]
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
                for v, _ in adj[u]:
                    pu = pair_right[v]
                    if pu == -1:
                        found = True
                    elif dist[pu] == -1:
                        dist[pu] = dist[u] + 1
                        q.append(pu)
            return found

        def dfs(u):
            for v, eid in adj[u]:
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
            answer[pair_edge[u]] = 0

        component_edges = []
        for v in vertices:
            for _, eid in adj[v]:
                if edges[eid][0] == v:
                    component_edges.append(eid)

        for seed in component_edges:
            if answer[seed] != -1:
                continue

            answer[seed] = 1
            q = deque([seed])

            while q:
                eid = q.popleft()
                u, v = edges[eid]
                for x in (u, v):
                    other = -1
                    for _, ne in adj[x]:
                        if answer[ne] != 0 and ne != eid:
                            other = ne
                            break

                    needed = 3 - answer[eid]  # swaps 1 and 2
                    if answer[other] == -1:
                        answer[other] = needed
                        q.append(other)
                    elif answer[other] != needed:
                        return False

        return True

    perms = list(permutations((0, 1, 2)))
    full_domain = (1 << 6) - 1

    allowed = [[[0] * 8 for _ in range(3)]][0]
    for pos in range(3):
        for color_mask in range(8):
            mask = 0
            for state, perm in enumerate(perms):
                if color_mask & (1 << perm[pos]):
                    mask |= 1 << state
            allowed[pos][color_mask] = mask

    possible_colors = [[0] * 64 for _ in range(3)]
    for pos in range(3):
        for domain in range(64):
            cm = 0
            for state, perm in enumerate(perms):
                if domain & (1 << state):
                    cm |= 1 << perm[pos]
            possible_colors[pos][domain] = cm

    edge_pos = [[-1, -1] for _ in range(m)]
    for v in range(n):
        for pos, (_, eid) in enumerate(adj[v]):
            u, w = edges[eid]
            if v == u:
                edge_pos[eid][0] = pos
            else:
                edge_pos[eid][1] = pos

    def color_nonbipartite_component(vertices):
        domains = [0] * n
        for v in vertices:
            domains[v] = full_domain

        trail = []

        def propagate(initial):
            q = deque(initial)
            in_queue = set(initial)

            while q:
                v = q.popleft()
                in_queue.discard(v)

                for _, eid in adj[v]:
                    a, b = edges[eid]
                    pa, pb = edge_pos[eid]
                    da = domains[a]
                    db = domains[b]

                    common = (
                        possible_colors[pa][da]
                        & possible_colors[pb][db]
                    )
                    if common == 0:
                        return False

                    nda = da & allowed[pa][common]
                    ndb = db & allowed[pb][common]

                    if nda == 0 or ndb == 0:
                        return False

                    if nda != da:
                        trail.append((a, da))
                        domains[a] = nda
                        if a not in in_queue:
                            in_queue.add(a)
                            q.append(a)

                    if ndb != db:
                        trail.append((b, db))
                        domains[b] = ndb
                        if b not in in_queue:
                            in_queue.add(b)
                            q.append(b)

            return True

        root = vertices[0]
        domains[root] = 1  # Fix global color permutation symmetry.
        if not propagate([root]):
            return False

        def search():
            chosen = -1
            best_count = 7
            best_score = -1

            for v in vertices:
                count = domains[v].bit_count()
                if 1 < count < best_count:
                    chosen = v
                    best_count = count
                    best_score = 0
                elif count == best_count and count > 1:
                    score = 0
                    for to, _ in adj[v]:
                        score += 6 - domains[to].bit_count()
                    if score > best_score:
                        chosen = v
                        best_score = score

            if chosen == -1:
                return True

            candidates = domains[chosen]
            while candidates:
                bit = candidates & -candidates
                candidates -= bit
                checkpoint = len(trail)

                old = domains[chosen]
                trail.append((chosen, old))
                domains[chosen] = bit

                if propagate([chosen]) and search():
                    return True

                while len(trail) > checkpoint:
                    v, old_domain = trail.pop()
                    domains[v] = old_domain

            return False

        if not search():
            return False

        for v in vertices:
            state = domains[v].bit_length() - 1
            perm = perms[state]
            for pos, (_, eid) in enumerate(adj[v]):
                color = perm[pos]
                if answer[eid] == -1:
                    answer[eid] = color
                elif answer[eid] != color:
                    return False

        return True

    for cid, vertices in enumerate(components):
        if bipartite[cid]:
            if not color_bipartite_component(vertices):
                print("NO")
                return
        else:
            if not color_nonbipartite_component(vertices):
                print("NO")
                return

    for v in range(n):
        colors = {answer[eid] for _, eid in adj[v]}
        if colors != {0, 1, 2}:
            print("NO")
            return

    print("YES")
    print(*[c + 1 for c in answer])


if __name__ == "__main__":
    main()