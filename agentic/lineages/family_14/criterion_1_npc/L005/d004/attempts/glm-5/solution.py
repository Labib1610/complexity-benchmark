import sys
import heapq

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    key_assets = [int(next(it)) for _ in range(t)]
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Dijkstra from each key asset
    dist = [[float('inf')] * (n + 1) for _ in range(t)]
    for i, start in enumerate(key_assets):
        d = dist[i]
        d[start] = 0
        pq = [(0, start)]
        while pq:
            cur_d, u = heapq.heappop(pq)
            if cur_d > d[u]:
                continue
            for v, w in adj[u]:
                nd = cur_d + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(pq, (nd, v))
    
    # DP over subsets of key assets
    full_mask = (1 << t) - 1
    dp = [float('inf')] * (1 << t)
    dp[0] = 0
    
    # Precompute cost to connect subset S through node v
    # cost[S][v] = sum of min dist from each key in S to v
    # We compute on the fly
    
    for mask in range(1 << t):
        if dp[mask] == float('inf'):
            continue
        
        # Find first key not in mask
        remaining = full_mask ^ mask
        if remaining == 0:
            continue
        
        # Get list of keys not in mask
        not_in_mask = []
        for i in range(t):
            if not (mask & (1 << i)):
                not_in_mask.append(i)
        
        # Try adding subsets of remaining keys
        sub = remaining
        while sub > 0:
            # Get indices of keys in this subset
            subset_keys = []
            temp = sub
            idx = 0
            while temp:
                if temp & 1:
                    subset_keys.append(not_in_mask[idx])
                temp >>= 1
                idx += 1
            
            # Compute min cost to connect these keys
            best = float('inf')
            for v in range(1, n + 1):
                cost = 0
                for i in subset_keys:
                    cost += dist[i][v]
                if cost < best:
                    best = cost
            
            new_mask = mask | sub
            if dp[mask] + best < dp[new_mask]:
                dp[new_mask] = dp[mask] + best
            
            sub = (sub - 1) & remaining
    
    print(dp[full_mask])

if __name__ == "__main__":
    solve()