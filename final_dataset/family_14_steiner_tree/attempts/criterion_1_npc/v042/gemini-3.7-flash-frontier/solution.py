import sys
import heapq

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    n = int(next(iterator))
    m = int(next(iterator))
    t = int(next(iterator))
    
    terminals = [int(next(iterator)) - 1 for _ in range(t)]
    
    if t <= 1:
        print(0)
        return
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    num_masks = 1 << t
    INF = float('inf')
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
        
    for mask in range(1, num_masks):
        # Combine submasks
        sub = (mask - 1) & mask
        while sub > (mask ^ sub):
            other = mask ^ sub
            dp_sub = dp[sub]
            dp_other = dp[other]
            dp_mask = dp[mask]
            for u in range(n):
                cost = dp_sub[u] + dp_other[u]
                if cost < dp_mask[u]:
                    dp_mask[u] = cost
            sub = (sub - 1) & mask
            
        # Dijkstra for the current mask
        pq = []
        dp_mask = dp[mask]
        for u in range(n):
            if dp_mask[u] < INF:
                heapq.heappush(pq, (dp_mask[u], u))
                
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp_mask[u]:
                continue
            for v, w in adj[u]:
                if dp_mask[u] + w < dp_mask[v]:
                    dp_mask[v] = dp_mask[u] + w
                    heapq.heappush(pq, (dp_mask[v], v))
                    
    ans = min(dp[num_masks - 1])
    print(ans)

if __name__ == '__main__':
    solve()