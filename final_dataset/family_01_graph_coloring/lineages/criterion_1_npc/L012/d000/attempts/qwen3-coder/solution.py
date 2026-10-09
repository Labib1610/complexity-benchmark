import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].add(v)
        adj[v].add(u)
    
    # Try all 3-colorings using backtracking
    color = [-1] * n  # -1 means uncolored
    
    def is_safe(node, c):
        # Check if assigning color c to node is safe
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        for c in range(3):  # Try colors 0, 1, 2
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1  # Backtrack
                
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(str(c + 1) for c in color))  # Convert back to 1-indexed
    else:
        print("NO")

solve()