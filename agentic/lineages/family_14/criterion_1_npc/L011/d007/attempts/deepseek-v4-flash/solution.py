import sys
input = sys.stdin.readline
INF = 10**18

n, m, t = map(int, input().split())
essentials = list(map(int, input().split()))
essentials = [x-1 for x in essentials]

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

# Floyd-Warshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# DP
full_mask = (1 << t) - 1
dp = [[INF]*n for _ in range(1 << t)]

for i in range(t):
    dp[1 << i][essentials[i]] = 0

# Steiner tree DP
for mask in range(1 << t):
    # merge two submasks
    sub = (mask - 1) & mask
    while sub:
        other = mask ^ sub
        if other < sub:  # avoid duplicate
            sub = (sub - 1) & mask
            continue
        for v in range(n):
            if dp[sub][v] + dp[other][v] < dp[mask][v]:
                dp[mask][v] = dp[sub][v] + dp[other][v]
        sub = (sub - 1) & mask

    # relax via shortest paths
    # We can use Dijkstra-like relaxation, but since n small, we can do simple relaxation
    for _ in range(n):
        updated = False
        for u in range(n):
            if dp[mask][u] < INF:
                for v in range(n):
                    if dist[u][v] < INF:
                        nd = dp[mask][u] + dist[u][v]
                        if nd < dp[mask][v]:
                            dp[mask][v] = nd
                            updated = True
        if not updated:
            break

# Now we need to enforce degree >= 2 for non-essential vertices.
# The above DP may include non-essential vertices with degree 1.
# We can fix by only allowing non-essential vertices to be used as merge points.
# We'll do a second DP that tracks whether a non-essential vertex is "active" as a merge point.

# Since t <= 10, we can do DP over masks and last vertex, but we need to ensure degree constraint.
# A simpler approach: run the DP but when merging at a non-essential vertex, require both submasks non-empty.

# Actually, the above DP already merges at v, so if v is non-essential and both submasks are non-empty, v has degree >= 2.
# But we also need to ensure that when we extend a path to a non-essential vertex, it eventually gets degree >= 2.
# We can handle by only allowing non-essential vertices to be endpoints if they are also used as merge points.

# We'll modify: for non-essential vertices, we only allow them to be in dp[mask][v] if they are used as merge points.
# That means we should not initialize dp with non-essential vertices as endpoints unless they are essential.

# The above DP already only initializes essential vertices. So non-essential vertices only appear via merging or path extension.
# But path extension could make a non-essential vertex an endpoint with degree 1. We must prevent that.

# We can do: after computing dp, we only consider answers where the final root is essential, or if non-essential, it must have degree >= 2.
# Since we can always root the tree at an essential vertex, we can just take min over essential vertices.

ans = min(dp[full_mask][ess] for ess in essentials)
print(ans)