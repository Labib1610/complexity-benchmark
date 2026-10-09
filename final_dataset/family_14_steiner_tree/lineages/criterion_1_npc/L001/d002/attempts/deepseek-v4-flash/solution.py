import sys
import heapq

input = sys.stdin.readline

n, m, t = map(int, input().split())
core = list(map(int, input().split()))
core_set = set(core)

# Build graph
graph = [[] for _ in range(n + 1)]
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    edges.append((u, v, w))

# If only one core bank, cost is 0
if t == 1:
    print(0)
    sys.exit()

# Map core banks to indices 0..t-1
core_index = {node: i for i, node in enumerate(core)}

# Compute all-pairs shortest paths between core nodes using Dijkstra
INF = 10**18
dist = [[INF] * (n + 1) for _ in range(t)]
for i, node in enumerate(core):
    d = [INF] * (n + 1)
    d[node] = 0
    pq = [(0, node)]
    while pq:
        du, u = heapq.heappop(pq)
        if du != d[u]:
            continue
        for v, w in graph[u]:
            if d[v] > du + w:
                d[v] = du + w
                heapq.heappush(pq, (d[v], v))
    dist[i] = d

# DP over subsets of terminals
# dp[mask][i] = min cost to connect terminals in mask, ending at terminal i
dp = [[INF] * t for _ in range(1 << t)]
for i in range(t):
    dp[1 << i][i] = 0

# Steiner tree DP
for mask in range(1 << t):
    for i in range(t):
        if dp[mask][i] == INF:
            continue
        # Try to extend to another terminal
        sub = (mask - 1) & mask
        while sub:
            other = mask ^ sub
            if other > sub:
                sub = (sub - 1) & mask
                continue
            for j in range(t):
                if (other >> j) & 1:
                    dp[mask | (1 << j)][j] = min(
                        dp[mask | (1 << j)][j],
                        dp[mask][i] + dist[i][core[j]]
                    )
            sub = (sub - 1) & mask

# Combine subsets
full_mask = (1 << t) - 1
best = INF
for i in range(t):
    best = min(best, dp[full_mask][i])

print(best)