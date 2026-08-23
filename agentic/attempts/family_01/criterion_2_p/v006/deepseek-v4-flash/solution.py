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

# Now we have a valid bipartition, but we want lexicographically smallest assignment.
# We can try to flip colors in each connected component if it makes smaller numbers assigned to 1.
# Since each component is independent, we check which coloring gives smaller lexicographic order.

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
        # count how many in each color
        count0 = sum(1 for u in comp if color[u] == 0)
        count1 = len(comp) - count0
        # If flipping reduces the number of 1's in the component, flip
        # Actually we want smallest lexicographic: we want smallest indices to be 1 if possible.
        # So we check: if the smallest index in comp is color 1, we might flip to make it 0.
        min_node = min(comp)
        if color[min_node] == 1:
            # flip
            for u in comp:
                color[u] = 1 - color[u]

print("YES")
print(' '.join(str(c + 1) for c in color))