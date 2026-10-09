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
        # try starting with 0
        color[i] = 0
        if not bfs(i):
            # try starting with 1
            color[i] = 1
            # reset component colors
            # We need to redo BFS for this component
            # So we reset all nodes in this component
            stack = [i]
            comp = []
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if color[v] != -1 and v not in comp:
                        stack.append(v)
            # Actually simpler: just reset all visited in this component
            # We'll do a fresh BFS with color 1
            # But we must reset colors of this component
            # Let's do a DFS to find component
            comp_nodes = []
            stack = [i]
            visited = set()
            while stack:
                u = stack.pop()
                if u in visited:
                    continue
                visited.add(u)
                comp_nodes.append(u)
                for v in adj[u]:
                    if v not in visited:
                        stack.append(v)
            for u in comp_nodes:
                color[u] = -1
            color[i] = 1
            if not bfs(i):
                print("NO")
                return

print("YES")
print(' '.join(str(c + 1) for c in color))