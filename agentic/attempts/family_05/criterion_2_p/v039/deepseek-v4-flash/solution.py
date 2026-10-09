import sys
from collections import deque

input = sys.stdin.readline

k, t = map(int, input().split())

# adj[x] = list of flight paths for pilot x
adj = [[] for _ in range(k + 1)]

for _ in range(t):
    x, y, z = map(int, input().split())
    adj[x].append(z)

# Hopcroft-Karp
pair_u = [0] * (k + 1)  # pair_u[x] = path assigned to pilot x
pair_v = [0] * (k + 1)  # pair_v[z] = pilot assigned to path z
dist = [0] * (k + 1)

INF = 10**9

def bfs():
    q = deque()
    for u in range(1, k + 1):
        if pair_u[u] == 0:
            dist[u] = 0
            q.append(u)
        else:
            dist[u] = INF
    dist[0] = INF
    while q:
        u = q.popleft()
        if dist[u] < dist[0]:
            for v in adj[u]:
                if dist[pair_v[v]] == INF:
                    dist[pair_v[v]] = dist[u] + 1
                    q.append(pair_v[v])
    return dist[0] != INF

def dfs(u):
    if u != 0:
        for v in adj[u]:
            if dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v]):
                pair_v[v] = u
                pair_u[u] = v
                return True
        dist[u] = INF
        return False
    return True

matching = 0
while bfs():
    for u in range(1, k + 1):
        if pair_u[u] == 0 and dfs(u):
            matching += 1

if matching == k:
    print("YES")
    # Reconstruct aircraft from pilot: pilot i -> aircraft i (since fixed)
    for pilot in range(1, k + 1):
        path = pair_u[pilot]
        print(pilot, pilot, path)
else:
    print("NO")