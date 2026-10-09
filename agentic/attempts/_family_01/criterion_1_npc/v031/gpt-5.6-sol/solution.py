import sys

sys.setrecursionlimit(1_000_000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [[] for _ in range(n)]
    adj_mask = [0] * n

    p = 2
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v or ((adj_mask[u] >> v) & 1):
            continue
        adj[u].append(v)
        adj[v].append(u)
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    answer = [0] * n
    seen = [False] * n
    components = []

    for start in range(n):
        if seen[start]:
            continue
        stack = [start]
        seen[start] = True
        component = []
        while stack:
            v = stack.pop()
            component.append(v)
            for u in adj[v]:
                if not seen[u]:
                    seen[u] = True
                    stack.append(u)
        components.append(component)

    def bipartite_coloring(vertices):
        color = {}
        for start in vertices:
            if start in color:
                continue
            color[start] = 1
            queue = [start]
            head = 0
            while head < len(queue):
                v = queue[head]
                head += 1
                nc = 3 - color[v]
                for u in adj[v]:
                    if u not in color:
                        color[u] = nc
                        queue.append(u)
                    elif color[u] == color[v]:
                        return None
        return color

    def solve_two_sat(vertices, domains, assigned_mask):
        unassigned = [v for v in vertices if not ((assigned_mask >> v) & 1)]
        idx = {v: i for i, v in enumerate(unassigned)}
        options = []

        for v in unassigned:
            bits = [1 << c for c in range(3) if domains[v] & (1 << c)]
            if len(bits) != 2:
                return None
            options.append(bits)

        k = len(unassigned)
        graph = [[] for _ in range(2 * k)]
        reverse = [[] for _ in range(2 * k)]

        def add_implication(a, b):
            graph[a].append(b)
            reverse[b].append(a)

        for i, v in enumerate(unassigned):
            for u in adj[v]:
                j = idx.get(u)
                if j is None or i >= j:
                    continue
                for a in range(2):
                    for b in range(2):
                        if options[i][a] == options[j][b]:
                            x = 2 * i + a
                            y = 2 * j + b
                            add_implication(x, 2 * j + (1 - b))
                            add_implication(y, 2 * i + (1 - a))

        visited = [False] * (2 * k)
        order = []

        def dfs1(v):
            visited[v] = True
            for u in graph[v]:
                if not visited[u]:
                    dfs1(u)
            order.append(v)

        for v in range(2 * k):
            if not visited[v]:
                dfs1(v)

        comp = [-1] * (2 * k)

        def dfs2(v, cid):
            comp[v] = cid
            for u in reverse[v]:
                if comp[u] == -1:
                    dfs2(u, cid)

        cid = 0
        for v in reversed(order):
            if comp[v] == -1:
                dfs2(v, cid)
                cid += 1

        result = domains.copy()
        for i, v in enumerate(unassigned):
            if comp[2 * i] == comp[2 * i + 1]:
                return None
            choice = 1 if comp[2 * i + 1] > comp[2 * i] else 0
            result[v] = options[i][choice]

        return result

    def solve_component(vertices):
        if len(vertices) == 1:
            return {vertices[0]: 1}

        simple = bipartite_coloring(vertices)
        if simple is not None:
            return simple

        component_mask = 0
        for v in vertices:
            component_mask |= 1 << v

        domains = [0] * n
        for v in vertices:
            domains[v] = 7

        root = max(vertices, key=lambda x: len(adj[x]))
        domains[root] = 1
        failed = set()
        memo_limit = 500_000

        def dfs(dom, assigned_mask, used_colors):
            queue = []
            for v in vertices:
                if not ((assigned_mask >> v) & 1):
                    d = dom[v]
                    if d == 0:
                        return None
                    if d & (d - 1) == 0:
                        queue.append(v)

            head = 0
            while head < len(queue):
                v = queue[head]
                head += 1
                if (assigned_mask >> v) & 1:
                    continue

                color_bit = dom[v]
                if color_bit == 0 or color_bit & (color_bit - 1):
                    continue

                assigned_mask |= 1 << v
                used_colors |= color_bit

                for u in adj[v]:
                    if not ((component_mask >> u) & 1):
                        continue
                    if (assigned_mask >> u) & 1:
                        if dom[u] == color_bit:
                            return None
                    elif dom[u] & color_bit:
                        nd = dom[u] & ~color_bit
                        if nd == 0:
                            return None
                        if nd != dom[u]:
                            dom[u] = nd
                            if nd & (nd - 1) == 0:
                                queue.append(u)

            if (assigned_mask & component_mask) == component_mask:
                return dom

            all_two = True
            for v in vertices:
                if not ((assigned_mask >> v) & 1) and dom[v].bit_count() != 2:
                    all_two = False
                    break
            if all_two:
                return solve_two_sat(vertices, dom, assigned_mask)

            key = tuple(dom[v] for v in vertices)
            if key in failed:
                return None

            best = -1
            best_key = None
            unassigned_mask = component_mask & ~assigned_mask

            for v in vertices:
                if (assigned_mask >> v) & 1:
                    continue
                domain_size = dom[v].bit_count()
                remaining_degree = (adj_mask[v] & unassigned_mask).bit_count()
                candidate_key = (domain_size, -remaining_degree, -len(adj[v]))
                if best_key is None or candidate_key < best_key:
                    best_key = candidate_key
                    best = v

            allowed = used_colors
            if used_colors != 7:
                for bit in (1, 2, 4):
                    if not (used_colors & bit):
                        allowed |= bit
                        break

            choices = dom[best] & allowed
            for bit in (1, 2, 4):
                if choices & bit:
                    next_dom = dom.copy()
                    next_dom[best] = bit
                    result = dfs(next_dom, assigned_mask, used_colors)
                    if result is not None:
                        return result

            if len(failed) < memo_limit:
                failed.add(key)
            return None

        result = dfs(domains, 0, 0)
        if result is None:
            return None

        coloring = {}
        for v in vertices:
            bit = result[v]
            if bit == 1:
                coloring[v] = 1
            elif bit == 2:
                coloring[v] = 2
            elif bit == 4:
                coloring[v] = 3
            else:
                return None
        return coloring

    components.sort(key=lambda comp: (-len(comp), -sum(len(adj[v]) for v in comp)))

    for component in components:
        coloring = solve_component(component)
        if coloring is None:
            print("NO")
            return
        for v, c in coloring.items():
            answer[v] = c

    for v in range(n):
        for u in adj[v]:
            if answer[v] == answer[u]:
                print("NO")
                return

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()