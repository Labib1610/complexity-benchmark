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
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    if t <= 1:
        print(0)
        return

    INF = float('inf')
    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0
        
    for mask in range(1, num_masks):
        # 1. Combine submasks
        s = (mask - 1) & mask
        while s > (mask ^ s):
            other = mask ^ s
            dp_s = dp[s]
            dp_other = dp[other]
            dp_mask = dp[mask]
            for u in range(n):
                val = dp_s[u] + dp_other[u]
                if val < dp_mask[u]:
                    dp_mask[u] = val
            s = (s - 1) & mask
            
        # 2. Dijkstra relaxation for this mask
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
                if dp_mask[v] > d + w:
                    dp_mask[v] = d + w
                    heapq.heappush(pq, (d + w, v))
                    
    ans = min(dp[num_masks - 1])
    print(ans)

if __name__ == '__main__':
    solve()