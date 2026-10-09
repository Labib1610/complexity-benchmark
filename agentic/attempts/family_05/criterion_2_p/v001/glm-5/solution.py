import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # pilot x is paired with aircraft y; store allowed routes for each pilot
    routes = [None] * (k + 1)
    aircraft_of = [0] * (k + 1)
    
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        if routes[x] is None:
            routes[x] = []
        routes[x].append(z)
        aircraft_of[x] = y
    
    # Build bipartite graph: pilots 1..k on left, routes 1..k on right
    # Hopcroft-Karp
    INF = float('inf')
    pair_u = [0] * (k + 1)  # pair_u[u] = v matched to pilot u
    pair_v = [0] * (k + 1)  # pair_v[v] = u matched to route v
    dist = [0] * (k + 1)
    
    adj = [[] for _ in range(k + 1)]
    for x in range(1, k + 1):
        if routes[x] is not None:
            for z in routes[x]:
                adj[x].append(z)
    
    from collections import deque
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[0] != INF
    
    def dfs(u):
        for v in adj[u]:
            if dist[pair_v[v]] == dist[u] + 1:
                if dfs(pair_v[v]):
                    pair_v[v] = u
                    pair_u[u] = v
                    return True
        dist[u] = INF
        return False
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == k:
        out = ["YES"]
        for u in range(1, k + 1):
            out.append(f"{u} {aircraft_of[u]} {pair_u[u]}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()