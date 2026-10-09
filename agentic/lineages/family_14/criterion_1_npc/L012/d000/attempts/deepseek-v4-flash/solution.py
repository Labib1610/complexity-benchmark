import sys
import heapq

input = sys.stdin.readline

n, m, t = map(int, input().split())
primary = list(map(int, input().split()))
primary_set = set(primary)

# Build graph
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# If only one primary language, cost is 0
if t == 1:
    print(0)
    sys.exit()

# Map primary languages to bit positions
idx = {lang: i for i, lang in enumerate(primary)}

# Step 1: Compute shortest paths between all pairs of primary languages
# We can run Dijkstra from each primary language
INF = 10**18
dist = [[INF] * t for _ in range(t)]

for i, lang in enumerate(primary):
    d = [INF] * (n + 1)
    d[lang] = 0
    pq = [(0, lang)]
    while pq:
        du, u = heapq.heappop(pq)
        if du != d[u]:
            continue
        for v, w in graph[u]:
            if d[v] > du + w:
                d[v] = du + w
                heapq.heappush(pq, (d[v], v))
    for j, other in enumerate(primary):
        dist[i][j] = d[other]

# Step 2: Steiner tree DP over subsets of primary languages
# dp[mask][i] = min cost to connect subset mask with i as root (i in 0..t-1)
dp = [[INF] * t for _ in range(1 << t)]
for i in range(t):
    dp[1 << i][i] = 0

# For each subset, try merging two smaller subsets
for mask in range(1, 1 << t):
    # Try splitting mask into two non-empty subsets
    sub = (mask - 1) & mask
    while sub:
        other = mask ^ sub
        if sub < other:  # avoid duplicate work
            for i in range(t):
                if dp[sub][i] == INF:
                    continue
                for j in range(t):
                    if dp[other][j] == INF:
                        continue
                    # connect i and j via shortest path
                    cost = dp[sub][i] + dp[other][j] + dist[i][j]
                    if cost < dp[mask][i]:
                        dp[mask][i] = cost
                    if cost < dp[mask][j]:
                        dp[mask][j] = cost
        sub = (sub - 1) & mask

    # Also relax within same mask using shortest paths
    # (like running Dijkstra on the dp states)
    # We can do a simple relaxation: for each i, try to improve via j
    for _ in range(t):
        updated = False
        for i in range(t):
            if dp[mask][i] == INF:
                continue
            for j in range(t):
                if dp[mask][i] + dist[i][j] < dp[mask][j]:
                    dp[mask][j] = dp[mask][i] + dist[i][j]
                    updated = True
        if not updated:
            break

full_mask = (1 << t) - 1
ans = min(dp[full_mask][i] for i in range(t))
print(ans)