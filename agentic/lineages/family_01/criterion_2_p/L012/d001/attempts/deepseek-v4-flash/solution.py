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
ans = [1] * n

for start in range(n):
    if color[start] != -1:
        continue
    color[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                print("NO")
                sys.exit()

# Now color is 0/1, we want lexicographically smallest
# We can flip all colors in a connected component if it makes earlier nodes 1
visited = [False] * n
for i in range(n):
    if visited[i]:
        continue
    # BFS to collect component
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
    # Check if flipping gives lexicographically smaller
    # Current assignment: color 0 -> 1, color 1 -> 2
    # If we flip: color 0 -> 2, color 1 -> 1
    # We compare at the smallest index in comp
    smallest_idx = min(comp)
    if color[smallest_idx] == 1:
        # flipping makes it 1, so flip
        for u in comp:
            color[u] ^= 1

for i in range(n):
    ans[i] = 1 if color[i] == 0 else 2

print("YES")
print(" ".join(map(str, ans)))