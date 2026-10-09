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
    color[start] = 0
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

# Convert colors to shifts: color 0 -> shift 1, color 1 -> shift 2
# But to get lexicographically smallest, we may need to swap colors in each component
# We'll do BFS again but assign 1 to the first node in each component if possible
color = [-1] * n
for i in range(n):
    if color[i] == -1:
        color[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)

# Now check if swapping colors in some components gives smaller lexicographic order
# We can try to assign 1 to the smallest index in each component
visited = [False] * n
for i in range(n):
    if not visited[i]:
        # BFS to collect component
        comp = []
        q = deque([i])
        visited[i] = True
        comp.append(i)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
                    comp.append(v)
        # Try both colorings for this component
        # coloring1: keep as is, coloring2: flip
        # We choose the one that gives smaller lexicographic order for the whole array
        # Since components are independent, we can decide per component
        # We'll compare the two options for this component
        min_idx = min(comp)
        # If min_idx currently has color 1, flipping might make it 0 (shift 1)
        # We want shift 1 for smallest index if possible
        if color[min_idx] == 1:
            # flip this component
            for node in comp:
                color[node] ^= 1

# Now output
print("YES")
print(" ".join(str(c + 1) for c in color))