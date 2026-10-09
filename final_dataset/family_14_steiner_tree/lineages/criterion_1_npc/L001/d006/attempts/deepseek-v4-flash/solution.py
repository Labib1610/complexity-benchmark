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

if t == 1:
    print(0)
    sys.exit()

# Map target variables to bit positions
target_index = {var: i for i, var in enumerate(targets)}

# dist[i][mask] = min cost to connect target i to the set of targets in mask
INF = 10**18
dist = [[INF] * (1 << t) for _ in range(n + 1)]

# Initialize: each target alone has cost 0 for its own bit
for i, var in enumerate(targets):
    dist[var][1 << i] = 0

# Dijkstra-like DP over (node, mask)
pq = []
for i, var in enumerate(targets):
    heapq.heappush(pq, (0, var, 1 << i))

while pq:
    d, u, mask = heapq.heappop(pq)
    if d > dist[u][mask]:
        continue
    # Try to merge with another mask at the same node
    # (standard Steiner DP: combine two masks)
    # We'll do this by iterating over submasks
    sub = (mask - 1) & mask
    while sub:
        other = mask ^ sub
        if dist[u][sub] + dist[u][other] < dist[u][mask]:
            dist[u][mask] = dist[u][sub] + dist[u][other]
            heapq.heappush(pq, (dist[u][mask], u, mask))
        sub = (sub - 1) & mask

    # Relax edges
    for v, w in graph[u]:
        nd = d + w
        if nd < dist[v][mask]:
            dist[v][mask] = nd
            heapq.heappush(pq, (nd, v, mask))

# Answer is min over all nodes of dist[node][full_mask]
full_mask = (1 << t) - 1
ans = min(dist[node][full_mask] for node in range(1, n + 1))
print(ans)