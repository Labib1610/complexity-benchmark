import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    B = int(next(it))
    
    required = [int(next(it)) - 1 for _ in range(t)]
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    if t == 0:
        print("YES")
        return
    
    if t == 1:
        print("YES")
        return

    INF = float('inf')
    num_masks = 1 << t
    
    dp = [[INF] * n for _ in range(num_masks)]
    how = [[None] * n for _ in range(num_masks)]
    
    for i in range(t):
        r = required[i]
        dp[1 << i][r] = 0
        how[1 << i][r] = ('base',)

    for mask in range(1, num_masks):
        # 1. Submask transitions
        submask = (mask - 1) & mask
        while submask > 0:
            rem = mask ^ submask
            if rem < submask:
                dp_sub = dp[submask]
                dp_rem = dp[rem]
                dp_mask = dp[mask]
                how_mask = how[mask]
                for v in range(n):
                    val = dp_sub[v] + dp_rem[v]
                    if val < dp_mask[v]:
                        dp_mask[v] = val
                        how_mask[v] = ('split', submask)
            submask = (submask - 1) & mask
            
        # 2. Dijkstra transitions
        pq = []
        dp_mask = dp[mask]
        how_mask = how[mask]
        for v in range(n):
            if dp_mask[v] < INF:
                heapq.heappush(pq, (dp_mask[v], v))
                
        while pq:
            d, u = heapq.heappop(pq)
            if d > dp_mask[u]:
                continue
            for v, w in adj[u]:
                if dp_mask[u] + w < dp_mask[v]:
                    dp_mask[v] = dp_mask[u] + w
                    how_mask[v] = ('edge', u)
                    heapq.heappush(pq, (dp_mask[v], v))

    full_mask = num_masks - 1
    best_cost = INF
    best_root = -1
    for v in range(n):
        if dp[full_mask][v] < best_cost:
            best_cost = dp[full_mask][v]
            best_root = v

    if best_cost > B or best_root == -1:
        print("NO")
        return

    edges = set()
    
    def reconstruct(mask, v):
        info = how[mask][v]
        if not info or info[0] == 'base':
            return
        if info[0] == 'edge':
            u = info[1]
            edges.add((min(u, v), max(u, v)))
            reconstruct(mask, u)
        elif info[0] == 'split':
            sub = info[1]
            rem = mask ^ sub
            reconstruct(sub, v)
            reconstruct(rem, v)

    reconstruct(full_mask, best_root)
    
    print("YES")
    for u, v in edges:
        print(f"{u + 1} {v + 1}")

if __name__ == '__main__':
    solve()