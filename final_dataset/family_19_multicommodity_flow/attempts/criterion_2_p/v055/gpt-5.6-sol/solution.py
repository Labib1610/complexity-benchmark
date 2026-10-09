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
capacities = []

for _ in range(m):
    u = next(it) - 1
    v = next(it) - 1
    cap = next(it)
    capacities.append(cap)

    if u == v:
        edge_refs.append(None)
        continue

    forward_index = len(graph[u])
    reverse_index = len(graph[v])
    graph[u].append([v, reverse_index, cap])
    graph[v].append([u, forward_index, 0])
    edge_refs.append((u, forward_index))

if s == t:
    if demand == 0:
        print("YES")
        print(" ".join(["0"] * m))
    else:
        print("NO")
    sys.exit()

level = [-1] * n
ptr = [0] * n

def bfs():
    for i in range(n):
        level[i] = -1
    level[s] = 0
    q = deque([s])

    while q:
        u = q.popleft()
        for v, rev, cap in graph[u]:
            if cap > 0 and level[v] == -1:
                level[v] = level[u] + 1
                if v == t:
                    return True
                q.append(v)
    return level[t] != -1

def dfs(u, pushed):
    if u == t:
        return pushed

    while ptr[u] < len(graph[u]):
        idx = ptr[u]
        edge = graph[u][idx]
        v, rev, cap = edge

        if cap > 0 and level[v] == level[u] + 1:
            sent = dfs(v, min(pushed, cap))
            if sent:
                edge[2] -= sent
                graph[v][rev][2] += sent
                return sent

        ptr[u] += 1

    return 0

flow = 0
while flow < demand and bfs():
    ptr[:] = [0] * n
    while flow < demand:
        pushed = dfs(s, demand - flow)
        if pushed == 0:
            break
        flow += pushed

if flow < demand:
    print("NO")
else:
    result = []
    for cap, ref in zip(capacities, edge_refs):
        if ref is None:
            result.append(0)
        else:
            u, idx = ref
            result.append(cap - graph[u][idx][2])

    print("YES")
    print(" ".join(map(str, result)))