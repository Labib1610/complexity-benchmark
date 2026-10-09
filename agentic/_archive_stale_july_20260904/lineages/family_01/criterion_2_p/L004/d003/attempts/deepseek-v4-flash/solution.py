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

for start in range(n):
    if color[start] != -1:
        continue
    color[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                print("NO")
                sys.exit()

# Now we have a valid bipartition.
# To get lexicographically smallest, we can flip colors in each component if needed.
# We want smallest possible z_i, so we try to set 1 for smallest index in each component.

visited = [False] * n
for i in range(n):
    if visited[i]:
        continue
    # BFS to collect component
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
    # Check if flipping colors makes lexicographically smaller
    # Current color: 0 -> band 1, 1 -> band 2
    # If we flip, 0 -> 2, 1 -> 1
    # We compare the two options for this component
    # Option A: keep as is
    # Option B: flip
    # We choose the one that gives smaller sequence for the component indices sorted
    comp_sorted = sorted(comp)
    # Build both options
    optA = [color[x] for x in comp_sorted]
    optB = [1 - color[x] for x in comp_sorted]
    # Choose lexicographically smaller (0 means band 1, 1 means band 2)
    if optB < optA:
        for x in comp:
            color[x] = 1 - color[x]

# Output
print("YES")
print(' '.join(str(c + 1) for c in color))