import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    core = [int(input_data[idx + i]) - 1 for i in range(t)]
    idx += t

    INF = 10**18
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        w = int(input_data[idx+2])
        idx += 3
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            dik = dist[i][k]
            for j in range(n):
                nd = dik + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd
    
    full_mask = (1 << t) - 1
    dp = [[INF] * n for _ in range(1 << t)]
    for i, c in enumerate(core):
        dp[1 << i][c] = 0
    
    # Enumerate masks in increasing order
    for mask in range(1 << t):
        # merge submasks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # avoid double count
                for v in range(n):
                    val = dp[sub][v] + dp[other][v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            sub = (sub - 1) & mask
        
        # Relax using all-pairs shortest paths
        # Dijkstra-like
        visited = [False] * n
        for _ in range(n):
            u = -1
            best = INF
            for v in range(n):
                if not visited[v] and dp[mask][v] < best:
                    best = dp[mask][v]
                    u = v
            if u == -1:
                break
            visited[u] = True
            du = dp[mask][u]
            for v in range(n):
                if du + dist[u][v] < dp[mask][v]:
                    dp[mask][v] = du + dist[u][v]
    
    ans = min(dp[full_mask])
    print(ans)

if __name__ == "__main__":
    solve()