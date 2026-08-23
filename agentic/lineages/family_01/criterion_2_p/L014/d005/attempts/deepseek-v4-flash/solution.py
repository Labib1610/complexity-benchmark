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

color = [-1] * n
possible = True

for start in range(n):
    if color[start] != -1:
        continue
    # BFS to color component
    q = deque([start])
    color[start] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                possible = False
                q.clear()
                break
    if not possible:
        break

if not possible:
    print("NO")
else:
    # Apply tie-breaking: for each component, smallest index gets 1 if possible
    assigned = [-1] * n
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        # find component nodes
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
        # smallest index in component
        min_node = min(comp)
        # assign based on color from BFS
        base = color[min_node]
        # We want min_node to be 1 if possible
        # If base == 0, min_node already 1; if base == 1, flip all
        flip = (base == 1)
        for u in comp:
            assigned[u] = 1 if (color[u] ^ flip) == 0 else 2

    print("YES")
    print(" ".join(map(str, assigned)))