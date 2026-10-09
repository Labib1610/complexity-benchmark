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

Delta = max(max(degL), max(degR), 1)

# adjacency lists for L and R
adjL = [[] for _ in range(nL + 1)]
adjR = [[] for _ in range(nR + 1)]

# We'll store color of each edge
color = [0] * m

# For each L node, store (neighbor, edge_index)
for idx, (u, v) in enumerate(edges):
    adjL[u].append((v, idx))
    adjR[v].append((u, idx))

# colorL[u][c] = neighbor v if edge from u to v has color c, else 0
colorL = [[0] * (Delta + 1) for _ in range(nL + 1)]
colorR = [[0] * (Delta + 1) for _ in range(nR + 1)]

for u in range(1, nL + 1):
    for v, idx in adjL[u]:
        # find smallest free color for u
        c = 1
        while colorL[u][c] != 0:
            c += 1
        # assign
        color[idx] = c
        colorL[u][c] = v
        colorR[v][c] = u

        # resolve conflicts on R side
        if colorR[v][c] != 0 and colorR[v][c] != u:
            # conflict: recolor the edge from colorR[v][c] to v
            u2 = colorR[v][c]
            # find free color for u2
            c2 = 1
            while colorL[u2][c2] != 0:
                c2 += 1
            # find edge index
            for v2, idx2 in adjL[u2]:
                if v2 == v and color[idx2] == c:
                    # recolor
                    color[idx2] = c2
                    colorL[u2][c] = 0
                    colorL[u2][c2] = v
                    colorR[v][c] = u
                    colorR[v][c2] = u2
                    break

# Output
print("YES")
print(" ".join(map(str, color)))