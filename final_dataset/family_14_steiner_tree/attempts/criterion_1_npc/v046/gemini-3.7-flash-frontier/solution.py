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
    terminals = [int(data[ptr + i]) - 1 for i in range(t)]
    ptr += t
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(data[ptr]) - 1
        v = int(data[ptr + 1]) - 1
        w = int(data[ptr + 2])
        ptr += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    num_masks = 1 << t
    INF = float('inf')
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
        
    for mask in range(1, num_masks):
        # 1. Combine submasks
        # Fix the lowest set bit to avoid duplicate partitions
        low_bit = mask & (-mask)
        sub = (mask - 1) & mask
        while sub > 0:
            if sub & low_bit:
                comp = mask ^ sub
                dp_sub = dp[sub]
                dp_comp = dp[comp]
                dp_mask = dp[mask]
                for v in range(n):
                    val = dp_sub[v] + dp_comp[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
            sub = (sub - 1) & mask
            
        # 2. Dijkstra step to propagate within the graph
        heap = []
        dp_mask = dp[mask]
        for v in range(n):
            if dp_mask[v] < INF:
                heap.append((dp_mask[v], v))
        heapq.heapify(heap)
        
        while heap:
            d, u = heapq.heappop(heap)
            if d > dp_mask[u]:
                continue
            for v, w in adj[u]:
                if dp_mask[v] > d + w:
                    dp_mask[v] = d + w
                    heapq.heappush(heap, (d + w, v))
                    
    full_mask = num_masks - 1
    ans = min(dp[full_mask])
    print(ans)

if __name__ == '__main__':
    solve()