import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

# Bipartite coloring
color = [-1] * n
for i in range(n):
    if color[i] == -1:
        color[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)

left = [i for i in range(n) if color[i] == 0]
right = [i for i in range(n) if color[i] == 1]

# Build graph for Hopcroft-Karp
left_id = {v: i for i, v in enumerate(left)}
right_id = {v: i for i, v in enumerate(right)}
L = len(left)
R = len(right)

g = [[] for _ in range(L)]
for u in left:
    for v in adj[u]:
        g[left_id[u]].append(right_id[v])

INF = 10**9
pairU = [-1] * L
pairV = [-1] * R
dist = [0] * L

def bfs():
    q = deque()
    for u in range(L):
        if pairU[u] == -1:
            dist[u] = 0
            q.append(u)
        else:
            dist[u] = INF
    found = False
    while q:
        u = q.popleft()
        for v in g[u]:
            pu = pairV[v]
            if pu != -1 and dist[pu] == INF:
                dist[pu] = dist[u] + 1
                q.append(pu)
            elif pu == -1:
                found = True
    return found

def dfs(u):
    for v in g[u]:
        pu = pairV[v]
        if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
            pairU[u] = v
            pairV[v] = u
            return True
    dist[u] = INF
    return False

matching = 0
while bfs():
    for u in range(L):
        if pairU[u] == -1 and dfs(u):
            matching += 1

# Build minimum vertex cover via alternating paths
# From unmatched left vertices, traverse alternating paths
visited_left = [False] * L
visited_right = [False] * R

q = deque()
for u in range(L):
    if pairU[u] == -1:
        q.append(u)
        visited_left[u] = True

while q:
    u = q.popleft()
    for v in g[u]:
        if not visited_right[v]:
            visited_right[v] = True
            pu = pairV[v]
            if pu != -1 and not visited_left[pu]:
                visited_left[pu] = True
                q.append(pu)

# Minimum vertex cover: (left not visited) + (right visited)
cover_left = [left[i] for i in range(L) if not visited_left[i]]
cover_right = [right[i] for i in range(R) if visited_right[i]]
min_cover = set(cover_left + cover_right)

# Maximum independent set = all vertices not in min cover
ind_set = [i for i in range(n) if i not in min_cover]

if len(ind_set) < k:
    print("NO")
else:
    print("YES")
    print(" ".join(str(x + 1) for x in ind_set[:k]))