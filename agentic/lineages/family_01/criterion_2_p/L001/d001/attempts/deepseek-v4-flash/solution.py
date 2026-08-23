import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

color = [-1] * n  # posture: 1 or 2, colored as 0 or 1 internally?

# Use 0 and 1 for coloring, then final mapping: color0 → 1, color1 → 2.

def bfs(start):
    q = deque([start])
    color[start] = 0
    while q:
        u = q.popleft()
        for v in g[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                print("NO")
                sys.exit()

for i in range(n):
    if color[i] == -1:
        color color[i] = 0  # typically the smallest
        bfs(i) # or manage queue

# If we get here, the graph is bipartite
# convert colors: color=0 -> post=1, color=1-> post2
result = [1 if color[c] == color 0 else 1 for c in range(n)]

sys.stdout.write("YES\n")
sys.stdout.write(' ' . join(map(str, result)))