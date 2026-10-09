import heapq
from itertools import combinations

def solve():
    n, m, t = map(int, input().split())
    targets = list(map(int, input().split()))
    targets = [x - 1 for x in targets]
    
    if t <= 1:
        print(0)
        return
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    T = len(targets)
    target_set = frozenset(targets)
    target_index = {x: i for i, x in enumerate(targets)}
    
    INF = float('inf')
    size = 1 << T
    dp = [[INF] * n for _ in range(size)]
    
    for i, v in enumerate(targets):
        dp[1 << i][v] = 0
    
    for mask in range(1, size):
        for v in range(n):
            sub = (mask - 1) & mask
            while sub > 0:
                other = mask ^ sub
                if other < sub:
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
                sub = (sub - 1) & mask
        
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
        
        while pq:
            d, v = heapq.heappop(pq)
            if d > dp[mask][v]:
                continue
            for u, w in adj[v]:
                nd = d + w
                if nd < dp[mask][u]:
                    dp[mask][u] = nd
                    heapq.heappush(pq, (nd, u))
    
    ans = min(dp[size - 1][v] for v in range(n))
    print(ans)

solve()