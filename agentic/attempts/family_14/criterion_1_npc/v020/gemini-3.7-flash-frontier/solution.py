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
    
    if t <= 1:
        print(0)
        return
    
    idx = 3
    primaries = [int(data[idx + i]) - 1 for i in range(t)]
    idx += t
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        w = int(data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    num_masks = 1 << t
    INF = float('inf')
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i in range(t):
        dp[1 << i][primaries[i]] = 0
        
    for mask in range(1, num_masks):
        # Combine submasks
        # To iterate over proper submasks:
        submask = (mask - 1) & mask
        while submask > (mask ^ submask):
            other = mask ^ submask
            dp_sub = dp[submask]
            dp_other = dp[other]
            dp_mask = dp[mask]
            for v in range(n):
                val = dp_sub[v] + dp_other[v]
                if val < dp_mask[v]:
                    dp_mask[v] = val
            submask = (submask - 1) & mask
            
        # Run Dijkstra on current mask
        pq = []
        dp_mask = dp[mask]
        for v in range(n):
            if dp_mask[v] < INF:
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