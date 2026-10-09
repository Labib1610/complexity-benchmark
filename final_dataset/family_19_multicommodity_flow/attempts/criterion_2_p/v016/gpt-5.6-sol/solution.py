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
demand = next(it)

graph = [[] for _ in range(n)]
edge_refs = []


def add_edge(u, v, capacity):
    forward = [v, len(graph[v]), capacity]
    backward = [u, len(graph[u]), 0]
    graph[u].append(forward)
    graph[v].append(backward)
    return forward


for _ in range(m):
    u = next(it) - 1
    v = next(it) - 1
    capacity = next(it)

    if u == v:
        edge_refs.append((None, capacity))
    else:
        edge_refs.append((add_edge(u, v, capacity), capacity))

if s == t:
    if demand == 0:
        print("YES")
        print(*([0] * m))
    else:
        print("NO")
    sys.exit()

level = [-1] * n
ptr = [0] * n


def bfs():
    level[:] = [-1] * n
    level[s] = 0
    queue = deque([s])

    while queue:
        u = queue.popleft()
        for edge in graph[u]:
            if edge[2] > 0 and level[edge[0]] == -1:
                level[edge[0]] = level[u] + 1
                queue.append(edge[0])

    return level[t] != -1


def dfs(u, pushed):
    if pushed == 0:
        return 0
    if u == t:
        return pushed

    while ptr[u] < len(graph[u]):
        edge = graph[u][ptr[u]]
        v, rev, capacity = edge

        if capacity > 0 and level[v] == level[u] + 1:
            sent = dfs(v, min(pushed, capacity))
            if sent:
                edge[2] -= sent
                graph[v][rev][2] += sent
                return sent

        ptr[u] += 1

    return 0


total_flow = 0

while total_flow < demand and bfs():
    ptr[:] = [0] * n
    while total_flow < demand:
        sent = dfs(s, demand - total_flow)
        if sent == 0:
            break
        total_flow += sent

if total_flow < demand:
    print("NO")
else:
    flows = []
    for edge, original_capacity in edge_refs:
        if edge is None:
            flows.append(0)
        else:
            flows.append(original_capacity - edge[2])

    print("YES")
    print(*flows)