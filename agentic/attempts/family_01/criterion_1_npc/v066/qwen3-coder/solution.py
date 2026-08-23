import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Color assignment: -1 means unassigned, 1, 2, 3 are the colors
    color = [-1] * n
    
    # Try to assign colors to each component
    for start in range(n):
        if color[start] != -1:
            continue
            
        # BFS to check if this component is 3-colorable
        queue = [start]
        # Try assigning color 1 to the starting node
        color[start] = 1
        
        while queue:
            node = queue.pop(0)
            current_color = color[node]
            
            # Check all neighbors
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    # Assign the smallest available color (1, 2, or 3)
                    # that's different from current node's color
                    used_colors = set()
                    for n_neighbor in adj[neighbor]:
                        if color[n_neighbor] != -1:
                            used_colors.add(color[n_neighbor])
                    
                    # Find the smallest available color for the neighbor
                    found_color = False
                    for c in [1, 2, 3]:
                        if c not in used_colors and c != current_color:
                            color[neighbor] = c
                            queue.append(neighbor)
                            found_color = True
                            break
                    
                    if not found_color:
                        print("NO")
                        return
                elif color[neighbor] == current_color:
                    # Conflict: adjacent nodes have the same color
                    print("NO")
                    return
    
    # Verify the coloring is valid
    for i in range(n):
        for j in adj[i]:
            if color[i] == color[j]:
                print("NO")
                return
    
    # Output the result
    print("YES")
    print(' '.join(str(c) for c in color))

# More careful implementation using backtracking for lex smallest
def solve_correct():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Color assignment: 0 means unassigned, 1, 2, 3 are the colors
    color = [0] * n
    
    # Function to check if we can color node with c
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    # Backtracking function
    def backtrack(node):
        if node == n:
            return True
            
        for c in [1, 2, 3]:
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0  # Backtrack
                
        return False
    
    if not backtrack(0):
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, color)))

solve_correct()