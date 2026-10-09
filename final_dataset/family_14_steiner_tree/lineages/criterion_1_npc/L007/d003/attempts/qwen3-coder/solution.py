import sys
import heapq
from collections import defaultdict

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def kruskal(nodes, edges):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    edges.sort()
    cost = 0
    connected = 0
    for w, u, v in edges:
        if union(parent, rank, u, v):
            cost += w
            connected += 1
            if connected == len(nodes) - 1:
                break
    return cost

n, m, t = map(int, sys.stdin.readline().split())
priorities = list(map(int, sys.stdin.readline().split()))

if t <= 1:
    print(0)
    exit()

edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((w, u, v))

# We need to connect all priority nodes with minimum cost
# This is essentially finding the Minimum Spanning Tree of the subgraph 
# induced by the priority nodes and any additional nodes needed

# But we can also think of it as finding the MST of the whole graph,
# but only considering connections between priority nodes.

# Better approach: Use Kruskal's algorithm on the full graph,
# but only track when priority nodes get connected.

parent = list(range(n + 1))
rank = [0] * (n + 1)

# Sort edges by weight
edges.sort()

cost = 0
priority_set = set(priorities)
# Create a mapping from component root to set of priority nodes in that component
component_priorities = defaultdict(set)
for p in priorities:
    component_priorities[p].add(p)

# Initially each priority node is in its own component
components_count = len(priorities)

for w, u, v in edges:
    pu = find(parent, u)
    pv = find(parent, v)
    
    if pu != pv:
        # Union the components
        if rank[pu] < rank[pv]:
            pu, pv = pv, pu
        parent[pv] = pu
        if rank[pu] == rank[pv]:
            rank[pu] += 1
            
        # Merge the priority sets
        component_priorities[pu] |= component_priorities[pv]
        del component_priorities[pv]
        
        # Check how many priority nodes are now connected
        if len(component_priorities[pu]) > 1:
            cost += w
            # If all priorities are connected, we're done
            if len(component_priorities[pu]) == len(priorities):
                break

print(cost)