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
    if color[start] == -1:
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

# Now we have a valid 2-coloring, but we need lexicographically smallest.
# We can flip colors in each connected component if it makes earlier nodes 1.
# Since components are independent, we check each component and flip if needed.

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
        # Check if flipping makes lexicographically smaller
        # Count how many nodes would become 1 if we flip
        # We compare the first node in comp (smallest index) — if it's 1 already, keep; else flip.
        first = min(comp)
        if color[first] == 1:
            # flip all in this component
            for u in comp:
                color[u] ^= 1

print("YES")
print(" ".join(str(c + 1) for c in color))