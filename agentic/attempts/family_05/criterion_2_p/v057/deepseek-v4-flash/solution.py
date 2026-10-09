import sys
from collections import deque

input = sys.stdin.readline

k, t = map(int, input().split())

# Map from (c,g) pair to index
pair_to_idx = {}
idx_to_pair = []
edges = [[] for _ in range(k)]  # edges from pair index to spectrometer bank

for _ in range(t):
    c, g, s = map(int, input().split())
    if (c, g) not in pair_to_idx:
        pair_to_idx[(c, g)] = len(idx_to_pair)
        idx_to_pair.append((c, g))
    u = pair_to_idx[(c, g)]
    edges[u].append(s - 1)  # 0-based bank index

n_left = len(idx_to_pair)
n_right = k

# Hopcroft-Karp
pairU = [-1] * n_left
pairV = [-1] * n_right
dist = [0] * n_left

INF = 10**9

def bfs():
    q = deque()
    for u in range(n_left):
        if pairU[u] == -1:
            dist[u] = 0
            q.append(u)
        else:
            dist[u] = INF
    found = False
    while q:
        u = q.popleft()
        for v in edges[u]:
            pu = pairV[v]
            if pu != -1 and dist[pu] == INF:
                dist[pu] = dist[u] + 1
                q.append(pu)
            elif pu == -1:
                found = True
    return found

def dfs(u):
    for v in edges[u]:
        pu = pairV[v]
        if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
            pairU[u] = v
            pairV[v] = u
            return True
    dist[u] = INF
    return False

matching = 0
while bfs():
    for u in range(n_left):
        if pairU[u] == -1 and dfs(u):
            matching += 1

if matching != k:
    print("NO")
else:
    print("YES")
    for u in range(n_left):
        if pairU[u] != -1:
            c, g = idx_to_pair[u]
            s = pairU[u] + 1
            print(c, g, s)