import sys
input = sys.stdin.readline
INF = 10**18

n, m, t = map(int, input().split())
targets = list(map(int, input().split()))
targets = [x-1 for x in targets]

# adjacency matrix
dist = [[INF]*n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w < dist[u][v]:
        dist[u][v] = w
        dist[v][u] = w

# Floyd-Warshall to get shortest paths
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# DP over subsets
# dp[mask][v] = min cost to connect terminals in mask with v as root
full_mask = 1 << t
dp = [[INF]*n for _ in range(full_mask)]

# Initialize: single terminal
for i, term in enumerate(targets):
    dp[1 << i][term] = 0

# Dreyfus-Wagner
for mask in range(1, full_mask):
    # split mask into two non-empty submasks
    sub = (mask - 1) & mask
    while sub:
        other = mask ^ sub
        if other:
            for v in range(n):
                if dp[sub][v] + dp[other][v] < dp[mask][v]:
                    dp[mask][v] = dp[sub][v] + dp[other][v]
        sub = (sub - 1) & mask
    # relax via shortest paths
    for v in range(n):
        if dp[mask][v] < INF:
            for u in range(n):
                if dp[mask][v] + dist[v][u] < dp[mask][u]:
                    dp[mask][u] = dp[mask][v] + dist[v][u]

ans = min(dp[full_mask-1][v] for v in range(n))
print(ans)