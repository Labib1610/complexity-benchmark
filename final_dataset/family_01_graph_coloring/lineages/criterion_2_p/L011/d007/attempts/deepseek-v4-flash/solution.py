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

def bfs(start, first_color):
    q = deque([start])
    color[start] = first_color
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
        # try starting with 0 (meaning p=1)
        temp_color = color[:]
        if bfs(i, 0):
            continue
        # if failed, reset and try starting with 1 (meaning p=2)
        color = temp_color
        if not bfs(i, 1):
            print("NO")
            sys.exit()

print("YES")
print(' '.join(str(c + 1) for c in color))