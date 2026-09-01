import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n  # -1 uncolored, 0 -> state 1, 1 -> state 2

for start in range(n):
    if color[start] != -1:
        continue
    # BFS to color component, try to assign 0 (state 1) to start
    color[start] = 0
    q = deque([start])
    ok = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                ok = False
                break
        if not ok:
            break
    if not ok:
        print("NO")
        sys.exit()

# Now we have a valid bipartite coloring, but we need lexicographically smallest.
# For each component, we can flip colors if it makes the smallest index in that component have state 1.
visited = [False] * n
for i in range(n):
    if visited[i]:
        continue
    # collect component
    comp = []
    q = deque([i])
    visited[i] = True
    while q:
        u = q.popleft()
        comp.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    # If the smallest node in comp has color 1, flip all colors in comp
    min_node = min(comp)
    if color[min_node] == 1:
        for u in comp:
            color[u] = 1 - color[u]

# Output
res = [1 if c == 0 else 2 for c in color]
print("YES")
print(" ".join(map(str, res)))