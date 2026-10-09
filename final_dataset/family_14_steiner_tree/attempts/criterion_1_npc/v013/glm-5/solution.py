import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    required = [int(x) - 1 for x in input_data[3:3+t]]
    
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        
    idx = 3 + t
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
        dk = dist[k]
        for i in range(n):
            di = dist[i]
            dik = di[k]
            if dik == INF:
                continue
            for j in range(n):
                if dk[j] + dik < di[j]:
                    di[j] = dk[j] + dik

    if t <= 1:
        print(0)
        return

    # Dreyfus-Wagner algorithm
    # dp[v][mask] = min cost to connect required sites in 'mask' with root at v
    dp = [[INF] * (1 << t) for _ in range(n)]
    
    for i in range(t):
        dp[required[i]][1 << i] = 0
        
    for mask in range(1, 1 << t):
        # Merge submasks
        submask = (mask - 1) & mask
        while submask > 0:
            other = mask ^ submask
            for v in range(n):
                val = dp[v][submask] + dp[v][other]
                if val < dp[v][mask]:
                    dp[v][mask] = val
            submask = (submask - 1) & mask
            
        # Relax edges (Steiner tree DP transition)
        for v in range(n):
            for u in range(n):
                if u == v:
                    continue
                if dist[u][v] + dp[u][mask] < dp[v][mask]:
                    dp[v][mask] = dist[u][v] + dp[u][mask]
                    
    full_mask = (1 << t) - 1
    ans = INF
    for v in range(n):
        if dp[v][full_mask] < ans:
            ans = dp[v][full_mask]
            
    print(ans)

if __name__ == '__main__':
    solve()