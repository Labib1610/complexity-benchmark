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
    color[start] = 0
    q = deque([start])
    comp_nodes = [start]
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                comp_nodes.append(v)
                q.append(v)
            elif color[v] == color[u]:
                possible = False
                break
        if not possible:
            break
    if not possible:
        break

if not possible:
    print("NO")
else:
    # Now we have a valid 2-coloring, but we need lexicographically smallest.
    # We can flip colors in each component if it makes the smallest index in that component 0 (mode 1).
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
        # If the smallest index in this component has color 1, flip all colors in this component
        min_idx = min(comp)
        if color[min_idx] == 1:
            for u in comp:
                color[u] ^= 1

    print("YES")
    print(' '.join(str(c + 1) for c in color))