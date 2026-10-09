import sys
from collections import deque

input = sys.stdin.readline

nL, nR, m = map(int, input().split())
edges = []
adj = [[] for _ in range(nL + nR + 1)]
deg = [0] * (nL + nR + 1)

for i in range(m):
    u, v = map(int, input().split())
    v += nL  # shift right side indices
    edges.append((u, v))
    adj[u].append((v, i))
    adj[v].append((u, i))
    deg[u] += 1
    deg[v] += 1

Delta = max(deg) if m > 0 else 0
color = [-1] * m

# Greedy edge coloring with color swapping
for u in range(1, nL + 1):
    used = [False] * (Delta + 1)
    for v, idx in adj[u]:
        if color[idx] != -1:
            used[color[idx]] = True
    # find smallest free color for each edge from u
    for v, idx in adj[u]:
        if color[idx] != -1:
            continue
        # find smallest free color for u
        c = 1
        while c <= Delta and used[c]:
            c += 1
        # assign
        color[idx] = c
        used[c] = True
        # now fix conflicts on v side
        while True:
            # check if v has this color already
            conflict = -1
            for w, j in adj[v]:
                if color[j] == c and j != idx:
                    conflict = j
                    break
            if conflict == -1:
                break
            # recolor conflict edge
            old = color[conflict]
            color[conflict] = c
            used[old] = False
            used[c] = True
            # move to the other endpoint of conflict edge
            u2, v2 = edges[conflict]
            if u2 == v:
                v = v2
            else:
                v = u2
            idx = conflict
            c = old

print("YES")
print(" ".join(str(color[i]) for i in range(m)))