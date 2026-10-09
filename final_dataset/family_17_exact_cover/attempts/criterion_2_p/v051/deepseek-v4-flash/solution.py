import sys
from collections import deque

input = sys.stdin.readline

q, t = map(int, input().split())
adj = [[] for _ in range(q + 1)]
for _ in range(t):
    a, b = map(int, input().split())
    adj[a].append(b - q)  # store as 1..q for bases

match_base = [0] * (q + 1)  # base matched to which acid
match_acid = [0] * (q + 1)  # acid matched to which base
dist = [0] * (q + 1)

def bfs():
    dq = deque()
    for u in range(1, q + 1):
        if match_acid[u] == 0:
            dist[u] = 0
            dq.append(u)
        else:
            dist[u] = float('inf')
    found = False
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            nxt = match_base[v]
            if nxt != 0 and dist[nxt] == float('inf'):
                dist[nxt] = dist[u] + 1
                dq.append(nxt)
            elif nxt == 0:
                found = True
    return found

def dfs(u):
    for v in adj[u]:
        nxt = match_base[v]
        if nxt == 0 or (dist[nxt] == dist[u] + 1 and dfs(nxt)):
            match_acid[u] = v
            match_base[v] = u
            return True
    dist[u] = float('inf')
    return False

matching = 0
while bfs():
    for u in range(1, q + 1):
        if match_acid[u] == 0 and dfs(u):
            matching += 1

if matching == q:
    print("YES")
    for acid in range(1, q + 1):
        base = match_acid[acid]
        print(acid, base + q)
else:
    print("NO")