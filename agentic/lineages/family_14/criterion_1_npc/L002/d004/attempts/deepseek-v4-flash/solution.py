import sys
import heapq

input = sys.stdin.readline

n, m, t = map(int, input().split())
targets = list(map(int, input().split()))
target_set = set(targets)

# Build graph
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# If only one target, cost is 0
if t == 1:
    print(0)
    sys.exit()

# Map target indices to 0..t-1
target_index = {v: i for i, v in enumerate(targets)}

# Compute shortest paths between all pairs of target nodes
INF = 10**18
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0
    pq = [(0, i)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[i][u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[i][v]:
                dist[i][v] = nd
                heapq.heappush(pq, (nd, v))

# DP over subsets of targets
# dp[mask][v] = min cost to connect targets in mask, ending at vertex v
dp = [[INF] * (n + 1) for _ in range(1 << t)]
for i, target in enumerate(targets):
    dp[1 << i][target] = 0

# First, combine subsets via a vertex
for mask in range(1 << t):
    # Subset splitting
    sub = (mask - 1) & mask
    while sub:
        other = mask ^ sub
        if sub < other:  # avoid double work
            for v in range(1, n + 1):
                if dp[sub][v] < INF and dp[other][v] < INF:
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
        sub = (sub - 1) & mask
    # Dijkstra-like relaxation for this mask
    pq = [(dp[mask][v], v) for v in range(1, n + 1) if dp[mask][v] < INF]
    heapq.heapify(pq)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dp[mask][u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dp[mask][v]:
                dp[mask][v] = nd
                heapq.heappush(pq, (nd, v))

full_mask = (1 << t) - 1
ans = min(dp[full_mask][v] for v in range(1, n + 1))
print(ans)