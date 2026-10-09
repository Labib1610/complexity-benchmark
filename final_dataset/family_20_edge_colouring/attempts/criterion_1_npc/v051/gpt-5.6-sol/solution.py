import sys
from collections import deque

sys.setrecursionlimit(20000)


def solve():
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

    if m * 2 != 3 * n or any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    def other(eid, u):
        a, b = edges[eid]
        return b if a == u else a

    # A cubic graph with a bridge cannot have a 3-edge-coloring.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def bridge_dfs(u, parent_edge):
        nonlocal timer, has_bridge
        tin[u] = low[u] = timer
        timer += 1
        for eid in adj[u]:
            if eid == parent_edge:
                continue
            v = other(eid, u)
            if tin[v] == -1:
                bridge_dfs(v, eid)
                if low[v] > tin[u]:
                    has_bridge = True
                if low[v] < low[u]:
                    low[u] = low[v]
            elif tin[v] < low[u]:
                low[u] = tin[v]

    for start in range(n):
        if tin[start] == -1:
            bridge_dfs(start, -1)

    if has_bridge:
        print("NO")
        return

    # Edges belonging to the same 2-edge-cut must receive the same color.
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

    for skipped in range(m):
        r = find(skipped)
        if size[r] > 1:
            continue

        disc = [-1] * n
        low2 = [0] * n
        timer2 = 0
        bridges_after_removal = []

        def dfs2(u, parent_edge):
            nonlocal timer2
            disc[u] = low2[u] = timer2
            timer2 += 1
            for eid in adj[u]:
                if eid == skipped or eid == parent_edge:
                    continue
                v = other(eid, u)
                if disc[v] == -1:
                    dfs2(v, eid)
                    if low2[v] > disc[u]:
                        bridges_after_removal.append(eid)
                    if low2[v] < low2[u]:
                        low2[u] = low2[v]
                elif disc[v] < low2[u]:
                    low2[u] = disc[v]

        dfs2(0, -1)
        for eid in bridges_after_removal:
            union(skipped, eid)

    root_to_group = {}
    edge_group = [0] * m
    group_edges = []

    for eid in range(m):
        r = find(eid)
        gid = root_to_group.get(r)
        if gid is None:
            gid = len(group_edges)
            root_to_group[r] = gid
            group_edges.append([])
        edge_group[eid] = gid
        group_edges[gid].append(eid)

    groups = len(group_edges)
    vertex_groups = [[] for _ in range(n)]
    group_vertices = [[] for _ in range(groups)]

    for eid, (u, v) in enumerate(edges):
        g = edge_group[eid]
        vertex_groups[u].append(g)
        vertex_groups[v].append(g)
        group_vertices[g].append(u)
        group_vertices[g].append(v)

    # Equal-color edges may not meet at a vertex.
    for v in range(n):
        if len(set(vertex_groups[v])) != 3:
            print("NO")
            return

    group_color = [-1] * groups
    vertex_mask = [0] * n
    trail = []

    def domain(g):
        mask = 7
        for v in group_vertices[g]:
            mask &= 7 ^ vertex_mask[v]
            if mask == 0:
                break
        return mask

    def assign_group(g, c, queue):
        old = group_color[g]
        if old != -1:
            return old == c

        bit = 1 << c
        for v in group_vertices[g]:
            if vertex_mask[v] & bit:
                return False

        group_color[g] = c
        trail.append(g)
        for v in group_vertices[g]:
            vertex_mask[v] |= bit
            queue.append(v)
        return True

    def rollback(mark):
        while len(trail) > mark:
            g = trail.pop()
            bit = 1 << group_color[g]
            for v in group_vertices[g]:
                vertex_mask[v] ^= bit
            group_color[g] = -1

    def propagate(queue):
        while queue:
            v = queue.popleft()
            for g in vertex_groups[v]:
                if group_color[g] != -1:
                    continue
                d = domain(g)
                if d == 0:
                    return False
                if d & (d - 1) == 0:
                    c = d.bit_length() - 1
                    if not assign_group(g, c, queue):
                        return False
        return True

    def dfs():
        best = -1
        best_domain = 0
        best_count = 4
        best_score = -1

        for g in range(groups):
            if group_color[g] != -1:
                continue
            d = domain(g)
            cnt = d.bit_count()
            if cnt == 0:
                return False
            score = len(group_vertices[g])
            if cnt < best_count or (cnt == best_count and score > best_score):
                best = g
                best_domain = d
                best_count = cnt
                best_score = score

        if best == -1:
            return True

        mark = len(trail)

        # A completely untouched connected constraint component can have
        # its color permutation fixed at an arbitrary vertex.
        if best_count == 3:
            v = group_vertices[best][0]
            q = deque()
            for c, g in enumerate(vertex_groups[v]):
                if not assign_group(g, c, q):
                    rollback(mark)
                    return False
            if propagate(q) and dfs():
                return True
            rollback(mark)
            return False

        d = best_domain
        while d:
            bit = d & -d
            d -= bit
            c = bit.bit_length() - 1
            q = deque()
            if assign_group(best, c, q) and propagate(q) and dfs():
                return True
            rollback(mark)

        return False

    if not dfs():
        print("NO")
        return

    answer = [str(group_color[edge_group[eid]] + 1) for eid in range(m)]
    print("YES")
    print(" ".join(answer))


if __name__ == "__main__":
    solve()