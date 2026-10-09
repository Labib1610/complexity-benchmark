import sys
from collections import deque

input = sys.stdin.readline

q, t = map(int, input().split())
adj = [[] for _ in range(q)]
for _ in range(t):
    a, b = map(int, input().split())
    adj[a - 1].append(b - q - 1)  # platform index 0..q-1

# Hopcroft-Karp
INF = 10**9
pair_u = [-1] * q
pair_v = [-1] * q
dist = [0] * q

def bfs():
    dq = deque()
    for u in range(q):
        if pair_u[u] == -1:
            dist[u] = 0
            dq.append(u)
        else:
            dist[u] = INF
    found = False
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            pu = pair_v[v]
            if pu != -1 and dist[pu] == INF:
                dist[pu] = dist[u] + 1
                dq.append(pu)
            elif pu == -1:
                found = True
    return found

def dfs(u):
    for v in adj[u]:
        pu = pair_v[v]
        if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
            pair_u[u] = v
            pair_v[v] = u
            return True
    dist[u] = INF
    return False

matching = 0
while bfs():
    for u in range(q):
        if pair_u[u] == -1 and dfs(u):
            matching += 1

if matching == q:
    print("YES")
    for u in range(q):
        print(u + 1, pair_u[u] + q + 1)
else:
    print("NO")