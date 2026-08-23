import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
    
    # Try all possible assignments
    # We'll use backtracking with constraint checking
    assignment = [0] * (n + 1)  # 1-indexed
    
    def is_valid(node, color):
        # Check if assigning 'color' to 'node' conflicts with neighbors
        for neighbor in adj[node]:
            if assignment[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        # Try colors 1, 2, 3 in order for lexicographically smallest result
        for color in [1, 2, 3]:
            if is_valid(node, color):
                assignment[node] = color
                if backtrack(node + 1):
                    return True
                assignment[node] = 0  # Backtrack
        
        return False
    
    # This approach might be too slow for larger inputs
    # Let's think of a better way - this is essentially 3-coloring problem
    
    # For optimization, let's try a different approach with better pruning
    def solve_coloring():
        # Try to build a valid 3-coloring
        colors = [0] * (n + 1)
        
        def can_color(node, color):
            for neighbor in adj[node]:
                if colors[neighbor] == color:
                    return False
            return True
        
        def dfs(node):
            if node > n:
                return True
                
            for c in [1, 2, 3]:
                if can_color(node, c):
                    colors[node] = c
                    if dfs(node + 1):
                        return True
                    colors[node] = 0
            return False
        
        if dfs(1):
            return colors[1:]
        return None
    
    result = solve_coloring()
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, result)))

solve()