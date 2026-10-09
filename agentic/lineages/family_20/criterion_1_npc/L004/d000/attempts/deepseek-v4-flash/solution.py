import sys
sys.setrecursionlimit(1000000)

def find_bridges(n, edges):
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append((v, idx))
        g[v].append((u, idx))
    visited = [False] * n
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    bridges = set()
    def dfs(v, p_edge):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in g[v]:
            if eid == p_edge:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.add(eid)
    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    return bridges

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
    
    # Check if graph is bridgeless
    bridges = find_bridges(n, edges)
    if bridges:
        print("NO")
        return
    
    # Build adjacency with edge ids
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append((v, idx))
        g[v].append((u, idx))
    
    color = [-1] * m
    # We will use a known constructive method:
    # 1. Find a perfect matching (since cubic bridgeless => has perfect matching by Petersen's theorem)
    # 2. Color matching edges with color 1
    # 3. Remaining graph is 2-regular => color with 2 colors (2 and 3)
    
    # Find perfect matching using simple DFS-based approach (Kőnig's theorem for bipartite? Not bipartite necessarily)
    # Use a known algorithm: find a 1-factor via Tutte's theorem? Simpler: use network flow? 
    # But for n ≤ 2000, we can use a simple greedy + augmenting path for matching in general graph (Edmonds' Blossom).
    # However, implementing blossom is heavy. But since graph is cubic and bridgeless, we can use a simpler constructive:
    # Actually, for cubic bridgeless, we can find a perfect matching by repeatedly finding an alternating cycle? 
    # Simpler: Use a known trick: find a 2-factor (since bridgeless cubic has a 2-factor by Petersen's theorem), 
    # then color the 2-factor with 2 colors and the remaining perfect matching with the third color.
    
    # Let's implement a simple 2-factor finder: 
    # We can find a 2-factor by taking a cycle cover. 
    # But easier: use a known algorithm for 3-edge-coloring of cubic bridgeless graphs:
    # - Find a perfect matching M (color 1)
    # - The remaining edges form a 2-regular graph (disjoint cycles), color them alternately with 2 and 3.
    
    # We'll implement a simple perfect matching using backtracking? n=2000 too big.
    # Use Edmonds' Blossom algorithm for general graph maximum matching.
    # Let's implement a standard O(n^3) blossom.
    
    # Build adjacency list for matching
    adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append(v)
        adj[v].append(u)
    
    # Edmonds' Blossom algorithm
    match = [-1] * n
    p = [-1] * n
    base = [-1] * n
    used = [False] * n
    blossom = [False] * n
    
    from collections import deque
    
    def lca(a, b):
        used_path = [False] * n
        while True:
            a = base[a]
            used_path[a] = True
            if match[a] == -1:
                break
            a = p[match[a]]
        while True:
            b = base[b]
            if used_path[b]:
                return b
            b = p[match[b]]
    
    def mark_path(v, b, children):
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = children
            children = match[v]
            v = p[match[v]]
    
    def find_path(root):
        nonlocal match, p, base, used, blossom
        used = [False] * n
        p = [-1] * n
        for i in range(n):
            base[i] = i
        q = deque([root])
        used[root] = True
        while q:
            v = q.popleft()
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
            if v == -1:
                # No perfect matching? Shouldn't happen for bridgeless cubic
                print("NO")
                return
            while v != -1:
                pv = p[v]
                nv = match[pv]
                match[v] = pv
                match[pv] = v
                v = nv
    
    # Now match[] contains perfect matching
    matching_edges = set()
    for u in range(n):
        v = match[u]
        if u < v:
            # find edge id
            for eid, (a,b) in enumerate(edges):
                if (a==u and b==v) or (a==v and b==u):
                    matching_edges.add(eid)
                    break
    
    # Color matching edges with 1
    for eid in matching_edges:
        color[eid] = 1
    
    # Remaining edges form 2-regular graph (cycles)
    # Build adjacency for remaining edges
    rem_adj = [[] for _ in range(n)]
    for eid, (u,v) in enumerate(edges):
        if eid not in matching_edges:
            rem_adj[u].append((v, eid))
            rem_adj[v].append((u, eid))
    
    # Color cycles with 2 and 3 alternately
    visited = [False] * n
    for start in range(n):
        if not visited[start] and rem_adj[start]:
            # traverse cycle
            stack = [(start, -1, 0)]  # node, parent edge, color
            visited[start] = True
            while stack:
                v, pe, c = stack.pop()
                for to, eid in rem_adj[v]:
                    if eid == pe:
                        continue
                    if not visited[to]:
                        visited[to] = True
                        color[eid] = 2 if c == 0 else 3
                        stack.append((to, eid, 1-c))
                    else:
                        # already visited, just color if not colored
                        if color[eid] == -1:
                            color[eid] = 2 if c == 0 else 3
    
    # Check all edges colored
    if any(c == -1 for c in color):
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()