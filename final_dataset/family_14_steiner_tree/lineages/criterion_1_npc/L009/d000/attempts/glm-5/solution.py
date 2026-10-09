import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    required = set(int(input_data[3 + i]) for i in range(t))
    
    # Initialize adjacency matrix with infinity
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][i] = 0
        
    idx = 3 + t
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
            
    # Floyd-Warshall algorithm to find all-pairs shortest paths
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if dist[i][k] == INF:
                continue
            for j in range(1, n + 1):
                if dist[k][j] == INF:
                    continue
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    # If there's only 1 required site, no cabling is needed
    if t <= 1:
        print(0)
        return
        
    req_list = list(required)
    t_val = len(req_list)
    
    # DP to find Minimum Steiner Tree
    # dp[mask][v] = min cost to connect required sites in 'mask' ending at node v
    dp = [[INF] * (n + 1) for _ in range(1 << t_val)]
    
    for i in range(t_val):
        v = req_list[i]
        dp[1 << i][v] = 0
        
    for mask in range(1, 1 << t_val):
        # Combine two disjoint subsets of required sites
        sub = mask
        while sub > 0:
            sub = (sub - 1) & mask
            complement = mask ^ sub
            if sub < complement:
                for v in range(1, n + 1):
                    if dp[sub][v] + dp[complement][v] < dp[mask][v]:
                        dp[mask][v] = dp[sub][v] + dp[complement][v]
                        
        # Extend the tree by the shortest path to any other node
        for v in range(1, n + 1):
            if dp[mask][v] == INF:
                continue
            for u in range(1, n + 1):
                if dist[v][u] == INF:
                    continue
                if dp[mask][v] + dist[v][u] < dp[mask][u]:
                    dp[mask][u] = dp[mask][v] + dist[v][u]
                    
    full_mask = (1 << t_val) - 1
    ans = min(dp[full_mask])
    print(ans)

if __name__ == '__main__':
    solve()