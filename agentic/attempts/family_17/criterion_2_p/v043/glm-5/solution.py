import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    # Build adjacency list: lower-tier (1..q) -> upper-tier (q+1..2q)
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
    
    # Hopcroft-Karp algorithm for maximum bipartite matching
    # Left side: lower-tier assets 1..q
    # Right side: upper-tier assets q+1..2q, mapped to 1..q by subtracting q
    
    pair_u = [0] * (q + 1)  # pair_u[u] = v (upper-tier) matched to u, 0 if unmatched
    pair_v = [0] * (q + 1)  # pair_v[v] = u (lower-tier) matched to v, 0 if unmatched
    dist = [0] * (q + 1)
    
    from collections import deque
    
    INF = 10**9
    
    def bfs():
        queue = deque()
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for b in adj[u]:
                    v = b - q
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[0] != INF
    
    def dfs(u):
        if u != 0:
            for b in adj[u]:
                v = b - q
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = b
                        return True
            dist[u] = INF
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        out = ["YES"]
        for u in range(1, q + 1):
            out.append(f"{u} {pair_u[u]}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

solve()