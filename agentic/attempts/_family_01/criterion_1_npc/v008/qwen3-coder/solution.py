import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list for conflicts
    conflicts = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        conflicts[u].add(v)
        conflicts[v].add(u)
    
    # Try to 3-color the graph
    colors = [0] * (n + 1)  # colors[i] represents the shift of worker i
    
    def is_safe(node, color):
        # Check if assigning 'color' to 'node' conflicts with neighbors
        for neighbor in conflicts[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        # If already colored (from previous constraints), move to next
        if colors[node] != 0:
            return backtrack(node + 1)
            
        # Try colors 1, 2, 3
        for color in range(1, 4):
            if is_safe(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0  # Backtrack
                
        return False
    
    # Handle connected components separately for better efficiency
    visited = [False] * (n + 1)
    component_colors = {}
    
    def dfs(node, component_nodes):
        component_nodes.append(node)
        visited[node] = True
        for neighbor in conflicts[node]:
            if not visited[neighbor]:
                dfs(neighbor, component_nodes)
    
    # Process each connected component
    possible = True
    for start_node in range(1, n + 1):
        if not visited[start_node]:
            component_nodes = []
            dfs(start_node, component_nodes)
            
            # For this component, try to color it
            component_assignment = {}
            
            def color_component(nodes, idx):
                if idx == len(nodes):
                    return True
                    
                current_node = nodes[idx]
                for color in range(1, 4):
                    # Check if this color is valid for current node
                    valid = True
                    for neighbor in conflicts[current_node]:
                        if neighbor in component_assignment and component_assignment[neighbor] == color:
                            valid = False
                            break
                            
                    if valid:
                        component_assignment[current_node] = color
                        if color_component(nodes, idx + 1):
                            return True
                        del component_assignment[current_node]
                        
                return False
            
            if not color_component(component_nodes, 0):
                possible = False
                break
            else:
                # Apply the coloring to global colors array
                for node in component_nodes:
                    colors[node] = component_assignment[node]
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(*colors[1:])  # Print colors for nodes 1 to n

solve()