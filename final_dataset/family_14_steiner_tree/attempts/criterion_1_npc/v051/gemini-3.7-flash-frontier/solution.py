import sys
import heapq

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    terminals = [int(x) - 1 for x in data[3:3+t]]
    
    adj = [[] for _ in range(n)]
    idx = 3 + t
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        w = int(data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3
        
    if t <= 1:
        print(0)
        return

    num_masks = 1 << t
    INF = float('inf')
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0
        
    for mask in range(1, num_masks):
        # Combine submasks
        # To avoid double counting and symmetry, we can iterate submasks
        submask = (mask - 1) & mask
        while submask > (mask ^ submask):
            other = mask ^ submask
            dp_mask = dp[mask]
            dp_sub = dp[submask]
            dp_oth = dp[other]
            for u in range(n):
                val = dp_sub[u] + dp_oth[u]
                if val < dp_mask[u]:
                    dp_mask[u] = val
            submask = (submask - 1) & mask
            
        # Run Dijkstra for this mask
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