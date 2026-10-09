import sys
from collections import deque

input = sys.stdin.readline

k, t = map(int, input().split())

# Map specialist -> machine (given fixed)
spec_machine = {}
# For each specialist, list of allowed time slots
allowed = [[] for _ in range(k + 1)]

for _ in range(t):
    x, y, z = map(int, input().split())
    spec_machine[x] = y
    allowed[x].append(z)

# Build bipartite graph: left = specialists (1..k), right = time slots (1..k)
# Hopcroft-Karp
INF = 10**9
pairU = [0] * (k + 1)
pairV = [0] * (k + 1)
dist = [0] * (k + 1)

def bfs():
    q = deque()
    for u in range(1, k + 1):
        if pairU[u] == 0:
            dist[u] = 0
            q.append(u)
        else:
            dist[u] = INF
    dist[0] = INF
    while q:
        u = q.popleft()
        if dist[u] < dist[0]:
            for v in allowed[u]:
                if dist[pairV[v]] == INF:
                    dist[pairV[v]] = dist[u] + 1
                    q.append(pairV[v])
    return dist[0] != INF

def dfs(u):
    if u != 0:
        for v in allowed[u]:
            if dist[pairV[v]] == dist[u] + 1:
                if dfs(pairV[v]):
                    pairV[v] = u
                    pairU[u] = v
                    return True
        dist[u] = INF
        return False
    return True

matching = 0
while bfs():
    for u in range(1, k + 1):
        if pairU[u] == 0 and dfs(u):
            matching += 1

if matching != k:
    print("NO")
else:
    print("YES")
    for u in range(1, k + 1):
        v = pairU[u]
        print(u, spec_machine[u], v)