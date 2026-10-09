import sys
from collections import deque

input = sys.stdin.readline

q, t = map(int, input().split())
adj = [[] for _ in range(q + 1)]

for _ in range(t):
    a, b = map(int, input().split())
    adj[a].append(b - q)  # store responder as 1..q

# Hopcroft-Karp
INF = 10**9
matchU = [0] * (q + 1)
matchV = [0] * (q + 1)
dist = [0] * (q + 1)

def bfs():
    dq = deque()
    for u in range(1, q + 1):
        if matchU[u] == 0:
            dist[u] = 0
            dq.append(u)
        else:
            dist[u] = INF
    dist[0] = INF
    while dq:
        u = dq.popleft()
        if dist[u] < dist[0]:
            for v in adj[u]:
                if dist[matchV[v]] == INF:
                    dist[matchV[v]] = dist[u] + 1
                    dq.append(matchV[v])
    return dist[0] != INF

def dfs(u):
    if u != 0:
        for v in adj[u]:
            if dist[matchV[v]] == dist[u] + 1 and dfs(matchV[v]):
                matchV[v] = u
                matchU[u] = v
                return True
        dist[u] = INF
        return False
    return True

matching = 0
while bfs():
    for u in range(1, q + 1):
        if matchU[u] == 0 and dfs(u):
            matching += 1

if matching == q:
    print("YES")
    for u in range(1, q + 1):
        print(u, matchU[u] + q)
else:
    print("NO")