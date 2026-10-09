import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Color graph with 3 colors
    # Each node can be colored with 1, 2, or 3
    # Adjacent nodes must have different colors
    # But we also need to ensure that connected nodes are assigned perpendicular axes
    # Axes 1, 2, 3 correspond to X, Y, Z
    # Perpendicular pairs: (1,2), (1,3), (2,3)
    
    # This is equivalent to checking if the graph is 3-colorable
    # However, we have additional constraints - each edge represents perpendicularity
    # So we need to ensure that adjacent nodes get colors that represent perpendicular axes
    
    # Let's think differently:
    # We can model this as a graph coloring problem where:
    # Each node gets color 1, 2, or 3
    # Adjacent nodes must get colors that are different and represent perpendicular axes
    # Colors 1, 2, 3 represent X, Y, Z axes respectively
    # Perpendicular combinations: (1,2), (1,3), (2,3)
    # So adjacent nodes can't have the same color, and they can't have "parallel" assignment
    # Wait, actually all pairs (1,2), (1,3), (2,3) are perpendicular!
    # So this is just normal 3-coloring where adjacent nodes must have different colors
    
    # But wait, let's re-read the problem:
    # "any two modules joined by a strut must be aligned to perpendicular axes"
    # Axes 1, 2, 3 are all mutually perpendicular
    # So any two different axes are perpendicular
    # So adjacent nodes must have different axis assignments
    
    # This is simply graph 3-coloring problem
    
    color = [-1] * n  # -1 means uncolored, 1, 2, 3 are colors
    
    def is_valid_color(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def dfs(node):
        if color[node] != -1:
            return True
            
        for c in [1, 2, 3]:
            if is_valid_color(node, c):
                color[node] = c
                # Check if we can color all neighbors
                valid = True
                neighbors_to_color = []
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        neighbors_to_color.append(neighbor)
                
                # Try to color neighbors
                neighbor_colors = {}
                for neighbor in neighbors_to_color:
                    neighbor_colors[neighbor] = color[neighbor]
                    color[neighbor] = -1  # Temporarily mark as uncolored for recursive call
                
                # Recursively color the graph
                can_proceed = True
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        if not dfs(neighbor):
                            can_proceed = False
                            break
                
                if can_proceed:
                    return True
                    
                # Backtrack
                color[node] = -1
                for neighbor in neighbors_to_color:
                    color[neighbor] = neighbor_colors[neighbor]
        
        return False
    
    # Better approach: try to 3-color the graph using BFS/DFS
    def bfs_3color():
        # Try to color component by component
        visited = [False] * n
        
        for start in range(n):
            if visited[start] or color[start] != -1:
                continue
                
            # BFS coloring for this component
            queue = [start]
            visited[start] = True
            if color[start] == -1:
                color[start] = 1  # Start with color 1
            
            while queue:
                node = queue.pop(0)
                current_color = color[node]
                
                # Available colors for neighbors (must be different from current)
                available_colors = [c for c in [1, 2, 3] if c != current_color]
                
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                        
                        # Assign a color different from current node
                        if color[neighbor] == -1:
                            # Assign first available color
                            color[neighbor] = available_colors[0]
                        elif color[neighbor] == current_color:
                            # Conflict! Try to resolve
                            # This is getting complex, let's use backtracking
                            return False
                    else:
                        # Neighbor already visited
                        if color[neighbor] == current_color:
                            return False
        return True
    
    # Even simpler: full backtracking
    def backtrack(node):
        if node == n:
            return True
            
        for c in [1, 2, 3]:
            # Check if color c is valid for node
            valid = True
            for neighbor in adj[node]:
                if color[neighbor] == c:
                    valid = False
                    break
            
            if valid:
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1  # Backtrack
        
        return False
    
    # Check if graph is 3-colorable
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

solve()