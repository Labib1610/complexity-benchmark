import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    critical = set()
    for _ in range(t):
        critical.add(int(next(it)))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Dijkstra from each critical node
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for s in range(1, n + 1):
        if s not in critical:
            continue
        d = dist[s]
        d[s] = 0
        pq = [(0, s)]
        while pq:
            du, u = heapq.heappop(pq)
            if du > d[u]:
                continue
            for v, w in adj[u]:
                nd = du + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # Steiner tree DP
    crit_list = list(critical)
    num_crit = len(crit_list)
    crit_index = {v: i for i, v in enumerate(crit_list)}
    
    INF = float('inf')
    dp = [[INF] * (n + 1) for _ in range(1 << num_crit)]
    
    for i, v in enumerate(crit_list):
        dp[1 << i][v] = 0
    
    for mask in range(1, 1 << num_crit):
        # Combine submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            for v in range(1, n + 1):
                if dp[sub][v] < INF and dp[other][v] < INF:
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & mask
        
        # Dijkstra-like relaxation
        pq = []
        for v in range(1, n + 1):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        
        while pq:
            du, u = heapq.heappop(pq)
            if du > dp[mask][u]:
                continue
            for v, w in adj[u]:
                nd = du + w
                if nd < dp[mask][v]:
                    dp[mask][v] = nd
                    heapq.heappush(pq, (nd, v))
    
    full_mask = (1 << num_crit) - 1
    print(min(dp[full_mask]))

if __name__ == "__main__":
    solve()