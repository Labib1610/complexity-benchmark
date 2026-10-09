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
    
    # Each node has exactly 3 edges
    # We need to color edges such that each node has edges of 3 different colors
    
    # This is equivalent to edge coloring of a 3-regular graph
    # We can use BFS to assign colors
    
    color = [0] * m  # 1, 2, 3
    colored = [False] * m
    
    # For each node, we track which colors are used by its edges
    node_colors = defaultdict(set)
    
    # Process edges one by one using BFS-like approach
    queue = deque()
    visited = [False] * (n + 1)
    
    # Start from node 1
    queue.append(1)
    visited[1] = True
    
    while queue:
        node = queue.popleft()
        
        # Get available colors for this node
        used_colors = node_colors[node]
        available_colors = {1, 2, 3} - used_colors
        
        # Process each edge of this node
        for neighbor, edge_idx in adj[node]:
            if not colored[edge_idx]:
                # Assign a color that is not used by either endpoint
                edge_colors_used = node_colors[node] | node_colors[neighbor]
                available = {1, 2, 3} - edge_colors_used
                
                if not available:
                    print("NO")
                    return
                
                # Assign the first available color
                c = available.pop()
                color[edge_idx] = c
                colored[edge_idx] = True
                
                # Update color sets for both endpoints
                node_colors[node].add(c)
                node_colors[neighbor].add(c)
            
            # Add neighbor to queue if not visited
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    
    # Check if all edges are colored
    if not all(colored):
        # Try to color remaining edges
        for i in range(m):
            if not colored[i]:
                u, v = edges[i]
                used = node_colors[u] | node_colors[v]
                available = {1, 2, 3} - used
                if not available:
                    print("NO")
                    return
                c = available.pop()
                color[i] = c
                node_colors[u].add(c)
                node_colors[v].add(c)
    
    print("YES")
    print(' '.join(map(str, color)))

solve()