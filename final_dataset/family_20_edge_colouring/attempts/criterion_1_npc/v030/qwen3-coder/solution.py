import sys
from collections import defaultdict

def main():
    n, m = map(int, sys.stdin.readline().split())
    
    # Read edges
    edges = []
    adj = defaultdict(list)
    degree = [0] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Check if it's a valid graph where each node has same degree
    d = degree[1]
    for i in range(1, n + 1):
        if degree[i] != d:
            print("NO")
            return
    
    # Number of windows equals the degree of each node
    windows = d
    
    # Try to color the edges with d colors such that edges incident to 
    # each vertex have different colors
    
    # This is edge coloring of a regular graph
    # We can use Vizing's theorem - since this is a regular graph,
    # it can be edge-colored with d colors
    
    # We'll build the coloring using a greedy approach
    # For each vertex, we keep track of which colors are used on its edges
    
    edge_colors = [0] * m  # 1-indexed result
    vertex_edges = [[] for _ in range(n + 1)]  # For each vertex, list of (neighbor, edge_index)
    
    # Build adjacency with edge indices
    for idx, (u, v) in enumerate(edges):
        vertex_edges[u].append((v, idx))
        vertex_edges[v].append((u, idx))
    
    # For each vertex, we need to assign colors to its edges
    # We'll process vertices one by one and try to assign colors greedily
    
    # Used colors at each vertex
    used_colors = [set() for _ in range(n + 1)]
    
    # Process edges and assign colors
    for idx, (u, v) in enumerate(edges):
        # Find a color not used at either u or v
        color = 1
        while color in used_colors[u] or color in used_colors[v]:
            color += 1
        edge_colors[idx] = color
        used_colors[u].add(color)
        used_colors[v].add(color)
    
    # Check if we used more colors than allowed
    if max(edge_colors) > windows:
        print("NO")
        return
        
    print("YES")
    print(' '.join(map(str, edge_colors)))

if __name__ == "__main__":
    main()