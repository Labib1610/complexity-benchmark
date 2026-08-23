import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No constraints, all 1s is the lexicographically smallest solution
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For each edge (u,v), we need gain[u] * gain[v] = 2
    # This means exactly one of them should be 1 and the other should be 2
    # This is equivalent to a 2-coloring problem where:
    # - If gain[u] = 1, then gain[v] = 2
    # - If gain[u] = 2, then gain[v] = 1
    
    # Color: 0 means gain=1, 1 means gain=2
    color = {}
    gain = {}
    
    # Check if the graph is bipartite
    for start_node in range(1, n + 1):
        if start_node not in color:  # Unvisited component
            queue = deque([start_node])
            color[start_node] = 0  # Start with color 0 (gain=1)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                current_gain = 1 if current_color == 0 else 2
                
                for neighbor in adj[node]:
                    if neighbor not in color:
                        # Assign opposite color
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Conflict: same color but should be different
                        print("NO")
                        return
    
    # Verify all edges satisfy the constraint
    for u, v in edges:
        gain_u = 1 if color[u] == 0 else 2
        gain_v = 1 if color[v] == 0 else 2
        if gain_u * gain_v != 2:
            print("NO")
            return
    
    # Construct the lexicographically smallest solution
    # For each component, we can choose which color represents gain=1
    # To get lexicographically smallest, we want earlier nodes to be 1 if possible
    
    result = [0] * (n + 1)  # 1-indexed
    
    # Process each component
    visited_component = set()
    
    for node in range(1, n + 1):
        if node not in visited_component:
            # Collect all nodes in this component
            component_nodes = []
            queue = deque([node])
            visited_component.add(node)
            component_nodes.append(node)
            
            while queue:
                current = queue.popleft()
                for neighbor in adj[current]:
                    if neighbor not in visited_component:
                        visited_component.add(neighbor)
                        component_nodes.append(neighbor)
                        queue.append(neighbor)
            
            # For lexicographically smallest, we want to minimize the values
            # We can flip the coloring of the entire component if needed
            # Choose the coloring that gives the smallest lex order
            
            # Try both colorings
            # Coloring 0: color -> gain mapping as is
            # Coloring 1: flip all colors in component
            
            option1 = []
            option2 = []
            
            for v in range(1, n + 1):
                if v in color:
                    gain_val = 1 if color[v] == 0 else 2
                    option1.append(gain_val)
                    option2.append(3 - gain_val)  # Flip: 1->2, 2->1
                else:
                    option1.append(1)  # Isolated node, set to 1
                    option2.append(1)
            
            # Check which option is valid
            valid_option1 = True
            valid_option2 = True
            
            for u, v in edges:
                if option1[u-1] * option1[v-1] != 2:
                    valid_option1 = False
                if option2[u-1] * option2[v-1] != 2:
                    valid_option2 = False
            
            chosen_option = option1 if valid_option1 else option2
            
            # Apply the chosen option to result
            for i in range(1, n + 1):
                if i <= len(chosen_option):
                    result[i] = chosen_option[i-1]
    
    # Handle isolated nodes (nodes with no edges)
    for i in range(1, n + 1):
        if result[i] == 0:
            result[i] = 1  # Lexicographically smallest choice
    
    print("YES")
    print(" ".join(map(str, result[1:])))

solve()