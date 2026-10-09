import sys
sys.setrecursionlimit(300000)
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
    from collections import deque
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

for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            print("NO")
            sys.exit()

# Now we have a valid bipartite coloring, but we need lexicographically smallest.
# We can try to flip components if it makes earlier workers have smaller values.
visited = [False] * n
for i in range(n):
    if not visited[i]:
        # collect component
        comp = []
        stack = [i]
        visited[i] = True
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        # Check if flipping colors in this component gives lexicographically smaller
        # We compare current color[i] vs 3 - color[i] for smallest index in comp
        min_idx = min(comp)
        if color[min_idx] == 2:
            # flip
            for u in comp:
                color[u] = 3 - color[u]

print("YES")
print(' '.join(str(color[i]) for i in range(n)))