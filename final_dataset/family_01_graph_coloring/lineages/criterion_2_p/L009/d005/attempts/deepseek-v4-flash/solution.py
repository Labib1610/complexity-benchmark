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
ok = True

for start in range(n):
    if color[start] != -1:
        continue
    color[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                ok = False
                break
        if not ok:
            break
    if not ok:
        break

if not ok:
    print("NO")
else:
    # Now we have a valid 2-coloring, but we need lexicographically smallest.
    # For each component, we can flip colors if it makes the assignment smaller.
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
        # Try both colorings for this component
        # current coloring: color[comp] as is
        # flipped: 1 - color[comp]
        # choose lexicographically smaller
        # We compare the first differing index
        flip = False
        for u in sorted(comp):
            if (1 - color[u]) < color[u]:
                flip = True
                break
            elif (1 - color[u]) > color[u]:
                break
        if flip:
            for u in comp:
                color[u] = 1 - color[u]

    print("YES")
    print(' '.join(str(c + 1) for c in color))