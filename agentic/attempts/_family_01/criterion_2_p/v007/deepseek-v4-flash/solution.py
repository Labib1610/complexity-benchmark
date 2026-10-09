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

def bfs(start):
    q = deque([start])
    color[start] = 0  # 0 means shift 1, 1 means shift 2
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            print("NO")
            sys.exit()

# Now we have a valid bipartite coloring, but we want lexicographically smallest.
# Our BFS already tried color 0 first, but we must ensure that for each component,
# starting with 0 gives the smallest. This is already the case since we start each
# component with 0.
print("YES")
print(' '.join(str(c + 1) for c in color))