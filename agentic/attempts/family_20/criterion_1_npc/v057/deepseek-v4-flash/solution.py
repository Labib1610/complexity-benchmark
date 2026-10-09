import sys
sys.setrecursionlimit(10000)

def find_perfect_matching(n, adj):
    # Blossom algorithm for maximum matching in general graph
    # Returns a list match where match[u] = v or -1
    match = [-1] * n
    p = [-1] * n
    base = list(range(n))
    used = [False] * n
    blossom = [False] * n

    def lca(a, b):
        used_lca = [False] * n
        while True:
            a = base[a]
            used_lca[a] = True
            if match[a] == -1:
                break
            a = p[match[a]]
        while True:
            b = base[b]
            if used_lca[b]:
                return b
            b = p[match[b]]

    def mark_path(v, b, children):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = children
            children = match[v]
            v = p[match[v]]

    def find_path(root):
        nonlocal p, base, used, blossom
        used = [False] * n
        p = [-1] * n
        for i in range(n):
            base[i] = i
        q = [root]
        used[root] = True
        for v in q:
            for u in adj[v]:
                if base[v] == base[u] or match[v] == u:
                    continue
                if u == root or (match[u] != -1 and p[match[u]] != -1):
                    curbase = lca(v, u)
                    blossom = [False] * n
                    mark_path(v, curbase, u)
                    mark_path(u, curbase, v)
                    for i in range(n):
                        if blossom[base[i]]:
                            base[i] = curbase
                            if not used[i]:
                                used[i] = True
                                q.append(i)
                elif p[u] == -1:
                    p[u] = v
                    if match[u] == -1:
                        return u
                    u = match[u]
                    used[u] = True
                    q.append(u)
        return -1

    for i in range(n):
        if match[i] == -1:
            v = find_path(i)
            while v != -1:
                pv = p[v]
                nv = match[pv]
                match[v] = pv
                match[pv] = v
                v = nv

    # Check if perfect
    for i in range(n):
        if match[i] == -1:
            return None
    return match

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)

    # Check for bridges (if any bridge, no perfect matching -> NO)
    # Use Tarjan to find bridges
    tin = [-1] * n
    low = [-1] * n
    timer = [0]
    visited = [False] * n
    has_bridge = [False]

    def dfs(v, p_edge):
        visited[v] = True
        tin[v] = low[v] = timer[0]
        timer[0] += 1
        for to in adj[v]:
            if to == p_edge:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge[0] = True

    dfs(0, -1)
    if has_bridge[0]:
        print("NO")
        return

    # Find perfect matching
    match = find_perfect_matching(n, adj)
    if match is None:
        print("NO")
        return

    # Color matching edges with 1
    color = [0] * m
    match_edge_idx = {}
    for idx, (u, v) in enumerate(edges):
        if match[u] == v:
            color[idx] = 1
            match_edge_idx[(u, v)] = idx
            match_edge_idx[(v, u)] = idx

    # Remaining graph is 2-regular -> cycles
    # Build adjacency for non-matching edges
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if color[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))

    visited_cycle = [False] * n
    for start in range(n):
        if not visited_cycle[start]:
            # traverse cycle
            cycle_edges = []
            cur = start
            prev = -1
            while True:
                visited_cycle[cur] = True
                # pick next neighbor not prev
                nxt = -1
                eidx = -1
                for to, ei in rem_adj[cur]:
                    if to != prev:
                        nxt = to
                        eidx = ei
                        break
                if nxt == -1:
                    break
                cycle_edges.append(eidx)
                prev, cur = cur, nxt
                if cur == start:
                    break
            # color alternating 2,3
            for i, eidx in enumerate(cycle_edges):
                color[eidx] = 2 if i % 2 == 0 else 3

    # Verify each node has all three colors
    for u in range(n):
        cols = set()
        for v in adj[u]:
            # find edge index
            for idx, (a, b) in enumerate(edges):
                if (a == u and b == v) or (a == v and b == u):
                    cols.add(color[idx])
                    break
        if len(cols) != 3:
            print("NO")
            return

    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()