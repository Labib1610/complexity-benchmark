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
    terminals = [int(x) - 1 for x in data[idx:idx+t]]
    idx += t
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        w = int(data[idx+2])
        idx += 3
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
        low = mask & -mask
        s = (mask - 1) & mask
        while s > 0:
            if s & low:
                rem = mask ^ s
                for v in range(n):
                    cost = dp[s][v] + dp[rem][v]
                    if cost < dp[mask][v]:
                        dp[mask][v] = cost
            s = (s - 1) & mask
            
        pq = []
        for v in range(n):
            if dp[mask][v] < INF:
                heapq.heappush(pq, (dp[mask][v], v))
                
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