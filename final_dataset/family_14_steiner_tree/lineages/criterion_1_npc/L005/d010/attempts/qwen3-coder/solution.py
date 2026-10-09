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

def kruskal(n, edges, nodes):
    if len(nodes) <= 1:
        return 0
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    cost = 0
    components = {node: node for node in nodes}
    
    for u, v, w in edges:
        if union(parent, rank, u, v):
            cost += w
            # Update component representatives
            rep_u = find(parent, u)
            rep_v = find(parent, v)
            
            # Check if we've connected all critical nodes
            unique_components = set()
            for node in nodes:
                unique_components.add(find(parent, node))
            
            if len(unique_components) == 1:
                break
                
    # Verify all critical nodes are connected
    root = find(parent, nodes[0])
    for node in nodes[1:]:
        if find(parent, node) != root:
            return float('inf')  # Not all critical nodes connected
            
    return cost

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    critical = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
        
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))
    
    # We need to find minimum cost to connect all critical nodes
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Sort edges by weight for Kruskal's algorithm
    edges.sort(key=lambda x: x[2])
    
    cost = 0
    components = set(critical)
    
    for u, v, w in edges:
        # Check if this edge connects two different components containing critical nodes
        pu, pv = find(parent, u), find(parent, v)
        if pu != pv:
            # Count how many critical nodes are in each component
            count_u = sum(1 for node in critical if find(parent, node) == pu)
            count_v = sum(1 for node in critical if find(parent, node) == pv)
            
            if count_u > 0 and count_v > 0:
                # This edge connects components with critical nodes
                union(parent, rank, u, v)
                cost += w
                
                # Update counts
                new_count = count_u + count_v
                # Rebuild components mapping
                for i in range(len(critical)):
                    parent[critical[i]] = find(parent, critical[i])
    
    print(cost)

solve()