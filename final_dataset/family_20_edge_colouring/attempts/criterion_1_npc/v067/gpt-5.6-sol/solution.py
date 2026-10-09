import sys

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

    # A regular graph with a proper edge coloring using its degree
    # cannot contain a bridge.
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

    # Connected components.
    seen = [False] * n
    components = []

    for s in range(n):
        if seen[s]:
            continue
        stack = [s]
        seen[s] = True
        vertices = []
        component_edges = []
        edge_seen = set()

        while stack:
            v = stack.pop()
            vertices.append(v)
            for eid in adj[v]:
                if eid not in edge_seen:
                    edge_seen.add(eid)
                    component_edges.append(eid)
                a, b = edges[eid]
                to = b if a == v else a
                if not seen[to]:
                    seen[to] = True
                    stack.append(to)

        components.append((vertices, component_edges))

    # status: 0 = undecided, 1 = selected perfect-matching edge,
    #        -1 = edge in the remaining even cycles.
    status = [0] * m
    matched = [False] * n

    parent = list(range(n))
    size = [1] * n
    parity = [0] * n

    status_log = []
    matched_log = []
    dsu_log = []

    def find(x):
        px = 0
        while parent[x] != x:
            px ^= parity[x]
            x = parent[x]
        return x, px

    def unite_opposite(a, b):
        ra, xa = find(a)
        rb, xb = find(b)

        if ra == rb:
            return xa ^ xb == 1, False

        if size[ra] < size[rb]:
            ra, rb = rb, ra
            xa, xb = xb, xa

        dsu_log.append((rb, ra, size[ra]))
        parent[rb] = ra
        parity[rb] = xa ^ xb ^ 1
        size[ra] += size[rb]
        return True, True

    def checkpoint():
        return len(status_log), len(matched_log), len(dsu_log)

    def rollback(cp):
        sl, ml, dl = cp

        while len(status_log) > sl:
            eid = status_log.pop()
            status[eid] = 0

        while len(matched_log) > ml:
            v = matched_log.pop()
            matched[v] = False

        while len(dsu_log) > dl:
            child, root, old_size = dsu_log.pop()
            parent[child] = child
            parity[child] = 0
            size[root] = old_size

    def propagate(initial_actions, component_edges):
        actions = initial_actions[:]
        need_scan = False

        def check_vertex(v):
            if matched[v]:
                return True

            count = 0
            last = -1
            for eid in adj[v]:
                if status[eid] == 0:
                    count += 1
                    last = eid

            if count == 0:
                return False
            if count == 1:
                actions.append((1, last))
            return True

        while True:
            while actions:
                typ, eid = actions.pop()
                cur = status[eid]
                u, v = edges[eid]

                if typ == 1:
                    if cur == 1:
                        continue
                    if cur == -1 or matched[u] or matched[v]:
                        return False

                    status_log.append(eid)
                    status[eid] = 1

                    matched_log.append(u)
                    matched[u] = True
                    matched_log.append(v)
                    matched[v] = True

                    for x in (u, v):
                        for other in adj[x]:
                            if other != eid:
                                if status[other] == 1:
                                    return False
                                if status[other] == 0:
                                    actions.append((-1, other))

                else:
                    if cur == -1:
                        continue
                    if cur == 1:
                        return False

                    ok, changed = unite_opposite(u, v)
                    if not ok:
                        return False

                    status_log.append(eid)
                    status[eid] = -1
                    need_scan = need_scan or changed

                    if not check_vertex(u) or not check_vertex(v):
                        return False

            if not need_scan:
                break

            need_scan = False
            forced = False
            for eid in component_edges:
                if status[eid] != 0:
                    continue
                u, v = edges[eid]
                ru, xu = find(u)
                rv, xv = find(v)
                if ru == rv and xu == xv:
                    actions.append((1, eid))
                    forced = True

            if not forced:
                break

        return True

    def solve_component(vertices, component_edges):
        root_cp = checkpoint()

        # Any valid coloring can have its colors permuted so that this edge
        # belongs to the chosen matching.
        if not propagate([(1, component_edges[0])], component_edges):
            rollback(root_cp)
            return False

        def dfs():
            best_v = -1
            best_candidates = None

            for v in vertices:
                if matched[v]:
                    continue
                candidates = [eid for eid in adj[v] if status[eid] == 0]
                if not candidates:
                    return False
                if best_candidates is None or len(candidates) < len(best_candidates):
                    best_v = v
                    best_candidates = candidates
                    if len(candidates) == 1:
                        break

            if best_v == -1:
                return True

            # Prefer edges whose endpoints are already constrained by parity.
            best_candidates.sort(
                key=lambda eid: (
                    find(edges[eid][0])[0] != find(edges[eid][1])[0],
                    eid
                )
            )

            for eid in best_candidates:
                cp = checkpoint()
                if propagate([(1, eid)], component_edges) and dfs():
                    return True
                rollback(cp)

            return False

        if dfs():
            return True

        rollback(root_cp)
        return False

    for vertices, component_edges in components:
        if not component_edges or not solve_component(vertices, component_edges):
            print("NO")
            return

    colors = [0] * m

    for eid in range(m):
        if status[eid] == 1:
            colors[eid] = 3

    # The non-matching edges form disjoint even cycles. Alternate colors 1 and 2.
    for start in range(m):
        if status[start] != -1 or colors[start] != 0:
            continue

        colors[start] = 1
        stack = [start]

        while stack:
            eid = stack.pop()
            c = colors[eid]
            u, v = edges[eid]

            for x in (u, v):
                for other in adj[x]:
                    if other == eid or status[other] != -1:
                        continue
                    wanted = 3 - c
                    if colors[other] == 0:
                        colors[other] = wanted
                        stack.append(other)
                    elif colors[other] != wanted:
                        print("NO")
                        return

    print("YES")
    print(*colors)


if __name__ == "__main__":
    main()