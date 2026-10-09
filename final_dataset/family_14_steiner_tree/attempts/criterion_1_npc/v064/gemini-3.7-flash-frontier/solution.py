import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    t = int(next(iterator))
    
    terminals = [int(next(iterator)) - 1 for _ in range(t)]
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    INF = float('inf')
    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
        
    for mask in range(1, num_masks):
        dp_mask = dp[mask]
        
        # Submask partition
        sub = (mask - 1) & mask
        while sub > (mask ^ sub):
            other = mask ^ sub
            dp_sub = dp[sub]
            dp_other = dp[other]
            for u in range(n):
                val = dp_sub[u] + dp_other[u]
                if val < dp_mask[u]:
                    dp_mask[u] = val
            sub = (sub - 1) & mask
            
        # Dijkstra
        heap = [(dp_mask[u], u) for u in range(n) if dp_mask[u] < INF]
        heapq.heapify(heap)
        
        while heap:
            d, u = heapq.heappop(heap)
            if d > dp_mask[u]:
                continue
            for v, w in adj[u]:
                if d + w < dp_mask[v]:
                    dp_mask[v] = d + w
                    heapq.heappush(heap, (d + w, v))
                    
    ans = min(dp[(1 << t) - 1])
    print(ans)

if __name__ == '__main__':
    solve()