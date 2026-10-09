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

def main():
    n, m, t = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # Make a copy of the edges for the MST algorithm
    edges.sort()
    
    # First, build a spanning tree that connects all critical nodes with minimum cost
    # This is essentially a Minimum Spanning Tree problem with a twist:
    # We want to connect all critical nodes, not necessarily all nodes
    
    # Use a modified Kruskal's algorithm
    parent = list(range(n+1))
    rank = [0] * (n+1)
    
    # We'll use a Union-Find approach but we're really looking to connect 
    # all critical nodes. We can think of this as finding the minimum cost
    # to make all critical nodes connected.
    
    # Alternative approach: Create a graph where we want to connect all critical nodes.
    # The minimum way to do this is to find the minimum spanning tree of the subgraph
    # induced by the critical nodes, with edge weights being the shortest path distances
    # between them in the original graph. But that's complex.
    
    # Simpler approach: 
    # Run Kruskal's algorithm until all critical nodes are in the same component.
    
    total_cost = 0
    critical_components = len(critical)
    critical_parents = {c: c for c in critical}
    
    # Reset parent and rank for our specific use
    parent = list(range(n+1))
    rank = [0] * (n+1)
    
    for w, u, v in edges:
        pu = find(parent, u)
        pv = find(parent, v)
        
        if pu != pv:
            union(parent, rank, u, v)
            total_cost += w
            
            # Check how many separate critical components we have now
            critical_roots = set()
            for c in critical:
                critical_roots.add(find(parent, c))
            
            if len(critical_roots) == 1:
                break
    
    print(total_cost)

if __name__ == "__main__":
    main()