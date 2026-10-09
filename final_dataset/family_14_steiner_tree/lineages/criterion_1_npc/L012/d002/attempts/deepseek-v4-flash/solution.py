import sys

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = list(map(int, input().split()))
    terminals = [x-1 for x in terminals]  # zero-index
    
    INF = 10**15
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        if w < dist[u][v]:
            dist[u][v] = w
        if w < dist[v][u]:
            dist[v][u] = w
    
    # Floyd-Warshall
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(n):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    
    # If t == 1, answer is 0 (start at that terminal)
    if t == 1:
        print(0)
        return
    
    full_mask = 1 << t
    # dp[mask][v]
    dp = [[INF]*n for _ in range(full_mask)]
    
    # Initialize single terminal states
    for i in range(t):
        dp[1 << i][terminals[i]] = 0
    
    # Combine submasks
    for mask in range(1, full_mask):
        # First combine smaller masks
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if sub < other:  # only process once per pair
                for v in range(n):
                    if dp[sub][v] < INF and dp[other][v] < INF:
                        val = dp[sub][v] + dp[other][v]
                        if val < dp[mask][v]:
                            dp[mask][v] = val
            sub = (sub - 1) & mask
        
        # Relax using shortest paths
        # Run Dijkstra-like relaxation? Since n is small, just do Floyd-like relaxation
        for k in range(n):
            if dp[mask][k] == INF:
                continue
            dk = dist[k]
            dpm = dp[mask]
            for j in range(n):
                nd = dpm[k] + dk[j]
                if nd < dpm[j]:
                    dpm[j] = nd
    
    ans = INF
    for v in range(n):
        ans = min(ans, dp[full_mask-1][v])
    
    print(ans)

if __name__ == "__main__":
    solve()