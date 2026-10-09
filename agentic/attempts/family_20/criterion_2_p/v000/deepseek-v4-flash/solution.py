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

Delta = max(max(degL), max(degR))

# Build adjacency lists for left and right
adjL = [[] for _ in range(nL + 1)]
adjR = [[] for _ in range(nR + 1)]
for idx, (u, v) in enumerate(edges):
    adjL[u].append((v, idx))
    adjR[v].append((u, idx))

color = [0] * m

# For each left vertex, assign colors to its incident edges
for u in range(1, nL + 1):
    used = [False] * (Delta + 1)
    for v, idx in adjL[u]:
        if color[idx] != 0:
            used[color[idx]] = True
    # Find free colors for each edge
    for v, idx in adjL[u]:
        if color[idx] == 0:
            c = 1
            while c <= Delta and used[c]:
                c += 1
            color[idx] = c
            used[c] = True

# Now fix conflicts on right side using Kempe chain argument
# We'll do a BFS/DFS to recolor if needed
for v in range(1, nR + 1):
    # Check colors on this right vertex
    color_count = {}
    for u, idx in adjR[v]:
        c = color[idx]
        if c in color_count:
            # conflict: need to recolor one of them
            # find alternate color for the second edge
            other_idx = color_count[c]
            # Try to recolor other_idx to a free color
            used = [False] * (Delta + 1)
            for u2, idx2 in adjR[v]:
                used[color[idx2]] = True
            # also check left side of other_idx
            u_other, _ = edges[other_idx]
            for v2, idx2 in adjL[u_other]:
                used[color[idx2]] = True
            alt = 1
            while alt <= Delta and used[alt]:
                alt += 1
            if alt <= Delta:
                color[other_idx] = alt
            else:
                # Kempe chain: swap colors along alternating path
                # find path starting from other_idx
                stack = [(other_idx, c, alt)]
                visited = set()
                while stack:
                    eidx, c1, c2 = stack.pop()
                    if eidx in visited:
                        continue
                    visited.add(eidx)
                    color[eidx] = c2
                    uu, vv = edges[eidx]
                    # find other edge at uu with color c2
                    for v2, idx2 in adjL[uu]:
                        if idx2 != eidx and color[idx2] == c2:
                            stack.append((idx2, c2, c1))
                    # find other edge at vv with color c2
                    for u2, idx2 in adjR[vv]:
                        if idx2 != eidx and color[idx2] == c2:
                            stack.append((idx2, c2, c1))
        else:
            color_count[c] = idx

print("YES")
print(" ".join(map(str, color)))