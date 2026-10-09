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
    
    if t <= 1:
        print(0)
        return
    
    ptr = 3
    terminals = [int(x) - 1 for x in data[ptr:ptr+t]]
    ptr += t
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[ptr]) - 1
        v = int(data[ptr+1]) - 1
        w = int(data[ptr+2])
        ptr += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    num_masks = 1 << t
    INF = float('inf')
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0
        
    for mask in range(1, num_masks):
        # Submask merging
        submask = (mask - 1) & mask
        while submask > (mask ^ submask):
            other = mask ^ submask
            for u in range(n):
                val = dp[submask][u] + dp[other][u]
                if val < dp[mask][u]:
                    dp[mask][u] = val
            submask = (submask - 1) & mask
            
        # Dijkstra relaxation
        pq = []
        for u in range(n):
            if dp[mask][u] < INF:
                heapq.heappush(pq, (dp[mask][u], u))
                
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp[mask][u]:
                continue
            for v, w in adj[u]:
                if dp[mask][u] + w < dp[mask][v]:
                    dp[mask][v] = dp[mask][u] + w
                    heapq.heappush(pq, (dp[mask][v], v))
                    
    ans = min(dp[num_masks - 1])
    print(ans)

if __name__ == '__main__':
    solve()