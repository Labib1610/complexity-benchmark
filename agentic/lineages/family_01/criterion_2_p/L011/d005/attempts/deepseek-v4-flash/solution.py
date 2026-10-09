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
possible = True

for start in range(n):
    if color[start] != -1:
        continue
    color[start] = 0  # try 0 first (meaning cycle 1)
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                possible = False
                q.clear()
                break
    if not possible:
        break

if not possible:
    print("NO")
else:
    # color 0 -> cycle 1, color 1 -> cycle 2
    # But we need lexicographically smallest: try flipping components if it gives smaller sequence
    # We already started with 0 at first uncolored node, which is optimal for lexicographic order
    print("YES")
    print(' '.join(str(1 if c == 0 else 2) for c in color))