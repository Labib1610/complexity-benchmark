import sys
from collections import deque

input = sys.stdin.readline

nT, nP, m = map(int, input().split())
edges = []
adjT = [[] for _ in range(nT)]
adjP = [[] for _ in range(nP)]
degT = [0] * nT
degP = [0] * nP

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v))
    adjT[u].append((v, i))
    adjP[v].append((u, i))
    degT[u] += 1
    degP[v] += 1

K = max(max(degT, default=0), max(degP, default=0))
color = [-1] * m

# We'll use a simple greedy with augmenting paths to color edges
# For each edge, find a free color for both endpoints, if conflict, recolor.

# We'll store for each vertex the set of used colors
usedT = [set() for _ in range(nT)]
usedP = [set() for _ in range(nP)]

# For each edge, assign a color
for idx, (u, v) in enumerate(edges):
    # Find a color not used by u or v
    c = 1
    while c in usedT[u] or c in usedP[v]:
        c += 1
    # Assign
    color[idx] = c
    usedT[u].add(c)
    usedP[v].add(c)

# Now we must ensure no color exceeds K. Since K is max degree, greedy may exceed K.
# We'll fix by recoloring with augmenting paths.

# Build adjacency for current coloring
# We'll implement the standard algorithm:
# For each color c from 1..K, find a matching and assign.

# Reset
color = [-1] * m
# For each color, find a maximal matching in the subgraph of uncolored edges
for c in range(1, K + 1):
    # Build graph of uncolored edges
    adj = [[] for _ in range(nT)]
    for i, (u, v) in enumerate(edges):
        if color[i] == -1:
            adj[u].append(i)
    # Find matching
    matchT = [-1] * nT
    matchP = [-1] * nP
    for u in range(nT):
        if matchT[u] == -1:
            # BFS augment
            visited = [False] * nP
            parent = [-1] * nP
            q = deque([u])
            found = False
            while q and not found:
                x = q.popleft()
                for ei in adj[x]:
                    v = edges[ei][1]
                    if not visited[v]:
                        visited[v] = True
                        parent[v] = x
                        if matchP[v] == -1:
                            # augment
                            while v != -1:
                                x = parent[v]
                                ei = None
                                for e2 in adj[x]:
                                    if edges[e2][1] == v and color[e2] == -1:
                                        ei = e2
                                        break
                                nxt = matchT[x]
                                color[ei] = c
                                matchT[x] = v
                                matchP[v] = x
                                v = nxt
                            found = True
                            break
                        else:
                            q.append(matchP[v])
            # If no augmenting path, just leave uncolored (shouldn't happen if K is correct)

# Output
print("YES")
print(" ".join(str(color[i]) for i in range(m)))