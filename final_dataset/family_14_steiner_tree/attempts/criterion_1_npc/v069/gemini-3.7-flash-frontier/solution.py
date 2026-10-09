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
        
    if t <= 1:
        print(0)
        return

    INF = float('inf')
    num_masks = 1 << t
    dp = [[INF] * n for _ in range(num_masks)]
    
    for i, term in enumerate(terminals):
        dp[1 << i][term] = 0
        
    for mask in range(1, num_masks):
        # 1. Combine submasks
        submask = (mask - 1) & mask
        while submask > 0:
            other = mask ^ submask
            if submask <= other:
                dp_sub = dp[submask]
                dp_other = dp[other]
                dp_mask = dp[mask]
                for u in range(n):
                    val = dp_sub[u] + dp_other[u]
                    if val < dp_mask[u]:
                        dp_mask[u] = val
            submask = (submask - 1) & mask
            
        # 2. Dijkstra relaxation
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
                if dp_mask[u] + w < dp_mask[v]:
                    dp_mask[v] = dp_mask[u] + w
                    heapq.heappush(pq, (dp_mask[v], v))
                    
    ans = min(dp[num_masks - 1])
    print(ans)

if __name__ == '__main__':
    main()