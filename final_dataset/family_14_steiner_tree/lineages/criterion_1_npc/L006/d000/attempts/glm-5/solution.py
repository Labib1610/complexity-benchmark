import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    required = [int(x) for x in input_data[3:3+t]]
    
    # If there is 0 or 1 required site, no cabling is needed
    if t <= 1:
        print(0)
        return
        
    # Initialize distance matrix for Floyd-Warshall
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
            
    # Floyd-Warshall to find all-pairs shortest paths
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if dist[i][k] == INF:
                continue
            for j in range(1, n + 1):
                if dist[k][j] == INF:
                    continue
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    # Steiner Tree DP for the required sites
    # dp[mask][v] = min cost to connect sites of `mask` ending at node `v`
    dp = [[INF] * (n + 1) for _ in range(1 << t)]
    
    for i in range(t):
        node = required[i]
        dp[1 << i][node] = 0
        
    for mask in range(1, 1 << t):
        # Propagate: dp[mask][v] = min(dp[mask][v], dp[mask][u] + dist[u][v])
        for u in range(1, n + 1):
            if dp[mask][u] == INF:
                continue
            for v in range(1, n + 1):
                if dist[u][v] == INF:
                    continue
                if dp[mask][u] + dist[u][v] < dp[mask][v]:
                    dp[mask][v] = dp[mask][u] + dist[u][v]
                    
        # Merge submasks
        submask = mask
        while submask > 0:
            complement = mask ^ submask
            if complement < submask:
                for v in range(1, n + 1):
                    if dp[submask][v] != INF and dp[complement][v] != INF:
                        if dp[submask][v] + dp[complement][v] < dp[mask][v]:
                            dp[mask][v] = dp[submask][v] + dp[complement][v]
            submask = (submask - 1) & mask
            
    full_mask = (1 << t) - 1
    ans = min(dp[full_mask][v] for v in range(1, n + 1))
    print(ans)

if __name__ == '__main__':
    solve()