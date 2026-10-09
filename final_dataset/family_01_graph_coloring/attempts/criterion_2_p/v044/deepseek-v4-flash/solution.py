import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n

def bfs(start):
    q = deque([start])
    color[start] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            print("NO")
            sys.exit()

# Now we have a valid 2-coloring, but we want lexicographically smallest.
# color 0 -> phase 1, color 1 -> phase 2
# But we can try to flip components to get smaller lexicographic order.
# We'll do BFS/DFS and for each uncolored component, try both colorings and pick lexicographically smaller.

# Rebuild with component info
visited = [False] * n
comp_id = [-1] * n
comps = []
cid = 0
for i in range(n):
    if not visited[i]:
        q = deque([i])
        visited[i] = True
        comp = []
        while q:
            u = q.popleft()
            comp.append(u)
            comp_id[u] = cid
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        comps.append(comp)
        cid += 1

# For each component, we can flip colors (0<->1) independently.
# We want lexicographically smallest final assignment.
# color 0 -> 1, color 1 -> 2
# Flipping a component swaps 1<->2 for all nodes in it.

# We'll try to assign smallest possible value to smallest index.
# Since components are independent, we can decide per component.

# First, get base coloring from earlier BFS (color array)
# We'll try to flip components if it makes the smallest node in that component smaller.

# Build component nodes sorted
for comp in comps:
    comp.sort()
    # Try both options and pick lexicographically smaller for the whole array
    # Option 1: keep as is
    # Option 2: flip
    # We'll compare by looking at the smallest index where they differ.
    # Since we process components in order of smallest node, we can decide greedily.
    # But we need global comparison, so we'll just simulate both and pick better.

# Let's just do: for each component, try flipping if it makes the assignment lexicographically smaller.
# We'll compare the two possible assignments for that component only, given fixed others.

# But since components are independent, we can decide per component by comparing the two colorings
# restricted to that component, because other components are unchanged.

# So for each component, generate two possible assignments:
# assign1: color as is
# assign2: flipped
# Compare the two sequences for nodes in this component (sorted) and pick smaller.

result = [0] * n
for comp in comps:
    comp.sort()
    # option A: keep color
    optA = [color[u] for u in comp]
    # option B: flip
    optB = [1 - color[u] for u in comp]
    # choose lexicographically smaller
    if optA <= optB:
        for u, c in zip(comp, optA):
            result[u] = c
    else:
        for u, c in zip(comp, optB):
            result[u] = c

# Convert 0->1, 1->2
ans = [1 if c == 0 else 2 for c in result]
print("YES")
print(" ".join(map(str, ans)))