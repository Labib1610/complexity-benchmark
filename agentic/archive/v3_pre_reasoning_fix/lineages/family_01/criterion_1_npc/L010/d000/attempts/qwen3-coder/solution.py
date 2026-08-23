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
        for color in range(1, 4):
            if is_valid(node, color):
                assignment[node] = color
                if backtrack(node + 1):
                    return True
                assignment[node] = 0  # Backtrack
        
        return False
    
    # This approach might be too slow for n=40
    # Let's think differently - this is a graph coloring problem
    # But we need to be smart about it
    
    # Since we want lexicographically smallest, we can try assigning
    # colors greedily in order, but we need to check if it's possible
    
    # Actually, let's just implement the backtracking solution
    # For n=40 and 3 colors, it might work if the graph is sparse
    
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, assignment[1:])))
    else:
        print("NO")

# The above approach may time out for larger inputs
# Let's optimize by using a more systematic approach

def solve_optimized():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color assignment (0 means unassigned)
    color = [0] * (n + 1)
    
    # Check if we can color the graph with 3 colors
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def graph_coloring(node):
        if node > n:
            return True
            
        # Try colors in order 1, 2, 3 for lex smallest result
        for c in range(1, 4):
            if is_safe(node, c):
                color[node] = c
                if graph_coloring(node + 1):
                    return True
                color[node] = 0
                
        return False
    
    if graph_coloring(1):
        print("YES")
        print(' '.join(map(str, color[1:])))
    else:
        print("NO")

solve_optimized()