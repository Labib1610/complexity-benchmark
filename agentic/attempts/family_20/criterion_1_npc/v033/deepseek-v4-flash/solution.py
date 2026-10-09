import sys
sys.setrecursionlimit(10000)

def find_bridges(n, edges):
    g = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        g[u].append((v, idx))
        g[v].append((u, idx))
    visited = [False]*n
    tin = [-1]*n
    low = [-1]*n
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

def perfect_matching(n, edges):
    # Build adjacency with edge ids
    adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    match = [-1]*n
    match_edge = [-1]*n  # edge id used for matched vertex
    
    def augment(u, visited):
        for v, eid in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            if match[v] == -1 or augment(match[v], visited):
                match[u] = v
                match[v] = u
                match_edge[u] = eid
                match_edge[v] = eid
                return True
        return False
    
    for i in range(n):
        if match[i] == -1:
            visited = [False]*n
            visited[i] = True
            augment(i, visited)
    return match, match_edge

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        edges.append((u, v))
    
    # Check bridges
    bridges = find_bridges(n, edges)
    if bridges:
        print("NO")
        return
    
    # Find perfect matching
    match, match_edge = perfect_matching(n, edges)
    if any(x == -1 for x in match):
        print("NO")
        return
    
    color = [0]*m
    # Color matching edges with 1
    for i in range(n):
        if match_edge[i] != -1:
            color[match_edge[i]] = 1
    
    # Remaining edges form cycles
    # Build graph of remaining edges
    rem_adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        if color[idx] == 0:
            rem_adj[u].append((v, idx))
            rem_adj[v].append((u, idx))
    
    visited = [False]*n
    for start in range(n):
        if not visited[start] and rem_adj[start]:
            # traverse cycle
            cycle_edges = []
            prev = -1
            cur = start
            while True:
                visited[cur] = True
                # pick next unvisited neighbor
                nxt = None
                nxt_eid = None
                for to, eid in rem_adj[cur]:
                    if eid != prev:
                        nxt = to
                        nxt_eid = eid
                        break
                if nxt is None:
                    break
                cycle_edges.append(nxt_eid)
                prev = nxt_eid
                cur = nxt
                if cur == start:
                    break
            # color alternately 2 and 3
            for i, eid in enumerate(cycle_edges):
                color[eid] = 2 if i % 2 == 0 else 3
    
    # Check all colored
    if any(c == 0 for c in color):
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()