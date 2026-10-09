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
    
    idx = 3
    terminals = [int(data[idx + i]) - 1 for i in range(t)]
    idx += t
    
    if t <= 1:
        print(0)
        return

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        w = int(data[idx+2])
        idx += 3
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
            dp_mask = dp[mask]
            dp_sub = dp[sub]
            dp_other = dp[other]
            for u in range(n):
                val = dp_sub[u] + dp_other[u]
                if val < dp_mask[u]:
                    dp_mask[u] = val
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
                if dp_mask[v] > d + w:
                    dp_mask[v] = d + w
                    heapq.heappush(pq, (d + w, v))
                    
    ans = dp[num_masks - 1][terminals[0]]
    print(ans)

if __name__ == '__main__':
    solve()