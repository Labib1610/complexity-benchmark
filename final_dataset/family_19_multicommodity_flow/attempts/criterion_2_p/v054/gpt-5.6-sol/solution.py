import sys
from collections import deque

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

n = next(it)
m = next(it)
_ = next(it)

s = next(it) - 1
t = next(it) - 1
required = next(it)

graph = [[] for _ in range(n)]
to = []
capacity = []
original_capacity = []
route_edges = []

def add_edge(u, v, cap):
    edge_id = len(to)
    to.extend((v, u))
    capacity.extend((cap, 0))
    original_capacity.extend((cap, 0))
    graph[u].append(edge_id)
    graph[v].append(edge_id ^ 1)
    return edge_id

for _ in range(m):
    u = next(it) - 1
    v = next(it) - 1
    cap = next(it)
    route_edges.append(add_edge(u, v, cap))

if required == 0:
    print("YES")
    print(" ".join("0" for _ in range(m)))
    sys.exit()

if s == t:
    print("NO")
    sys.exit()

level = [-1] * n
ptr = [0] * n

def bfs():
    level[:] = [-1] * n
    level[s] = 0
    queue = deque([s])

    while queue:
        v = queue.popleft()
        next_level = level[v] + 1
        for edge_id in graph[v]:
            u = to[edge_id]
            if capacity[edge_id] > 0 and level[u] == -1:
                level[u] = next_level
                queue.append(u)

    return level[t] != -1

def dfs(v, pushed):
    if v == t:
        return pushed

    while ptr[v] < len(graph[v]):
        edge_id = graph[v][ptr[v]]
        u = to[edge_id]

        if capacity[edge_id] > 0 and level[u] == level[v] + 1:
            sent = dfs(u, min(pushed, capacity[edge_id]))
            if sent:
                capacity[edge_id] -= sent
                capacity[edge_id ^ 1] += sent
                return sent

        ptr[v] += 1

    return 0

flow = 0
while flow < required and bfs():
    ptr[:] = [0] * n
    while flow < required:
        sent = dfs(s, required - flow)
        if sent == 0:
            break
        flow += sent

if flow < required:
    print("NO")
else:
    answer = [
        original_capacity[edge_id] - capacity[edge_id]
        for edge_id in route_edges
    ]
    print("YES")
    print(*answer)