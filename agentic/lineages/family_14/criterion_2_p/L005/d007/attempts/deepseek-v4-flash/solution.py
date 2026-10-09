import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())
focus = set(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
deg = [0] * (n + 1)
edge_weight = {}

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
    deg[u] += 1
    deg[v] += 1
    edge_weight[(u, v)] = w
    edge_weight[(v, u)] = w

# If only one focus node, cost is 0
if t == 1:
    print(0)
    sys.exit()

# Remove non-focus leaves
q = deque()
in_tree = [True] * (n + 1)
for i in range(1, n + 1):
    if deg[i] == 1 and i not in focus:
        q.append(i)

while q:
    u = q.popleft()
    in_tree[u] = False
    for v, w in adj[u]:
        if in_tree[v]:
            deg[v] -= 1
            if deg[v] == 1 and v not in focus:
                q.append(v)

# Sum weights of edges where both endpoints are in_tree
total = 0
for (u, v), w in edge_weight.items():
    if u < v and in_tree[u] and in_tree[v]:
        total += w

print(total)