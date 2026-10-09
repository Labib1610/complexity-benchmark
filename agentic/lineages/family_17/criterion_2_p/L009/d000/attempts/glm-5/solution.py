import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    # Controllers: 1..q, Platforms: q+1..2q
    # We need a perfect matching in a bipartite graph
    
    # Build adjacency list for controllers
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
    
    # Hopcroft-Karp algorithm
    INF = q + 5
    pair_u = [0] * (q + 1)  # pair_u[u] = v matched to controller u
    pair_v = [0] * (2 * q + 1)  # pair_v[v] = u matched to platform v
    dist = [0] * (q + 1)
    
    from collections import deque
    
    def bfs():
        dq = deque()
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while dq:
            u = dq.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if pair_v[v] == 0:
                        if dist[0] == INF:
                            dist[0] = dist[u] + 1
                    elif dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        dq.append(pair_v[v])
        return dist[0] != INF
    
    def dfs(u):
        for v in adj[u]:
            if pair_v[v] == 0 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False
    
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, pair_u[u])
    else:
        print("NO")

solve()