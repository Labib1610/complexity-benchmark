import sys
from collections import deque

input = sys.stdin.readline

nL, nR, m = map(int, input().split())
edges = []
adjL = [[] for _ in range(nL)]
adjR = [[] for _ in range(nR)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v))
    adjL[u].append((v, i))
    adjR[v].append((u, i))

# Compute max degree
degL = [len(adjL[i]) for i in range(nL)]
degR = [len(adjR[i]) for i in range(nR)]
Delta = max(max(degL) if nL > 0 else 0, max(degR) if nR > 0 else 0)

color = [0] * m

# Greedy edge coloring for bipartite graph
# We'll use a simple algorithm: for each edge, find smallest free color for both endpoints
# This works because bipartite graphs are Delta-edge-colorable.

usedL = [set() for _ in range(nL)]
usedR = [set() for _ in range(nR)]

for idx, (u, v) in enumerate(edges):
    # find smallest color not used by u or v
    c = 1
    while c in usedL[u] or c in usedR[v]:
        c += 1
    color[idx] = c
    usedL[u].add(c)
    usedR[v].add(c)

print("YES")
print(" ".join(map(str, color)))