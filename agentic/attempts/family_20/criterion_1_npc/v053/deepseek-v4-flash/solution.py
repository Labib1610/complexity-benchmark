import sys
sys.setrecursionlimit(1000000)

def find_matching(n, edges):
    # Edmonds' blossom algorithm for maximum matching
    # n: number of vertices (0-indexed)
    # edges: list of (u,v) pairs
    adj = [[] for _ in range(n)]
    for idx, (u,v) in enumerate(edges):
        adj[u].append((v, idx))
        adj[v].append((u, idx))
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
        nonlocal p, base, used, blossom
        used = [False] * n
        p = [-1] * n
        for i in range(n):
            base[i] = i
        q = deque([root])
        used[root] = True
        while q:
            v = q.popleft()
            for to, eid in adj[v]:
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
                        return to
                    used[match[to]] = True
                    q.append(match[to])
        return -1

    for i in range(n):
        if match[i] == -1:
            v = find_path(i)
            if v == -1:
                continue
            while v != -1:
                pv = p[v]
                nv = match[pv] if pv != -1 else -1
                match[v] = pv
                match[pv] = v
                v = nv
    # Return matched edges
    matching = []
    for u in range(n):
        if match[u] != -1 and u < match[u]:
            matching.append((u, match[u]))
    return matching

def solve():
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
    
    # Build adjacency with edge indices
    adj = [[] for _ in range(n)]
    for idx, (u,v) in enumerate(edges):
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    
    # Check if graph is bridgeless
    # Find bridges using DFS
    visited = [False]*n
    tin = [-1]*n
    low = [-1]*n
    timer = 0
    bridges = set()
    
    def dfs(v, p):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in adj[v]:
            if to == p:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.add(eid)
    
    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    
    if bridges:
        print("NO")
        return
    
    # Find a perfect matching (1-factor)
    matching = find_matching(n, edges)
    if len(matching) != n//2:
        print("NO")
        return
    
    match_set = set()
    for u,v in matching:
        match_set.add((u,v))
        match_set.add((v,u))
    
    # Color matching edges with 1
    color = [0]*m
    for idx, (u,v) in enumerate(edges):
        if (u,v) in match_set:
            color[idx] = 1
    
    # Remaining edges form cycles
    # Build graph of remaining edges
    rem_adj = [[] for _ in range(n)]
    for idx, (u,v) in enumerate(edges):
        if color[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))
    
    # Color cycles alternately 2 and 3
    visited_cycle = [False]*n
    for start in range(n):
        if not visited_cycle[start] and rem_adj[start]:
            # traverse cycle
            stack = [(start, -1, -1)]  # node, parent, edge_id
            cycle_edges = []
            while stack:
                v, p, eid = stack.pop()
                if visited_cycle[v]:
                    continue
                visited_cycle[v] = True
                if eid != -1:
                    cycle_edges.append(eid)
                for to, eid2 in rem_adj[v]:
                    if to == p:
                        continue
                    stack.append((to, v, eid2))
            # Now color cycle edges alternately
            # Find a cycle start
            # Actually we need to walk the cycle properly
            # Let's do a simple BFS to get the cycle order
            # Since it's 2-regular, each component is a cycle
            # Find a starting edge
            start_node = start
            # find an edge
            if not rem_adj[start_node]:
                continue
            prev = -1
            cur = start_node
            first_edge = rem_adj[cur][0][1]
            cycle = []
            edge_seen = set()
            while True:
                # find next edge not going back
                nxt = None
                for to, eid in rem_adj[cur]:
                    if eid != prev and eid not in edge_seen:
                        nxt = (to, eid)
                        break
                if nxt is None:
                    break
                to, eid = nxt
                edge_seen.add(eid)
                cycle.append(eid)
                prev = eid
                cur = to
                if cur == start_node:
                    break
            # color alternately
            for i, eid in enumerate(cycle):
                color[eid] = 2 if i % 2 == 0 else 3
    
    # Check all edges colored
    if any(c == 0 for c in color):
        print("NO")
        return
    
    # Verify each vertex has one of each color
    for v in range(n):
        cnt = [0,0,0,0]
        for to, eid in adj[v]:
            cnt[color[eid]] += 1
        if cnt[1] != 1 or cnt[2] != 1 or cnt[3] != 1:
            print("NO")
            return
    
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()