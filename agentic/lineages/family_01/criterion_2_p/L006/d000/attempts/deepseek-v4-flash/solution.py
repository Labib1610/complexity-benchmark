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
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                print("NO")
                sys.exit()

# Now we have a valid 2-coloring, but we want lexicographically smallest.
# We'll try to flip components if it makes lower indices shift 1.
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
    # Count how many in this component have color 0 vs 1
    # We can flip the whole component if it reduces lexicographic order
    # For lexicographic smallest, we want smallest index in component to be 0
    # If the smallest index currently has color 1, flip the component.
    smallest = min(comp)
    if color[smallest] == 1:
        for u in comp:
            color[u] ^= 1

print("YES")
print(' '.join(str(c + 1) for c in color))