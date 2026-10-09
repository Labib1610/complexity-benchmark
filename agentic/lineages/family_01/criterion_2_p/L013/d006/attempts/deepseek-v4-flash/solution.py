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
    color[start] = 0  # 0 means tier 1
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
        # To make lexicographically smallest, try assigning 0 (tier 1) first
        # But we must ensure we don't conflict; do BFS from i with 0.
        color[i] = 0
        if not bfs(i):
            print("NO")
            sys.exit()

# Convert 0 -> 1, 1 -> 2
print("YES")
print(' '.join(str(c + 1) for c in color))