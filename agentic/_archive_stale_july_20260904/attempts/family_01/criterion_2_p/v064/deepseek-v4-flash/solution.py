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
    # BFS for bipartite check, assign start to color 0
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
                sys.exit(0)

# Now we have a valid coloring (colors 0 and 1)
# To get lexicographically smallest sequence:
# For each connected component, if its smallest index is colored 1, flip entire component
visited = [False] * n
for i in range(n):
    if not visited[i]:
        # find component
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
        min_node = min(comp)
        if color[min_node] == 1:
            # flip this component
            for u in comp:
                color[u] = 1 - color[u]

# Output
print("YES")
print(' '.join(str(c + 1) for c in color))