import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list and edge list
    adj = defaultdict(list)
    edges = []
    
    for i in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append((v, i))
        adj[v].append((u, i))
        edges.append((u, v))
    
    # Since each node has exactly 3 edges, and m = 3*n/2, this is a cubic graph
    
    # Try to 3-color the edges such that edges incident to each vertex have different colors
    # This is equivalent to finding a proper edge coloring with 3 colors
    
    # We'll use BFS to color the edges
    color = [-1] * m  # -1 means uncolored
    
    # For each component, we need to do BFS traversal
    visited_nodes = [False] * n
    visited_edges = [False] * m
    
    for start_node in range(n):
        if visited_nodes[start_node]:
            continue
            
        # BFS from start_node
        queue = deque([start_node])
        visited_nodes[start_node] = True
        
        while queue:
            node = queue.popleft()
            
            # Get the colors used by existing edges
            used_colors = set()
            colored_edges = []
            
            for neighbor, edge_idx in adj[node]:
                if color[edge_idx] != -1:  # Already colored
                    used_colors.add(color[edge_idx])
                    colored_edges.append(edge_idx)
            
            # Color uncolored edges incident to this node
            available_colors = {1, 2, 3} - used_colors
            
            for neighbor, edge_idx in adj[node]:
                if color[edge_idx] == -1:  # Not yet colored
                    if available_colors:
                        c = available_colors.pop()
                        color[edge_idx] = c
                        used_colors.add(c)
                    else:
                        # No available color, which shouldn't happen in a proper cubic graph
                        # But let's handle it properly
                        needed_color = None
                        for c in {1, 2, 3}:
                            if c not in used_colors:
                                needed_color = c
                                break
                        
                        if needed_color is None:
                            print("NO")
                            return
                        
                        color[edge_idx] = needed_color
                    
                    # Mark neighbor as visited if not already
                    if not visited_nodes[neighbor]:
                        visited_nodes[neighbor] = True
                        queue.append(neighbor)
    
    # Verify the solution
    for i in range(n):
        colors_at_node = set()
        for neighbor, edge_idx in adj[i]:
            if color[edge_idx] in colors_at_node:
                print("NO")
                return
            colors_at_node.add(color[edge_idx])
        
        if len(colors_at_node) != 3:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()