import sys
import heapq

input = sys.stdin.readline

n, m, t = map(int, input().split())
priority = list(map(int, input().split()))
priority_set = set(priority)

# Build graph
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# If t == 1, no pairs to connect
if t == 1:
    print(0)
    sys.exit()

# Compute shortest path distances between all priority nodes
# Since n <= 100, we can run Dijkstra from each priority node
INF = 10**18
dist_matrix = {}
for p in priority:
    dist = [INF] * (n + 1)
    dist[p] = 0
    pq = [(0, p)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    dist_matrix[p] = dist

# Build complete graph among priority nodes with shortest path costs
edges = []
for i in range(t):
    for j in range(i + 1, t):
        u = priority[i]
        v = priority[j]
        cost = dist_matrix[u][v]
        edges.append((cost, u, v))

# Minimum spanning tree (Kruskal)
parent = {p: p for p in priority}
rank = {p: 0 for p in priority}

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return False
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] += 1
    return True

edges.sort()
total_cost = 0
for cost, u, v in edges:
    if union(u, v):
        total_cost += cost

print(total_cost)