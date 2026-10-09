import sys
from collections import deque

input = sys.stdin.readline

q, t = map(int, input().split())
adj = [[] for _ in range(q)]
for _ in range(t):
    a, b = map(int, input().split())
    adj[a - 1].append(b - q - 1)

INF = 10**9
pairU = [-1] * q
pairV = [-1] * q
dist = [0] * q

def bfs():
    dq = deque()
    for u in range(q):
        if pairU[u] == -1:
            dist[u] = 0
            dq.append(u)
        else:
            dist[u] = INF
    found = False
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            pu = pairV[v]
            if pu == -1:
                found = True
            elif dist[pu] == INF:
                dist[pu] = dist[u] + 1
                dq.append(pu)
    return found

def dfs(u):
    for v in adj[u]:
        pu = pairV[v]
        if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
            pairU[u] = v
            pairV[v] = u
            return True
    dist[u] = INF
    return False

matching = 0
while bfs():
    for u in range(q):
        if pairU[u] == -1 and dfs(u):
            matching += 1

if matching == q:
    print("YES")
    for u in range(q):
        print(u + 1, pairU[u] + q + 1)
else:
    print("NO")