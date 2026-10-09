import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    graph = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))
    
    # Try all possible assignments
    # Each node can have value 1, 2, or 3
    # We'll use backtracking/BFS approach
    
    # Check if a given assignment is valid
    def is_valid_assignment(assignment):
        for u, v in edges:
            val_u = assignment[u]
            val_v = assignment[v]
            # Valid pairs are {1,2}, {1,3}, {2,3}
            if not ((val_u == 1 and val_v == 2) or (val_u == 2 and val_v == 1) or
                    (val_u == 1 and val_v == 3) or (val_u == 3 and val_v == 1) or
                    (val_u == 2 and val_v == 3) or (val_u == 3 and val_v == 2)):
                return False
        return True
    
    # Try all 3^n possibilities
    # But this is too slow for n=40, so we need a smarter approach
    
    # This is essentially a graph coloring problem where:
    # Colors are 1, 2, 3
    # Adjacent nodes can have colors (1,2), (1,3), or (2,3) - but NOT (1,1), (2,2), or (3,3)
    # AND they can't have the same color
    
    # So this is a valid edge coloring where endpoints must have different colors
    # And the allowed color pairs are the ones mentioned
    
    # Let's model this as 2-SAT or try to find a valid 3-coloring with constraints
    
    # Actually, let's think differently:
    # For each edge, the pair of values must be one of: (1,2), (1,3), (2,3) in some order
    # This means no two adjacent nodes can have the same value
    
    # This is exactly a 3-coloring problem!
    # Where colors are 1, 2, 3 and adjacent nodes must have different colors
    
    # But wait, let's check what's allowed more carefully:
    # Allowed pairs when we don't care about order: {1,2}, {1,3}, {2,3}
    # This means adjacent nodes cannot both be 1, cannot both be 2, cannot both be 3
    
    # So this IS a proper 3-coloring problem
    
    # Use BFS/DFS to try to 3-color the graph
    # assignment[i] represents the color of node i (1-indexed)
    assignment = [0] * (n + 1)  # 0 means unassigned
    
    def dfs(node):
        # Try colors 1, 2, 3 for this node
        for color in [1, 2, 3]:
            # Check if this color is valid with all neighbors
            valid = True
            for neighbor in graph[node]:
                if assignment[neighbor] == color:
                    valid = False
                    break
            
            if valid:
                assignment[node] = color
                # Find next unassigned node
                next_node = 0
                for i in range(1, n + 1):
                    if assignment[i] == 0:
                        next_node = i
                        break
                
                if next_node == 0:  # All nodes assigned
                    return True
                
                if dfs(next_node):
                    return True
                
                assignment[node] = 0  # Backtrack
        
        return False
    
    # Start with node 1
    assignment[1] = 1
    next_node = 0
    for i in range(1, n + 1):
        if assignment[i] == 0:
            next_node = i
            break
    
    found = False
    if next_node == 0:  # Only one node
        found = True
    else:
        found = dfs(next_node)
    
    # If that didn't work, try starting with color 2 for node 1
    if not found:
        assignment = [0] * (n + 1)
        assignment[1] = 2
        next_node = 0
        for i in range(1, n + 1):
            if assignment[i] == 0:
                next_node = i
                break
        
        if next_node == 0:
            found = True
        else:
            found = dfs(next_node)
    
    # If that didn't work, try starting with color 3 for node 1
    if not found:
        assignment = [0] * (n + 1)
        assignment[1] = 3
        next_node = 0
        for i in range(1, n + 1):
            if assignment[i] == 0:
                next_node = i
                break
        
        if next_node == 0:
            found = True
        else:
            found = dfs(next_node)
    
    if found:
        # Verify the solution
        if is_valid_assignment(assignment):
            print("YES")
            result = []
            for i in range(1, n + 1):
                result.append(str(assignment[i]))
            print(" ".join(result))
        else:
            print("NO")
    else:
        print("NO")

solve()