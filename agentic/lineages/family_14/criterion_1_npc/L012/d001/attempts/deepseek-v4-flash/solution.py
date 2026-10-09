import sys
import heapq

input = sys.stdin.readline

n, m, t = map(int, input().split())
priority = list(map(int, input().split()))
priority_set = set(priority)

# Build graph
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))

# If only one priority language, cost is 0
if t == 1:
    print(0)
    sys.exit()

# Map priority languages to bit indices
prio_index = {lang: i for i, lang in enumerate(priority)}

# dp[mask][v] = min cost to connect the set 'mask' of priority nodes, ending at node v
INF = 10**18
dp = [[INF] * n for _ in range(1 << t)]

# Initialize: for each priority node, cost 0 to reach itself
for i, lang in enumerate(priority):
    dp[1 << i][lang - 1] = 0

# Dijkstra for each mask to propagate shortest paths
for mask in range(1 << t):
    # Run Dijkstra from all nodes in this mask
    pq = [(dp[mask][v], v) for v in range(n) if dp[mask][v] < INF]
    heapq.heapify(pq)
    while pq:
        d, u = heapq.heappop(pq)
        if d != dp[mask][u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dp[mask][v]:
                dp[mask][v] = nd
                heapq.heappush(pq, (nd, v))

# Combine masks
for mask in range(1 << t):
    # Try splitting mask into two non-empty subsets
    sub = (mask - 1) & mask
    while sub:
        other = mask ^ sub
        if other < sub:  # avoid duplicate work
            sub = (sub - 1) & mask
            continue
        for v in range(n):
            if dp[sub][v] + dp[other][v] < dp[mask][v]:
                dp[mask][v] = dp[sub][v] + dp[other][v]
        sub = (sub - 1) & mask

# Answer is min over all nodes for full mask
full_mask = (1 << t) - 1
print(min(dp[full_mask]))