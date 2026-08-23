import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

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
                    color[v] = color[u] ^ 1
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
    # Now we have a valid bipartition, but we want lexicographically smallest.
    # We can try to flip components if it makes earlier gears direction 1.
    # color 0 -> direction 1, color 1 -> direction 2
    # We'll do BFS again, but for each component, decide orientation based on smallest index.
    visited = [False] * n
    res = [0] * n
    for i in range(n):
        if not visited[i]:
            # BFS to collect component
            comp = []
            q = deque([i])
            visited[i] = True
            comp.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
                        comp.append(v)
            # Determine orientation: if smallest index in comp can be 1
            # We already have color from previous BFS, but we can flip if needed.
            # color[i] is 0 or 1. If color[i] == 1, flipping makes it 0.
            flip = (color[i] == 1)
            for u in comp:
                if flip:
                    res[u] = 2 if color[u] == 0 else 1
                else:
                    res[u] = 1 if color[u] == 0 else 2
    print("YES")
    print(" ".join(map(str, res)))