import sys

# Increase recursion depth for deep DFS calls
sys.setrecursionlimit(10000)

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return
    
    # Adjacency list to store neighbors and corresponding edge indices
    adj = [[] for _ in range(n + 1)]
    
    # Read edges
    edges = []
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Initialize edge colors (0 means uncolored)
    colors = [0] * m
    
    # Process each vertex
    for u in range(1, n + 1):
        # Check if any edge incident to u is uncolored
        uncolored_edges = []
        for (v, edge_idx) in adj[u]:
            if colors[edge_idx] == 0:
                uncolored_edges.append((v, edge_idx))
        
        # If all edges are colored, verify the constraint
        if not uncolored_edges:
            used_colors = set()
            for (v, edge_idx) in adj[u]:
                used_colors.add(colors[edge_idx])
            if len(used_colors) != 3:
                print("NO")
                return
            continue
        
        # If there are uncolored edges, we need to color them
        # First, check if we have exactly 3 edges (as per problem guarantee)
        if len(adj[u]) != 3:
            print("NO")
            return
        
        # Find used colors at this vertex
        used_colors = set()
        for (v, edge_idx) in adj[u]:
            if colors[edge_idx] != 0:
                used_colors.add(colors[edge_idx])
        
        # If more than 3 different colors are used, impossible
        if len(used_colors) > 3:
            print("NO")
            return
        
        # Available colors
        all_colors = {1, 2, 3}
        available_colors = all_colors - used_colors
        
        # If no available colors but still have uncolored edges, impossible
        if not available_colors and uncolored_edges:
            print("NO")
            return
        
        # Color the uncolored edges
        available_list = list(available_colors)
        for idx, (v, edge_idx) in enumerate(uncolored_edges):
            if idx < len(available_list):
                colors[edge_idx] = available_list[idx]
            else:
                # This shouldn't happen if constraints are satisfied
                print("NO")
                return
    
    # Final verification: check all vertices have exactly 3 different colors
    for u in range(1, n + 1):
        vertex_colors = set()
        for (v, edge_idx) in adj[u]:
            vertex_colors.add(colors[edge_idx])
        if len(vertex_colors) != 3:
            print("NO")
            return
    
    # Output result
    print("YES")
    print(" ".join(map(str, colors)))

if __name__ == "__main__":
    solve()