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

color = [-1] * n  # -1 unassigned, 0 -> 1, 1 -> 2

def bfs(start):
    # try assigning 1 first
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
            # try assigning 2 first
            color = [-1] * n
            color[i] = 1
            q = deque([i])
            ok = True
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                print("NO")
                sys.exit()
            # continue with remaining unvisited nodes
            for j in range(n):
                if color[j] == -1:
                    if not bfs(j):
                        print("NO")
                        sys.exit()
            break

print("YES")
print(' '.join(str(c + 1) for c in color))