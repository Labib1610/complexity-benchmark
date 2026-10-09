import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
critical = set(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
edge_weight = {}

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
    degree[u] += 1
    degree[v] += 1
    edge_weight[(u, v)] = w
    edge_weight[(v, u)] = w

# If only one critical node, no corridors needed
if t == 1:
    print(0)
    sys.exit()

# Remove non-critical leaves iteratively
is_critical = [False] * (n + 1)
for c in critical:
    is_critical[c] = True

in_tree = [True] * (n + 1)
q = deque()

for i in range(1, n + 1):
    if degree[i] == 1 and not is_critical[i]:
        q.append(i)

while q:
    u = q.popleft()
    if not in_tree[u]:
        continue
    in_tree[u] = False
    for v, w in adj[u]:
        if in_tree[v]:
            degree[v] -= 1
            if degree[v] == 1 and not is_critical[v]:
                q.append(v)

# Sum weights of edges where both endpoints are in the tree
total = 0
for (u, v), w in edge_weight.items():
    if u < v and in_tree[u] and in_tree[v]:
        total += w

print(total)