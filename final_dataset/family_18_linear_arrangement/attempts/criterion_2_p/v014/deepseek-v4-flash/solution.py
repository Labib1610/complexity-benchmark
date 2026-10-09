import sys
from collections import deque

input = sys.stdin.readline

n, m, B = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

# Find tree center(s)
parent = [-1] * n
order = []
q = deque([0])
parent[0] = 0
while q:
    u = q.popleft()
    order.append(u)
    for v in adj[u]:
        if parent[v] == -1:
            parent[v] = u
            q.append(v)

# Compute degrees and prune leaves iteratively to find center
deg = [len(adj[i]) for i in range(n)]
leaves = [i for i in range(n) if deg[i] == 1]
remaining = n
while remaining > 2:
    new_leaves = []
    for leaf in leaves:
        p = parent[leaf]
        deg[p] -= 1
        if deg[p] == 1:
            new_leaves.append(p)
        remaining -= 1
    leaves = new_leaves

# choose center as one or two centers
if len(leaves) == 1:
    center = leaves[0]
else:
    center = leaves[0]  # pick any of the two centers

# BFS from center to get order by distance
pos = [-1] * n
pos[center] = 0
order_bfs = [center]
start = 0
while start < len(order_bfs):
    u = order_bfs[start]
    start += 1
    for v in adj[u]:
        if pos[v] == -1:
            pos[v] = pos[u] + 1
            order_bfs.append(v)

# Build layout: assign 1..n according to BFS order
placement = [0] * n
slot = 1
for u in order_bfs:
    placement[u] = slot
    slot += 1

# Check total length
total_len = 0
for u in range(n):
    for v in adj[u]:
        if u < v:
            total_len += abs(placement[u] - placement[v])

if total_len <= B:
    print("YES")
    print(" ".join(map(str, placement)))
else:
    print("NO")