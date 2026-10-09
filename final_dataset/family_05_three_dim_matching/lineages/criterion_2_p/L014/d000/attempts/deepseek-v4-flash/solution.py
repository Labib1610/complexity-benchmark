import sys
from collections import deque

input = sys.stdin.readline

k, t = map(int, input().split())

# For each route, store the vehicle and possible drivers
route_vehicle = [0] * (k + 1)
adj = [[] for _ in range(k + 1)]

for _ in range(t):
    x, y, z = map(int, input().split())
    route_vehicle[x] = y
    adj[x].append(z)

# Hopcroft-Karp
pair_u = [0] * (k + 1)
pair_v = [0] * (k + 1)
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
    for route in range(1, k + 1):
        driver = pair_u[route]
        vehicle = route_vehicle[route]
        print(route, vehicle, driver)
else:
    print("NO")