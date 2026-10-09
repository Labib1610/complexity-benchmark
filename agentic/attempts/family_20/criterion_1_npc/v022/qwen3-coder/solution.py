import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    edges = []
    adj = defaultdict(list)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Try to 3-color the line graph (each edge is a node, adjacent if they share a vertex)
    # This is equivalent to assigning frequencies 1,2,3 to edges such that edges sharing
    # a vertex have different frequencies
    
    # This is equivalent to edge-coloring the original graph with 3 colors
    # Since every vertex has degree 3, this is essentially checking if the graph
    # is class 1 (edge-colorable with 3 colors)
    
    # We'll model this as a constraint satisfaction problem
    # Each edge needs a color from {1,2,3}
    # Adjacent edges (sharing a vertex) must have different colors
    
    # Build adjacency list for edges (line graph)
    edge_adj = [[] for _ in range(m)]
    for v in range(1, n+1):
        edge_indices = [i for _, i in adj[v]]
        # All edges incident to v are adjacent in line graph
        for i in range(len(edge_indices)):
            for j in range(i+1, len(edge_indices)):
                edge_adj[edge_indices[i]].append(edge_indices[j])
                edge_adj[edge_indices[j]].append(edge_indices[i])
    
    # Now we need to 3-color this graph
    colors = [0] * m  # 0 means uncolored
    
    def is_safe(edge_idx, color):
        for neighbor in edge_adj[edge_idx]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
            
        for color in [1, 2, 3]:
            if is_safe(edge_idx, color):
                colors[edge_idx] = color
                if backtrack(edge_idx + 1):
                    return True
                colors[edge_idx] = 0
        return False
    
    # Optimization: Start with highest degree vertices in line graph
    # But for simplicity and given constraints, we'll try direct backtracking
    # with a small optimization - order edges by vertex to help propagation
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

sys.setrecursionlimit(10000)
solve()