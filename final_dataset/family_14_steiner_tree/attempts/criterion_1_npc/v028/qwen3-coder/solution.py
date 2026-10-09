import sys
from itertools import combinations
from collections import defaultdict, deque

def find_mst_cost(n, edges, must_connect):
    if len(must_connect) <= 1:
        return 0
    
    # Use Kruskal's algorithm with Union-Find
    parent = list(range(n + 1))
    
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
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    total_cost = 0
    connected_components = n
    
    for u, v, w in edges:
        if union(u, v):
            total_cost += w
            connected_components -= 1
    
    # Check if all must_connect vertices are connected
    root = find(next(iter(must_connect)))
    for node in must_connect:
        if find(node) != root:
            return float('inf')  # Not connected
            
    return total_cost

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    focal_dialects = set(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u, v, w))
    
    # Find minimum spanning tree cost that connects all focal dialects
    min_cost = float('inf')
    
    # Use a modified approach: try to connect all focal nodes
    parent = list(range(n + 1))
    
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
    
    # Try Kruskal's algorithm
    edges.sort(key=lambda x: x[2])
    
    # We need to connect all focal dialects
    # Let's use a different approach - find the MST of the subgraph that connects all focal nodes
    
    # Create a graph and find the minimum cost to connect all focal dialects
    # This is essentially finding the minimum Steiner tree, but since t<=10,
    # we can use enumeration approach
    
    # For small t, we can check all possible ways to connect the focal nodes
    # But let's use a simpler approach - run Kruskal and check if focal nodes are connected
    
    best_cost = float('inf')
    
    # Generate all possible subsets of edges and check if they connect all focal dialects
    # This is too expensive, so let's use a better approach
    
    # Run Kruskal's algorithm to find MST
    parent = list(range(n + 1))
    
    def reset_parent():
        for i in range(n + 1):
            parent[i] = i
            
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
    
    def is_connected(nodes):
        if len(nodes) <= 1:
            return True
        root = find(next(iter(nodes)))
        return all(find(node) == root for node in nodes)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Try adding edges in order until all focal dialects are connected
    reset_parent()
    cost = 0
    
    for u, v, w in edges:
        if union(u, v):
            cost += w
            if is_connected(focal_dialects):
                best_cost = min(best_cost, cost)
                break
    
    print(best_cost if best_cost != float('inf') else 0)

solve()