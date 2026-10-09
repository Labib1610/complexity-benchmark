import sys
from collections import deque

input = sys.stdin.readline

q, t = map(int, input().split())
adj = [[] for _ in range(q + 1)]
for _ in range(t):
    a, b = map(int, input().split())
    adj[a].append(b)

# Hopcroft-Karp
INF = 10**9
matchU = [0] * (q + 1)
matchV = [0] * (2 * q + 1)
dist = [0] * (q + 1)

def bfs():
    dq = deque()
    for u in range(1, q + 1):
        if matchU[u] == 0:
            dist[u] = 0
            dq.append(u)
        else:
            dist[u] = INF
    found = False
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            u2 = matchV[v]
            if u2 != 0 and dist[u2] == INF:
                dist[u2] = dist[u] + 1
                dq.append(u2)
            elif u2 == 0:
                found = True
    return found

def dfs(u):
    for v in adj[u]:
        u2 = matchV[v]
        if u2 == 0 or (dist[u2] == dist[u] + 1 and dfs(u2)):
            matchU[u] = v
            matchV[v] = u
            return True
    dist[u] = INF
    return False

matching = 0
while bfs():
    for u in range(1, q + 1):
        if matchU[u] == 0 and dfs(u):
            matching += 1

if matching == q:
    print("YES")
    for u in range(1, q + 1):
        print(u, matchU[u])
else:
    print("NO")