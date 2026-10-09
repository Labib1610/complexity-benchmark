import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Create adjacency list for incompatibilities
    adj = defaultdict(set)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].add(v)
        adj[v].add(u)
    
    # Try all possible assignments
    # For each animal, we try assigning it to enclosure 1, 2, or 3
    # But we can do this more efficiently by using graph coloring
    
    # This is essentially a 3-coloring problem
    # We'll use backtracking
    
    colors = [0] * n  # 0 means unassigned, 1, 2, 3 are the enclosures
    
    def is_valid(node, color):
        # Check if assigning 'color' to 'node' conflicts with neighbors
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        if colors[node] != 0:  # Already assigned
            return backtrack(node + 1)
            
        for color in range(1, 4):  # Try colors 1, 2, 3
            if is_valid(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0  # Backtrack
                
        return False
    
    # Special case: if there are no edges, any assignment works
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Try to find a valid 3-coloring
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

solve()