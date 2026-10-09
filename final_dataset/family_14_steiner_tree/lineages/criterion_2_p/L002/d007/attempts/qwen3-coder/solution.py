import sys
from collections import defaultdict
import heapq

def find_mst(n, edges):
    # Prim's algorithm to find Minimum Spanning Tree
    # We want to find the MST of the graph where we exclude target nodes
    # Actually, let's think differently.
    
    # The key insight: we want all target nodes to have the same value in any null space vector.
    # This means they must be connected in the graph formed by selected edges.
    # Non-target nodes can be used as intermediaries.
    
    # But actually, since the full graph has null space dimension 1 (spanned by all ones),
    # removing edges increases the null space dimension.
    # To force target nodes to have equal values, we need to ensure they are connected
    # through the remaining edges.
    
    # Let's model this correctly:
    # We have a graph with n nodes and m=n-1 edges forming a tree (since null space dim is 1).
    # We want to remove some edges such that in the remaining graph,
    # all target nodes are in the same connected component.
    
    # This is equivalent to finding a spanning forest where all targets are in one component.
    # Or, in the complement view, removing minimum weight edges such that 
    # the remaining graph connects all targets together.
    
    # Since the original graph is a tree, and we want to keep all targets connected,
    # we should find the minimal way to connect all targets.
    
    # Strategy:
    # 1. Contract all target nodes into one "super node"
    # 2. Find the MST of the resulting graph
    # 3. This is equivalent to finding the minimal edges to keep targets connected
    
    pass

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    targets = list(map(int, data[idx:idx+t]))
    idx += t
    
    # Convert to 0-indexed
    targets = [x - 1 for x in targets]
    
    edges = []
    for i in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
    
    # If there's only one target, condition is automatically satisfied
    if t <= 1:
        print(0)
        return
    
    # The original graph forms a tree (n nodes, n-1 edges, null space dim 1)
    # We want to find minimum cost subset such that all targets are connected
    # This is equivalent to finding the minimum spanning tree where all targets
    # are contracted to one node, then finding the MST of the resulting graph
    
    # But simpler approach:
    # Since we start with a tree, and we want to keep all targets in one component,
    # we can use Union-Find.
    # We contract all targets to one node (say, targets[0])
    # Then find the MST of the resulting graph
    
    # Create a mapping for contraction
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    # Contract all targets to the first target
    first_target = targets[0]
    for target in targets[1:]:
        parent[target] = first_target
    
    # Sort edges by weight
    edges.sort()
    
    total_cost = 0
    edges_used = 0
    
    # Kruskal's algorithm on the contracted graph
    for w, u, v in edges:
        if union(u, v):
            total_cost += w
            edges_used += 1
            # In a tree with n nodes, we need n-1 edges
            # But we've contracted t nodes into 1, so we have (n-t+1) nodes
            # We need (n-t+1)-1 = n-t edges
            if edges_used == n - t:
                break
    
    print(total_cost)

solve()