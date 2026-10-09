import sys
sys.setrecursionlimit(10000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    adj = [[] for _ in range(n)]
    eu = [0] * m
    ev = [0] * m

    p = 2
    for i in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        eu[i] = u
        ev[i] = v
        adj[u].append((v, i))
        adj[v].append((u, i))

    if any(len(adj[v]) != 3 for v in range(n)):
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
    seen_v = [False] * n
    seen_e = [False] * m

    for start in range(n):
        if seen_v[start]:
            continue
        stack = [start]
        seen_v[start] = True
        vertices = []
        edges = []

        while stack:
            v = stack.pop()
            vertices.append(v)
            for to, eid in adj[v]:
                if not seen_e[eid]:
                    seen_e[eid] = True
                    edges.append(eid)
                if not seen_v[to]:
                    seen_v[to] = True
                    stack.append(to)

        components.append((vertices, edges))

    domains = [7] * m  # Bits 1, 2, 4 correspond to colors 1, 2, 3.
    trail = []

    permutations = (
        (1, 2, 4), (1, 4, 2),
        (2, 1, 4), (2, 4, 1),
        (4, 1, 2), (4, 2, 1)
    )
    bit_count = (0, 1, 1, 2, 1, 2, 2, 3)

    def rollback(mark):
        while len(trail) > mark:
            eid, old = trail.pop()
            domains[eid] = old

    def restrict_edge(eid, new_domain):
        old = domains[eid]
        nd = old & new_domain
        if nd == 0:
            return False
        if nd != old:
            trail.append((eid, old))
            domains[eid] = nd
        return True

    def propagate(initial_vertices):
        queue = list(initial_vertices)
        in_queue = [False] * n
        for v in queue:
            in_queue[v] = True
        head = 0

        while head < len(queue):
            v = queue[head]
            head += 1
            in_queue[v] = False

            e0 = adj[v][0][1]
            e1 = adj[v][1][1]
            e2 = adj[v][2][1]
            d0, d1, d2 = domains[e0], domains[e1], domains[e2]

            a0 = a1 = a2 = 0
            for c0, c1, c2 in permutations:
                if (d0 & c0) and (d1 & c1) and (d2 & c2):
                    a0 |= c0
                    a1 |= c1
                    a2 |= c2

            if a0 == 0:
                return False

            for eid, allowed in ((e0, a0), (e1, a1), (e2, a2)):
                old = domains[eid]
                nd = old & allowed
                if nd == 0:
                    return False
                if nd != old:
                    trail.append((eid, old))
                    domains[eid] = nd
                    x, y = eu[eid], ev[eid]
                    if not in_queue[x]:
                        in_queue[x] = True
                        queue.append(x)
                    if not in_queue[y]:
                        in_queue[y] = True
                        queue.append(y)

        return True

    def solve_component(vertices, edges):
        root = vertices[0]
        root_edges = [eid for _, eid in adj[root]]
        base_mark = len(trail)

        for eid, color in zip(root_edges, (1, 2, 4)):
            if not restrict_edge(eid, color):
                rollback(base_mark)
                return False

        if not propagate(vertices):
            rollback(base_mark)
            return False

        def dfs():
            chosen = -1
            best_size = 4
            best_score = -1

            for eid in edges:
                d = domains[eid]
                cnt = bit_count[d]
                if cnt <= 1:
                    continue

                score = 0
                u, v = eu[eid], ev[eid]
                for x in (u, v):
                    for _, ne in adj[x]:
                        if ne != eid:
                            score += 3 - bit_count[domains[ne]]

                if cnt < best_size or (cnt == best_size and score > best_score):
                    best_size = cnt
                    best_score = score
                    chosen = eid

            if chosen == -1:
                return True

            d = domains[chosen]
            values = []
            b = 1
            while b <= 4:
                if d & b:
                    cost = 0
                    u, v = eu[chosen], ev[chosen]
                    for x in (u, v):
                        for _, ne in adj[x]:
                            if ne != chosen and (domains[ne] & b):
                                cost += 1
                    values.append((cost, b))
                b <<= 1
            values.sort()

            for _, color in values:
                mark = len(trail)
                if restrict_edge(chosen, color):
                    if propagate((eu[chosen], ev[chosen])) and dfs():
                        return True
                rollback(mark)

            return False

        if dfs():
            return True

        rollback(base_mark)
        return False

    for vertices, edges in components:
        if not solve_component(vertices, edges):
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