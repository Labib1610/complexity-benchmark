import sys
sys.setrecursionlimit(20000)

from itertools import permutations

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    m = next(it)

    eu = [0] * m
    ev = [0] * m
    pos_u = [0] * m
    pos_v = [0] * m
    adj = [[] for _ in range(n)]

    for eid in range(m):
        u = next(it) - 1
        v = next(it) - 1
        eu[eid] = u
        ev[eid] = v
        pos_u[eid] = len(adj[u])
        pos_v[eid] = len(adj[v])
        adj[u].append(eid)
        adj[v].append(eid)

    # A cubic graph with a bridge cannot be 3-edge-colored.
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
            to = ev[eid] if eu[eid] == v else eu[eid]
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

    # Connected components and bipartiteness.
    side = [-1] * n
    components = []
    component_edges = []

    for start in range(n):
        if side[start] != -1:
            continue
        stack = [start]
        side[start] = 0
        verts = []
        edges_set = set()
        bip = True

        while stack:
            v = stack.pop()
            verts.append(v)
            for eid in adj[v]:
                edges_set.add(eid)
                to = ev[eid] if eu[eid] == v else eu[eid]
                if side[to] == -1:
                    side[to] = side[v] ^ 1
                    stack.append(to)
                elif side[to] == side[v]:
                    bip = False

        components.append((verts, bip))
        component_edges.append(list(edges_set))

    answer = [0] * m

    # Bipartite regular components can be decomposed into perfect matchings.
    def color_bipartite(verts, edges):
        left = [v for v in verts if side[v] == 0]

        for color in (1, 2):
            match_edge = [-1] * n
            seen = [0] * n
            stamp = 0

            def augment(v):
                nonlocal stamp
                for eid in adj[v]:
                    if answer[eid] != 0:
                        continue
                    to = ev[eid] if eu[eid] == v else eu[eid]
                    if seen[to] == stamp:
                        continue
                    seen[to] = stamp
                    old = match_edge[to]
                    if old == -1:
                        match_edge[to] = eid
                        return True
                    old_left = eu[old] if side[eu[old]] == 0 else ev[old]
                    if augment(old_left):
                        match_edge[to] = eid
                        return True
                return False

            for v in left:
                stamp += 1
                if not augment(v):
                    return False

            for r in verts:
                if side[r] == 1 and match_edge[r] != -1:
                    answer[match_edge[r]] = color

        for eid in edges:
            if answer[eid] == 0:
                answer[eid] = 3
        return True

    non_bip_components = []
    for idx, (verts, bip) in enumerate(components):
        if bip:
            if not color_bipartite(verts, component_edges[idx]):
                print("NO")
                return
        else:
            non_bip_components.append((verts, component_edges[idx]))

    perms = list(permutations((0, 1, 2)))
    full_domain = (1 << 6) - 1
    domains = [full_domain] * n

    perm_bits = [[[0] * 3 for _ in range(3)]][0]
    for coord in range(3):
        for color in range(3):
            mask = 0
            for p, perm in enumerate(perms):
                if perm[coord] == color:
                    mask |= 1 << p
            perm_bits[coord][color] = mask

    color_sets = [[0] * 64 for _ in range(3)]
    filter_masks = [[[0] * 64 for _ in range(8)] for _ in range(3)]

    for coord in range(3):
        for mask in range(64):
            colors = 0
            for p in range(6):
                if (mask >> p) & 1:
                    colors |= 1 << perms[p][coord]
            color_sets[coord][mask] = colors
        for allowed in range(8):
            keep = 0
            for p in range(6):
                if (allowed >> perms[p][coord]) & 1:
                    keep |= 1 << p
            for mask in range(64):
                filter_masks[coord][allowed][mask] = mask & keep

    def other_and_positions(v, eid):
        if eu[eid] == v:
            return ev[eid], pos_u[eid], pos_v[eid]
        return eu[eid], pos_v[eid], pos_u[eid]

    def solve_non_bipartite(verts, edges):
        for v in verts:
            domains[v] = full_domain

        trail = []

        def rollback(checkpoint):
            while len(trail) > checkpoint:
                v, old = trail.pop()
                domains[v] = old

        def propagate(initial):
            queue = list(initial)
            head = 0
            while head < len(queue):
                v = queue[head]
                head += 1
                dv = domains[v]

                for eid in adj[v]:
                    to, cv, ct = other_and_positions(v, eid)
                    allowed = color_sets[cv][dv]
                    old = domains[to]
                    new = filter_masks[ct][allowed][old]
                    if new != old:
                        if new == 0:
                            return False
                        trail.append((to, old))
                        domains[to] = new
                        queue.append(to)
            return True

        # Fix all global color symmetry at one vertex.
        root = verts[0]
        trail.append((root, domains[root]))
        domains[root] = 1
        if not propagate([root]):
            return False

        def solve_binary_domains():
            variables = []
            var_id = {}
            opts = []

            for v in verts:
                d = domains[v]
                if d.bit_count() == 2:
                    var_id[v] = len(variables)
                    variables.append(v)
                    values = [p for p in range(6) if (d >> p) & 1]
                    opts.append(values)

            k = len(variables)
            g = [[] for _ in range(2 * k)]
            rg = [[] for _ in range(2 * k)]

            def add_imp(a, b):
                g[a].append(b)
                rg[b].append(a)

            for eid in edges:
                u = eu[eid]
                v = ev[eid]
                cu = pos_u[eid]
                cv = pos_v[eid]
                iu = var_id.get(u, -1)
                iv = var_id.get(v, -1)

                if iu == -1:
                    pu = domains[u].bit_length() - 1
                if iv == -1:
                    pv = domains[v].bit_length() - 1

                if iu == -1 and iv == -1:
                    if perms[pu][cu] != perms[pv][cv]:
                        return False
                elif iu != -1 and iv == -1:
                    fixed = perms[pv][cv]
                    for a in range(2):
                        if perms[opts[iu][a]][cu] != fixed:
                            add_imp(2 * iu + a, 2 * iu + (1 - a))
                elif iu == -1 and iv != -1:
                    fixed = perms[pu][cu]
                    for b in range(2):
                        if perms[opts[iv][b]][cv] != fixed:
                            add_imp(2 * iv + b, 2 * iv + (1 - b))
                else:
                    for a in range(2):
                        color_u = perms[opts[iu][a]][cu]
                        for b in range(2):
                            if color_u != perms[opts[iv][b]][cv]:
                                add_imp(2 * iu + a, 2 * iv + (1 - b))
                                add_imp(2 * iv + b, 2 * iu + (1 - a))

            visited = [False] * (2 * k)
            order = []

            def dfs1(x):
                visited[x] = True
                for y in g[x]:
                    if not visited[y]:
                        dfs1(y)
                order.append(x)

            for x in range(2 * k):
                if not visited[x]:
                    dfs1(x)

            comp = [-1] * (2 * k)

            def dfs2(x, c):
                comp[x] = c
                for y in rg[x]:
                    if comp[y] == -1:
                        dfs2(y, c)

            c = 0
            for x in reversed(order):
                if comp[x] == -1:
                    dfs2(x, c)
                    c += 1

            for i in range(k):
                if comp[2 * i] == comp[2 * i + 1]:
                    return False

            for i, v in enumerate(variables):
                chosen = 1 if comp[2 * i + 1] > comp[2 * i] else 0
                domains[v] = 1 << opts[i][chosen]

            return True

        def search():
            chosen_v = -1
            chosen_size = 7

            for v in verts:
                size = domains[v].bit_count()
                if size > 2 and size < chosen_size:
                    chosen_size = size
                    chosen_v = v

            if chosen_v == -1:
                return solve_binary_domains()

            d = domains[chosen_v]
            best_a = 0
            best_score = 100

            for coord in range(3):
                for color in range(3):
                    a = d & perm_bits[coord][color]
                    b = d & ~perm_bits[coord][color]
                    if a and b:
                        score = max(a.bit_count(), b.bit_count())
                        if score < best_score:
                            best_score = score
                            best_a = a

            branches = (best_a, d ^ best_a)
            for branch in branches:
                checkpoint = len(trail)
                trail.append((chosen_v, domains[chosen_v]))
                domains[chosen_v] = branch

                if propagate([chosen_v]) and search():
                    return True

                rollback(checkpoint)

            return False

        return search()

    for verts, edges in non_bip_components:
        if not solve_non_bipartite(verts, edges):
            print("NO")
            return

        for eid in edges:
            u = eu[eid]
            p = domains[u].bit_length() - 1
            answer[eid] = perms[p][pos_u[eid]] + 1

    # Final validation.
    for v in range(n):
        colors = [answer[eid] for eid in adj[v]]
        if sorted(colors) != [1, 2, 3]:
            print("NO")
            return

    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()