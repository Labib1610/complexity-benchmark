import heapq
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    if t <= 1:
        print(0)
        return
    
    idx = 3
    terminals = [int(x) - 1 for x in input_data[idx:idx + t]]
    idx += t
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        w = int(input_data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << t)]
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
        
    for mask in range(1, 1 << t):
        submask = (mask - 1) & mask
        while submask > 0:
            other = mask ^ submask
            if submask <= other:
                dp_sub = dp[submask]
                dp_oth = dp[other]
                dp_mask = dp[mask]
                for u in range(n):
                    val = dp_sub[u] + dp_oth[u]
                    if val < dp_mask[u]:
                        dp_mask[u] = val
            submask = (submask - 1) & mask
            
        pq = []
        dp_mask = dp[mask]
        for u in range(n):
            if dp_mask[u] < INF:
                pq.append((dp_mask[u], u))
        heapq.heapify(pq)
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp_mask[u]:
                continue
            for v, w in adj[u]:
                if dp_mask[u] + w < dp_mask[v]:
                    dp_mask[v] = dp_mask[u] + w
                    heapq.heappush(pq, (dp_mask[v], v))
                    
    full_mask = (1 << t) - 1
    ans = min(dp[full_mask])
    print(ans)

if __name__ == '__main__':
    solve()