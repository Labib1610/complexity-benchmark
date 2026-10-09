import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n)]
color = [-1] * n

# Build graph and color bipartition
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

# BFS to color
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

# Hopcroft–Karp for maximum bipartite matching
matchL = [-1] * n
matchR = [-1] * n
dist = [0] * n

def bfs():
    q = deque()
    for u in left:
        if matchL[u] == -1:
            dist[u] = 0
            q.append(u)
        else:
            dist[u] = float('inf')
    found = False
    while q:
        u = q.popleft()
        for v in adj[u]:
            mu = matchR[v]
            if mu != -1 and dist[mu] == float('inf'):
                dist[mu] = dist[u] + 1
                q.append(mu)
            elif mu == -1:
                found = True
    return found

def dfs(u):
    for v in adj[u]:
        mu = matchR[v]
        if mu == -1 or (dist[mu] == dist[u] + 1 and dfs(mu)):
            matchL[u] = v
            matchR[v] = u
            return True
    dist[u] = float('inf')
    return False

matching = 0
while bfs():
    for u in left:
        if matchL[u] == -1 and dfs(u):
            matching += 1

max_independent = n - matching
if max_independent < k:
    print("NO")
    sys.exit()

# Build independent set of size k
# Take all unmatched left vertices, then unmatched right vertices, then fill from matched ones
ind_set = []
used = [False] * n

for u in left:
    if matchL[u] == -1:
        ind_set.append(u)
        used[u] = True

for v in right:
    if matchR[v] == -1:
        ind_set.append(v)
        used[v] = True

# If still not enough, add from matched vertices (one from each matched pair)
for u in left:
    if len(ind_set) == k:
        break
    if not used[u]:
        ind_set.append(u)
        used[u] = True

print("YES")
print(" ".join(str(x + 1) for x in ind_set[:k]))