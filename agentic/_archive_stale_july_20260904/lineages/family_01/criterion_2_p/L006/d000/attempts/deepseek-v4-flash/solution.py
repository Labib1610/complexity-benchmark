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

def bfs(start):
    q = deque([start])
    color[start] = 0  # shift 1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            print("NO")
            sys.exit()

# Now we have a valid bipartite coloring, but we need lexicographically smallest.
# We can try to flip colors in each connected component if it makes earlier indices smaller.
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
        # Try both colorings for this component
        # current coloring from BFS is color[]
        # Option 1: keep as is
        # Option 2: flip all colors in comp
        # Choose the one that gives smaller assignment for smallest index in comp
        comp.sort()
        first = comp[0]
        # If first is already 0, keep; else flip
        if color[first] == 1:
            for u in comp:
                color[u] ^= 1

print("YES")
print(' '.join(str(c + 1) for c in color))