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
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
        
    for mask in range(1, num_masks):
        # 1. Combine submasks
        submask = (mask - 1) & mask
        while submask > 0:
            other = mask ^ submask
            if submask <= other:
                dp_sub = dp[submask]
                dp_other = dp[other]
                dp_mask = dp[mask]
                for v in range(n):
                    val = dp_sub[v] + dp_other[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
            submask = (submask - 1) & mask
            
        # 2. Dijkstra relaxation
        dp_mask = dp[mask]
        pq = [(dp_mask[v], v) for v in range(n) if dp_mask[v] < INF]
        heapq.heapify(pq)
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp_mask[u]:
                continue
            for v, w in adj[u]:
                if d + w < dp_mask[v]:
                    dp_mask[v] = d + w
                    heapq.heappush(pq, (d + w, v))
                    
    ans = min(dp[num_masks - 1])
    print(ans)

if __name__ == '__main__':
    solve()