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
    
    ptr = 3
    terminals = []
    for _ in range(t):
        terminals.append(int(data[ptr]) - 1)
        ptr += 1
        
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[ptr]) - 1
        v = int(data[ptr+1]) - 1
        w = int(data[ptr+2])
        ptr += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    INF = float('inf')
    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0
        
    for mask in range(1, num_masks):
        # Merge submasks
        submask = (mask - 1) & mask
        while submask > (mask ^ submask):
            other = mask ^ submask
            for u in range(n):
                val = dp[submask][u] + dp[other][u]
                if val < dp[mask][u]:
                    dp[mask][u] = val
            submask = (submask - 1) & mask
            
        # Dijkstra step
        pq = []
        for u in range(n):
            if dp[mask][u] < INF:
                heapq.heappush(pq, (dp[mask][u], u))
                
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp[mask][u]:
                continue
            for v, w in adj[u]:
                if dp[mask][v] > d + w:
                    dp[mask][v] = d + w
                    heapq.heappush(pq, (dp[mask][v], v))
                    
    ans = min(dp[num_masks - 1])
    print(ans)

if __name__ == '__main__':
    solve()