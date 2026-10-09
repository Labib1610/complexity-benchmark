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

color = [-1] * n  # -1 uncolored, 0 = shift 1, 1 = shift 2

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

# Now we have a valid bipartite coloring, but we need lexicographically smallest.
# We can try to flip components if it makes earlier nodes 0.
# Since BFS starts with 0, we may need to re-check components where first node is 1.
# We'll do a second pass: for each unvisited component, try starting with 0, if possible.

visited = [False] * n
result = [0] * n

for i in range(n):
    if not visited[i]:
        # Try coloring this component with i=0
        comp = []
        q = deque([i])
        visited[i] = True
        temp_color = [-1] * n
        temp_color[i] = 0
        ok = True
        while q:
            u = q.popleft()
            comp.append(u)
            for v in adj[u]:
                if temp_color[v] == -1:
                    temp_color[v] = temp_color[u] ^ 1
                    visited[v] = True
                    q.append(v)
                elif temp_color[v] == temp_color[u]:
                    ok = False
        if not ok:
            # Should not happen because graph is bipartite, but just in case
            print("NO")
            sys.exit()
        # Assign to result
        for u in comp:
            result[u] = temp_color[u] + 1  # 1 or 2

print("YES")
print(" ".join(map(str, result)))