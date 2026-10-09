import sys

sys.setrecursionlimit(10000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    if len(data) != 2 + 2 * m:
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

    def find_bridges(banned=-1):
        tin = [-1] * n
        low = [0] * n
        timer = 0
        bridges = []

        def dfs(v, parent_edge):
            nonlocal timer
            tin[v] = low[v] = timer
            timer += 1

            for to, eid in adj[v]:
                if eid == banned or eid == parent_edge:
                    continue
                if tin[to] == -1:
                    dfs(to, eid)
                    if low[to] < low[v]:
                        low[v] = low[to]
                    if low[to] > tin[v]:
                        bridges.append(eid)
                elif tin[to] < low[v]:
                    low[v] = tin[to]

        for start in range(n):
            if tin[start] == -1:
                dfs(start, -1)

        return bridges

    # A bridge in a cubic graph makes a 3-edge-coloring impossible.
    if find_bridges():
        print("NO")
        return

    parent = list(range(m))
    size = [1] * m

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

    # The two edges of every 2-edge-cut must have the same color.
    for banned in range(m):
        for eid in find_bridges(banned):
            union(banned, eid)

    root_to_gid = {}
    edge_group = [0] * m
    group_edges = []

    for eid in range(m):
        r = find(eid)
        gid = root_to_gid.get(r)
        if gid is None:
            gid = len(group_edges)
            root_to_gid[r] = gid
            group_edges.append([])
        edge_group[eid] = gid
        group_edges[gid].append(eid)

    gcount = len(group_edges)
    vertex_groups = [[] for _ in range(n)]
    group_vertices = [[] for _ in range(gcount)]

    for v in range(n):
        gs = [edge_group[eid] for _, eid in adj[v]]
        if len(set(gs)) != 3:
            print("NO")
            return
        vertex_groups[v] = gs
        for g in gs:
            group_vertices[g].append(v)

    for g in range(gcount):
        if len(group_vertices[g]) > 1:
            group_vertices[g] = list(set(group_vertices[g]))

    domains = [7] * gcount
    trail = []

    # Fix the global color permutation separately in every connected component.
    seen = [False] * n
    for start in range(n):
        if seen[start]:
            continue

        stack = [start]
        seen[start] = True
        while stack:
            v = stack.pop()
            for to, _ in adj[v]:
                if not seen[to]:
                    seen[to] = True
                    stack.append(to)

        for g, bit in zip(vertex_groups[start], (1, 2, 4)):
            nd = domains[g] & bit
            if nd == 0:
                print("NO")
                return
            if nd != domains[g]:
                trail.append((g, domains[g]))
                domains[g] = nd

    permutations = (
        (1, 2, 4), (1, 4, 2),
        (2, 1, 4), (2, 4, 1),
        (4, 1, 2), (4, 2, 1),
    )

    queued = [False] * n

    def propagate(initial_vertices):
        queue = []
        for v in initial_vertices:
            if not queued[v]:
                queued[v] = True
                queue.append(v)

        head = 0
        while head < len(queue):
            v = queue[head]
            head += 1
            queued[v] = False

            g0, g1, g2 = vertex_groups[v]
            d0, d1, d2 = domains[g0], domains[g1], domains[g2]

            a0 = a1 = a2 = 0
            possible = False

            for b0, b1, b2 in permutations:
                if d0 & b0 and d1 & b1 and d2 & b2:
                    possible = True
                    a0 |= b0
                    a1 |= b1
                    a2 |= b2

            if not possible:
                for i in range(head, len(queue)):
                    queued[queue[i]] = False
                return False

            for g, allowed in ((g0, a0), (g1, a1), (g2, a2)):
                nd = domains[g] & allowed
                if nd == 0:
                    for i in range(head, len(queue)):
                        queued[queue[i]] = False
                    return False
                if nd != domains[g]:
                    trail.append((g, domains[g]))
                    domains[g] = nd
                    for w in group_vertices[g]:
                        if not queued[w]:
                            queued[w] = True
                            queue.append(w)

        return True

    if not propagate(range(n)):
        print("NO")
        return

    def rollback(checkpoint):
        while len(trail) > checkpoint:
            g, old_domain = trail.pop()
            domains[g] = old_domain

    def solve():
        chosen = -1
        best_key = None

        for g, d in enumerate(domains):
            count = d.bit_count()
            if count > 1:
                key = (count, -len(group_vertices[g]))
                if best_key is None or key < best_key:
                    best_key = key
                    chosen = g

        if chosen == -1:
            return True

        d = domains[chosen]
        bits = []
        if d & 1:
            bits.append(1)
        if d & 2:
            bits.append(2)
        if d & 4:
            bits.append(4)

        for bit in bits:
            checkpoint = len(trail)
            trail.append((chosen, domains[chosen]))
            domains[chosen] = bit

            if propagate(group_vertices[chosen]) and solve():
                return True

            rollback(checkpoint)

        return False

    if not solve():
        print("NO")
        return

    answer = []
    for eid in range(m):
        d = domains[edge_group[eid]]
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