import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

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

possible = True
for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            possible = False
            break

if not possible:
    print("NO")
else:
    print("YES")
    # color 0 -> channel 1, color 1 -> channel 2
    print(' '.join(str(color[i] + 1) for i in range(n)))