import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
priority = set(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
weights = {}

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
    degree[u] += 1
    degree[v] += 1
    weights[(u, v)] = w
    weights[(v, u)] = w

# If only one priority language, no edges needed
if t == 1:
    print(0)
    sys.exit()

# Remove non-priority leaves
q = deque()
in_tree = [True] * (n + 1)

for i in range(1, n + 1):
    if degree[i] == 1 and i not in priority:
        q.append(i)

while q:
    u = q.popleft()
    if not in_tree[u]:
        continue
    in_tree[u] = False
    for v, w in adj[u]:
        if in_tree[v]:
            degree[v] -= 1
            if degree[v] == 1 and v not in priority:
                q.append(v)

# Sum weights of edges where both endpoints are still in the tree
total = 0
for u in range(1, n + 1):
    if in_tree[u]:
        for v, w in adj[u]:
            if u < v and in_tree[v]:
                total += w

print(total)