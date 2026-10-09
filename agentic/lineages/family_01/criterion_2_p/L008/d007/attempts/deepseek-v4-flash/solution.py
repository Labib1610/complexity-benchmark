import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
has_self_loop = False

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if u == v:
        has_self_loop = True
    adj[u].append(v)
    adj[v].append(u)

if has_self_loop:
    print("NO")
    sys.exit()

color = [-1] * n  # 0 = mode 1, 1 = mode 2

for start in range(n):
    if color[start] != -1:
        continue
    # try to assign mode 1 (0) to start
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

# If we reach here, graph is bipartite.
# But we need lexicographically smallest: we may need to flip components.
# We'll try to make as many early vertices as possible mode 1.
# We can do BFS from each uncolored vertex, but we already colored.
# To get lexicographically smallest, we can re-run with a greedy BFS:
# For each vertex in order, if uncolored, set to 0 and BFS.

color = [-1] * n
for i in range(n):
    if color[i] != -1:
        continue
    color[i] = 0
    q = deque([i])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)

# Output
print("YES")
print(' '.join(str(c + 1) for c in color))