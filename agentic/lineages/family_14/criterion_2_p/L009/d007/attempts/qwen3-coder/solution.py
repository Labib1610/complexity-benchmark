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

def kruskal_with_critical_nodes(n, edges, critical_nodes):
    if len(critical_nodes) <= 1:
        return 0
    
    # Convert to set for faster lookup
    critical_set = set(critical_nodes)
    
    # First, build connected components using Union-Find
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # We'll track which components contain critical nodes
    critical_in_component = defaultdict(set)
    for node in critical_set:
        critical_in_component[node].add(node)
    
    total_cost = 0
    
    for u, v, w in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)
        
        if root_u != root_v:
            # Check if this edge connects components with critical nodes
            crit_u = critical_in_component[root_u]
            crit_v = critical_in_component[root_v]
            
            # Union the components
            if rank[root_u] < rank[root_v]:
                root_u, root_v = root_v, root_u
            parent[root_v] = root_u
            if rank[root_u] == rank[root_v]:
                rank[root_u] += 1
                
            # Merge the critical node sets
            critical_in_component[root_u] |= critical_in_component[root_v]
            critical_in_component[root_v] = set()
            
            # If we connected two components that both had critical nodes,
            # we needed this edge
            if crit_u and crit_v:
                total_cost += w
    
    return total_cost

# Read input
line1 = list(map(int, sys.stdin.readline().split()))
N, E, F = line1[0], line1[1], line1[2]

critical_nodes = list(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, w))

# Solve and print result
result = kruskal_with_critical_nodes(N, edges, critical_nodes)
print(result)