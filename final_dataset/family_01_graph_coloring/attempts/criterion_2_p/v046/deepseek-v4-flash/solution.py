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

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
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
    # Now we have a valid bipartite coloring, but we need lexicographically smallest.
    # We can flip colors in each connected component if it makes the smallest node in that component shift 1.
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
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
            # smallest node in component
            min_node = min(comp)
            if color[min_node] != 0:
                # flip all colors in this component
                for u in comp:
                    color[u] = 1 - color[u]

    print("YES")
    print(' '.join(str(c + 1) for c in color))