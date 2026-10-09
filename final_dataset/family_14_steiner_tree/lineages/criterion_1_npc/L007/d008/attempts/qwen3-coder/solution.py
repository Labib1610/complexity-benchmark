import sys
from itertools import combinations

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1

def kruskal(n, edges):
    parent = list(range(n))
    rank = [0] * n
    edges.sort()
    cost = 0
    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            cost += w
    return cost

# Read input
n, m, t = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))
edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((w, u-1, v-1))  # Convert to 0-indexed

# If t <= 1, no pairs to enforce
if t <= 1:
    print(0)
    exit()

# For each pair of targets, we need to ensure they're connected in our selected subgraph
# This is equivalent to making sure all targets are in the same connected component
# So we just need to find the minimum spanning tree that connects all targets
# We can do this by running Kruskal's algorithm but only caring about connecting the targets

parent = list(range(n))
rank = [0] * n
edges.sort()
cost = 0
components = {x-1 for x in targets}  # Convert to 0-indexed

# We need to connect all targets into one component
target_set = set(x-1 for x in targets)
target_count = len(target_set)
if target_count <= 1:
    print(0)
    exit()

# Use Kruskal's algorithm to connect all targets with minimal cost
parent = list(range(n))
rank = [0] * n
edges.sort()
cost = 0
connected_targets = {next(iter(target_set))}
remaining_targets = target_set - connected_targets

for w, u, v in edges:
    # Check if this edge helps connect more targets
    pu = find(parent, u)
    pv = find(parent, v)
    
    # If both endpoints are targets and not yet connected, or one is a target and the other connects to a target component
    u_is_target = u in target_set
    v_is_target = v in target_set
    
    # If they're already connected, skip
    if pu == pv:
        continue
        
    # If this edge connects two components and at least one contains a target
    # Actually, let's think differently: run standard Kruskal until all targets are connected
    
    # Standard Kruskal approach
    if pu != pv:
        # Check if this union connects new targets
        # Let's track which targets are in which components
        # But simpler: just do Kruskal and stop when all targets are connected
        
        union(parent, rank, u, v)
        cost += w
        
        # Check if all targets are now connected
        root = find(parent, next(iter(target_set)))
        if all(find(parent, x) == root for x in target_set):
            break

print(cost)