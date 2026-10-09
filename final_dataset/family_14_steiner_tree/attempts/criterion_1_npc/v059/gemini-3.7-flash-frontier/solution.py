import sys
import heapq

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    terminals = [int(x) - 1 for x in data[3:3 + t]]
    
    adj = [[] for _ in range(n)]
    idx = 3 + t
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        w = int(data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    INF = float('inf')
    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0
        
    for mask in range(1, num_masks):
        # 1. Combine submasks
        submask = (mask - 1) & mask
        while submask > (mask ^ submask):
            other = mask ^ submask
            dp_mask = dp[mask]
            dp_sub = dp[submask]
            dp_oth = dp[other]
            for v in range(n):
                val = dp_sub[v] + dp_oth[v]
                if val < dp_mask[v]:
                    dp_mask[v] = val
            submask = (submask - 1) & mask
            
        # 2. Dijkstra to propagate across edges
        pq = []
        dp_mask = dp[mask]
        for v in range(n):
            if dp_mask[v] != INF:
                pq.append((dp_mask[v], v))
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
    main()