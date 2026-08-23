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
    
    # Try all possible colorings (1, 2, 3) for each node
    # We want the lexicographically smallest valid coloring
    
    # Use backtracking with constraint checking
    coloring = [0] * (n + 1)  # coloring[i] represents the color of node i
    
    def is_valid(node, color):
        # Check if assigning 'color' to 'node' conflicts with neighbors
        for neighbor in adj[node]:
            if coloring[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for color in [1, 2, 3]:
            if is_valid(node, color):
                coloring[node] = color
                if backtrack(node + 1):
                    return True
                coloring[node] = 0  # backtrack
                
        return False
    
    # This approach is too slow for larger inputs
    # Let's use a more efficient graph coloring algorithm
    
    # For triangle-free graphs, we can use a greedy approach
    # But we need to ensure lexicographically smallest result
    
    # Better approach: for each node in order 1..n, try colors 1,2,3 in order
    # and pick the first valid one
    
    for i in range(1, n + 1):
        found_color = False
        for color in [1, 2, 3]:
            valid = True
            for neighbor in adj[i]:
                if neighbor < i and coloring[neighbor] == color:
                    valid = False
                    break
            if valid:
                coloring[i] = color
                found_color = True
                break
        if not found_color:
            print("NO")
            return
    
    # Now verify the solution
    valid = True
    for i in range(1, n + 1):
        for neighbor in adj[i]:
            if coloring[i] == coloring[neighbor]:
                valid = False
                break
        if not valid:
            break
            
    if valid:
        print("YES")
        print(' '.join(map(str, coloring[1:])))
    else:
        print("NO")

solve()