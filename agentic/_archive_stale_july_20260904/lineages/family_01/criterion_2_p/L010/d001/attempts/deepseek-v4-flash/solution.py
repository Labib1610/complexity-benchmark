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

color = [-1] * n  # -1 unassigned, 0 -> tier 1, 1 -> tier 2

for start in range(n):
    if color[start] == -1:
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

# Now we have a valid bipartite coloring, but we need lexicographically smallest.
# We can try to flip components if it makes earlier nodes smaller.
# Since color 0 -> tier 1, color 1 -> tier 2, we want as many 0s early as possible.

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
        # Check if flipping this component makes it lexicographically smaller
        # We compare current vs flipped for the smallest index in comp
        flip = False
        for u in sorted(comp):
            if color[u] == 1:
                flip = True
                break
            elif color[u] == 0:
                break
        if flip:
            for u in comp:
                color[u] = 1 - color[u]

print("YES")
print(' '.join(str(c + 1) for c in color))