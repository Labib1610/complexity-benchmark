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

def try_color(start_color):
    color = [-1] * n
    color[0] = start_color
    q = deque([0])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                return None
    # If some nodes are disconnected, color them with 1 if possible
    for i in range(n):
        if color[i] == -1:
            color[i] = 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return None
    return color

# Try starting with 1
res = try_color(1)
if res is None:
    res = try_color(0)
if res is None:
    print("NO")
else:
    print("YES")
    print(" ".join(str(c + 1) for c in res))