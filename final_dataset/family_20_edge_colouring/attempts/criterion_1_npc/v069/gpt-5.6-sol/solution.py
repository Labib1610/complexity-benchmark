import sys

sys.setrecursionlimit(100000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    if m != 3 * n // 2 or len(data) != 2 + 2 * m:
        print("NO")
        return

    adj = [[] for _ in range(n)]
    ends = [None] * m

    p = 2
    for eid in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if not (0 <= u < n and 0 <= v < n) or u == v:
            print("NO")
            return
        ends[eid] = (u, v)
        adj[u].append(eid)
        adj[v].append(eid)

    if any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    tin = [-1] * n
    low = [0] * n
    component = [-1] * n
    timer = 0
    has_bridge = False
    component_count = 0

    def bridge_dfs(v, parent_edge, cid):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1
        component[v] = cid

        for eid in adj[v]:
            if eid == parent_edge:
                continue
            a, b = ends[eid]
            to = b if a == v else a

            if tin[to] == -1:
                bridge_dfs(to, eid, cid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True
            else:
                low[v] = min(low[v], tin[to])

    for v in range(n):
        if tin[v] == -1:
            bridge_dfs(v, -1, component_count)
            component_count += 1

    if has_bridge:
        print("NO")
        return

    component_vertices = [[] for _ in range(component_count)]
    component_edges = [[] for _ in range(component_count)]

    for v in range(n):
        component_vertices[component[v]].append(v)
    for eid, (u, _) in enumerate(ends):
        component_edges[component[u]].append(eid)

    domains = [7] * m
    popcount = (0, 1, 1, 2, 1, 2, 2, 3)
    permutations = (
        (1, 2, 4), (1, 4, 2),
        (2, 1, 4), (2, 4, 1),
        (4, 1, 2), (4, 2, 1)
    )

    def solve_component(vertices, edge_list):
        trail = []
        in_queue = [False] * n

        def propagate(initial_vertices):
            queue = []
            for v in initial_vertices:
                if not in_queue[v]:
                    in_queue[v] = True
                    queue.append(v)

            head = 0
            while head < len(queue):
                v = queue[head]
                head += 1
                in_queue[v] = False

                e0, e1, e2 = adj[v]
                d0, d1, d2 = domains[e0], domains[e1], domains[e2]
                s0 = s1 = s2 = 0

                for c0, c1, c2 in permutations:
                    if (d0 & c0) and (d1 & c1) and (d2 & c2):
                        s0 |= c0
                        s1 |= c1
                        s2 |= c2

                if s0 == 0:
                    for i in range(head, len(queue)):
                        in_queue[queue[i]] = False
                    return False

                for eid, nd in ((e0, s0), (e1, s1), (e2, s2)):
                    od = domains[eid]
                    if nd != od:
                        trail.append((eid, od))
                        domains[eid] = nd
                        a, b = ends[eid]
                        if not in_queue[a]:
                            in_queue[a] = True
                            queue.append(a)
                        if not in_queue[b]:
                            in_queue[b] = True
                            queue.append(b)

            return True

        root = vertices[0]
        initial_vertices = []
        for eid, color in zip(adj[root], (1, 2, 4)):
            if domains[eid] != color:
                trail.append((eid, domains[eid]))
                domains[eid] = color
                a, b = ends[eid]
                initial_vertices.append(a)
                initial_vertices.append(b)

        if not propagate(initial_vertices):
            return False

        def search():
            chosen = -1
            best_size = 4
            best_impact = -1

            for eid in edge_list:
                d = domains[eid]
                size = popcount[d]
                if size == 1:
                    continue

                if size > best_size:
                    continue

                u, v = ends[eid]
                impact = 0
                for x in adj[u]:
                    if x != eid and popcount[domains[x]] > 1:
                        impact += 1
                for x in adj[v]:
                    if x != eid and popcount[domains[x]] > 1:
                        impact += 1

                if size < best_size or impact > best_impact:
                    best_size = size
                    best_impact = impact
                    chosen = eid

            if chosen == -1:
                return True

            u, v = ends[chosen]
            choices = []
            mask = domains[chosen]
            for color in (1, 2, 4):
                if mask & color:
                    cost = 0
                    for eid in adj[u]:
                        if eid != chosen and domains[eid] & color:
                            cost += 1
                    for eid in adj[v]:
                        if eid != chosen and domains[eid] & color:
                            cost += 1
                    choices.append((cost, color))
            choices.sort()

            for _, color in choices:
                mark = len(trail)
                old = domains[chosen]
                if old != color:
                    trail.append((chosen, old))
                    domains[chosen] = color

                if propagate((u, v)) and search():
                    return True

                while len(trail) > mark:
                    eid, old_domain = trail.pop()
                    domains[eid] = old_domain

            return False

        return search()

    for cid in range(component_count):
        if not solve_component(component_vertices[cid], component_edges[cid]):
            print("NO")
            return

    answer = []
    for d in domains:
        if d == 1:
            answer.append("1")
        elif d == 2:
            answer.append("2")
        elif d == 4:
            answer.append("3")
        else:
            print("NO")
            return

    print("YES")
    print(" ".join(answer))

if __name__ == "__main__":
    main()