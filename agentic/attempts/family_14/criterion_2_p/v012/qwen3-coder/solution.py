import sys
from collections import defaultdict
import heapq

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

def kruskal(n, edges, priority_nodes):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize Union-Find structure
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Track how many priority nodes are in each component
    priority_count = [0] * (n + 1)
    for node in priority_nodes:
        priority_count[node] = 1
    
    total_cost = 0
    components_with_priority = len(priority_nodes)
    
    for u, v, w in edges:
        pu, pv = find(parent, u), find(parent, v)
        if pu != pv:
            # Merge components
            if rank[pu] < rank[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            if rank[pu] == rank[pv]:
                rank[pu] += 1
            
            # Update priority count in the merged component
            priority_count[pu] += priority_count[pv]
            
            # If we just connected two components that both had priority nodes
            if priority_count[pu] > 0 and priority_count[pv] > 0:
                total_cost += w
                
            # If this merge creates a component with all priority nodes, we're done
            if priority_count[pu] == len(priority_nodes):
                break
    
    return total_cost

# Read input
line1 = list(map(int, sys.stdin.readline().split()))
n, m, t = line1[0], line1[1], line1[2]

priority_centers = list(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

# Handle special case: if there's only one priority center, cost is 0
if t <= 1:
    print(0)
else:
    result = kruskal(n, edges, priority_centers)
    print(result)