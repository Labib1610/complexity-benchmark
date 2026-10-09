import sys
from heapq import heappush, heappop

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    primaries = []
    for i in range(t):
        primaries.append(int(input_data[idx]) - 1); idx += 1
    
    adj = [[] for _ in range(n)]
    edges = []
    for i in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        w = int(input_data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    # dp[S][v] = min cost to connect terminals in S, tree includes v
    INF = float('inf')
    full = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]
    
    # Initialize single terminals
    for i in range(t):
        dp[1 << i][primaries[i]] = 0
    
    # For each subset, do Dijkstra to propagate
    for S in range(1, 1 << t):
        # First, merge subsets
        sub = (S - 1) & S
        while sub > 0:
            other = S ^ sub
            if sub < other or True:  # process all
                for v in range(n):
                    if dp[sub][v] < INF and dp[other][v] < INF:
                        dp[S][v] = min(dp[S][v], dp[sub][v] + dp[other][v])
            sub = (sub - 1) & S
        
        # Dijkstra to relax dp[S][v] using shortest paths
        pq = []
        for v in range(n):
            if dp[S][v] < INF:
                heappush(pq, (dp[S][v], v))
        
        while pq:
            d, u = heappop(pq)
            if d > dp[S][u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dp[S][v]:
                    dp[S][v] = nd
                    heappush(pq, (nd, v))
    
    result = min(dp[full])
    print(result)

solve()