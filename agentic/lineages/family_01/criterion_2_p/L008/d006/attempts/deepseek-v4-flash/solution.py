from collections import deque
import sys

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

# First check bipartiteness
for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            print("NO")
            sys.exit()

# Now we have a valid bipartition, but we want lexicographically smallest.
# We can try to flip colors in each component to make early nodes 1.
# We'll do BFS again, but with priority to assign 1 if possible.

color = [-1] * n
for i in range(n):
    if color[i] == -1:
        # Try assigning 0 (meaning opacity 1) to start node
        color[i] = 0
        q = deque([i])
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    ok = False
        if not ok:
            # If conflict, flip this component
            color[i] = 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        pass  # shouldn't happen if bipartite

# Convert to 1/2
res = [1 if c == 0 else 2 for c in color]
print("YES")
print(" ".join(map(str, res)))