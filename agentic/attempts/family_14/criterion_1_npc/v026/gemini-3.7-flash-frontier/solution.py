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
    terminals = []
    for _ in range(t):
        terminals.append(int(data[idx]) - 1)
        idx += 1
        
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
        # Submask combination
        dp_mask = dp[mask]
        s = (mask - 1) & mask
        while s > (mask ^ s):
            s_comp = mask ^ s
            dp_s = dp[s]
            dp_s_comp = dp[s_comp]
            for u in range(n):
                val = dp_s[u] + dp_s_comp[u]
                if val < dp_mask[u]:
                    dp_mask[u] = val
            s = (s - 1) & mask
            
        # Dijkstra for the current mask
        pq = []
        for u in range(n):
            if dp_mask[u] < INF:
                heapq.heappush(pq, (dp_mask[u], u))
                
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