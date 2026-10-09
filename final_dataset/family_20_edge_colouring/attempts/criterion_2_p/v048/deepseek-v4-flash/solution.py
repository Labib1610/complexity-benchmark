import sys
from collections import deque

input = sys.stdin.readline

nL, nR, m = map(int, input().split())
edges = []
degL = [0] * (nL + 1)
degR = [0] * (nR + 1)

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    degL[u] += 1
    degR[v] += 1

peak = max(max(degL), max(degR), 1)

# adjacency lists for locks and keys
adjL = [[] for _ in range(nL + 1)]
adjR = [[] for _ in range(nR + 1)]

for idx, (u, v) in enumerate(edges):
    adjL[u].append((v, idx))
    adjR[v].append((u, idx))

color = [0] * m

# For each vertex, keep track of used colors
usedL = [set() for _ in range(nL + 1)]
usedR = [set() for _ in range(nR + 1)]

# Simple greedy: for each edge, pick smallest color not used by both endpoints
for idx, (u, v) in enumerate(edges):
    c = 1
    while c in usedL[u] or c in usedR[v]:
        c += 1
    color[idx] = c
    usedL[u].add(c)
    usedR[v].add(c)

print("YES")
print(" ".join(map(str, color)))