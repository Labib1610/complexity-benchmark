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
    color[start] = 1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 3 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

# First check bipartiteness
for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            print("NO")
            sys.exit()

# Now we have a valid bipartition, but we need lexicographically smallest.
# We can try to flip components if it makes earlier nodes phase 1.
visited = [False] * n
for i in range(n):
    if not visited[i]:
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
        # Check if flipping this component makes lexicographically smaller
        # Count how many nodes in comp have color 2 vs 1
        # We flip if the smallest node in comp currently has color 2
        min_node = min(comp)
        if color[min_node] == 2:
            for u in comp:
                color[u] = 3 - color[u]

print("YES")
print(" ".join(str(color[i]) for i in range(n)))