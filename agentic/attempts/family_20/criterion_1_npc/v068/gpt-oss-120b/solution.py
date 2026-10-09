import sys
sys.setrecursionlimit(10000)

# ------------------------------------------------------------
# 1. bridge detection (lowlink)
def find_bridge(n, edges):
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append((v, idx))
        g[v].append((u, idx))
    tin = [-1] * n
    low = [0] * n
    timer = 0
    bridge = [False]

    def dfs(v, p_edge):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in g[v]:
            if eid == p_edge:
                continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridge[0] = True

    dfs(0, -1)
    return bridge[0]

# ------------------------------------------------------------
# 2. Edmonds blossom (maximum matching) – CP‑algorithm version
def blossom_maximum_matching(n, adj):
    # adj: list of sets, undirected
    INF = n + 5
    match = [-1] * n
    base = list(range(n))
    p = [-1] * n
    q = []
    used = [False] * n
    blossom = [False] * n

    def lca(a, b):
        used2 = [False] * n
        while True:
            a = base[a]
            used2[a] = True
            if match[a] == -1:
                break
            a = p[match[a]]
        while True:
            b = base[b]
            if used2[b]:
                return b
            b = p[match[b]]

    def mark_path(v, b, x):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = x
            x = match[v]
            v = p[match[v]]

    def find_path(root):
        nonlocal q, used, p, base, blossom
        used = [False] * n
        p = [-1] * n
        base = list(range(n))
        q = [root]
        used[root] = True
        head = 0
        while head < len(q):
            v = q[head]
            head += 1
            for to in adj[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    curbase = lca(v, to)
                    blossom = [False] * n
                    mark_path(v, curbase, to)
                    mark_path(to, curbase, v)
                    for i in range(n):
                        if blossom[base[i]]:
                            base[i] = curbase
                            if not used[i]:
                                used[i] = True
                                q.append(i)
                elif p[to] == -1:
                    p[to] = v
                    if match[to] == -1:
                        # augmenting
                        cur = to
                        while cur != -1:
                            prev = p[cur]
                            nxt = match[prev] if prev != -1 else -1
                            match[cur] = prev
                            match[prev] = cur
                            cur = nxt
                        return True
                    else:
                        used[match[to]] = True
                        q.append(match[to])
        return False

    for v in range(n):
        if match[v] == -1:
            find_path(v)
    return match

# ------------------------------------------------------------
def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))

    # 1. bridge test
    if find_bridge(n, edges):
        print("NO")
        return

    # 2. build adjacency for blossom
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    match = blossom_maximum_matching(n, adj)
    # match is a perfect matching
    # 3. build 2‑regular graph after removing matching
    in_match = [False] * m
    edge_id = {}
    for idx, (u, v) in enumerate(edges):
        edge_id[(u, v)] = edge_id[(v, u)] = idx
        if match[u] == v:
            in_match[idx] = True

    # adjacency of the remaining graph (each vertex degree 2)
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if not in_match[idx]:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    # 4. eliminate odd cycles
    visited = [False] * n
    def dfs_cycle(v, parent, comp):
        visited[v] = True
        comp.append(v)
        for to, _ in rem_adj[v]:
            if to == parent:
                continue
            if not visited[to]:
                if dfs_cycle(to, v, comp):
                    return True
        return False

    # we will repeatedly find an odd cycle and flip along an alternating
    # path to merge it with an even one.
    while True:
        # find any odd cycle
        visited = [False] * n
        odd_cycle = None
        parent_edge = [-1] * n
        for start in range(n):
            if visited[start]:
                continue
            stack = [(start, -1)]
            while stack:
                v, pe = stack.pop()
                if visited[v]:
                    # found a back edge -> cycle
                    # reconstruct cycle
                    cur = v
                    cyc = []
                    while cur != -1 and cur != v:
                        cyc.append(cur)
                        cur = parent_edge[cur]
                    cyc.append(v)
                    if len(cyc) % 2 == 1:
                        odd_cycle = (v, pe)
                        break
                    continue
                visited[v] = True
                parent_edge[v] = pe
                for to, eid in rem_adj[v]:
                    if eid == pe:
                        continue
                    stack.append((to, eid))
            if odd_cycle:
                break
        if not odd_cycle:
            break  # all cycles even

        # odd_cycle gives an edge of the odd cycle (not needed explicitly)
        # we now find an alternating path from one endpoint of that edge
        # to any vertex that lies on an even cycle.
        # For simplicity we just pick the first vertex of the odd cycle
        # and run BFS in the whole graph using alternating edges.

        # mark vertices belonging to even cycles
        even_vertices = [False] * n
        visited = [False] * n
        for v in range(n):
            if not visited[v]:
                comp = []
                stack = [v]
                visited[v] = True
                while stack:
                    x = stack.pop()
                    comp.append(x)
                    for to, _ in rem_adj[x]:
                        if not visited[to]:
                            visited[to] = True
                            stack.append(to)
                if len(comp) % 2 == 0:
                    for x in comp:
                        even_vertices[x] = True

        # start BFS from any vertex of the odd cycle
        start = odd_cycle[0]
        from collections import deque
        q = deque([start])
        prev = [-1] * n
        prev_edge = [-1] * n
        in_match_edge = [False] * n  # whether we arrived via matching edge
        while q:
            v = q.popleft()
            if even_vertices[v] and v != start:
                # found target
                break
            for to, eid in rem_adj[v]:
                if prev[to] != -1:
                    continue
                # edge is not in matching (rem_adj only contains non‑matching)
                # we can move along it, then must take the matching edge incident to 'to'
                prev[to] = v
                prev_edge[to] = eid
                # now go through matching edge
                w = match[to]
                if prev[w] == -1:
                    prev[w] = to
                    prev_edge[w] = -1
                    q.append(w)
        # reconstruct and flip
        cur = v
        while cur != -1 and prev[cur] != -1:
            pe = prev_edge[cur]
            if pe != -1:
                # toggle this edge between matching / non‑matching
                in_match[pe] = not in_match[pe]
                # update rem_adj structures
                u, w = edges[pe]
                if in_match[pe]:
                    # remove from rem_adj
                    rem_adj[u] = [(x, e) for x, e in rem_adj[u] if e != pe]
                    rem_adj[w] = [(x, e) for x, e in rem_adj[w] if e != pe]
                else:
                    rem_adj[u].append((w, pe))
                    rem_adj[w].append((u, pe))
            cur = prev[cur]

    # 5. final colouring
    colour = [0] * m
    for i, b in enumerate(in_match):
        if b:
            colour[i] = 1
    # colour even cycles with 2/3
    visited = [False] * n
    for v in range(n):
        if visited[v]:
            continue
        # traverse the cycle
        cur = v
        prev = -1
        col = 2
        while True:
            visited[cur] = True
            # find the non‑matching edge leading forward
            nxt = None
            eid = None
            for to, e in rem_adj[cur]:
                if to == prev:
                    continue
                nxt = to
                eid = e
                break
            if eid is None:
                break
            colour[eid] = col
            col = 5 - col          # switch between 2 and 3
            prev, cur = cur, nxt
            if cur == v:
                break

    print("YES")
    print(' '.join(str(colour[i]) for i in range(m)))

if __name__ == "__main__":
    main()