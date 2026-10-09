import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all possible colorings with backtracking
    # We want the lexicographically smallest one
    colors = [0] * (n + 1)  # colors[i] represents the color of relay i
    
    def is_valid(node, color):
        # Check if assigning 'color' to 'node' conflicts with neighbors
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for color in [1, 2, 3]:
            if is_valid(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0  # Backtrack
        return False
    
    if backtrack(1):
        print("YES")
        print(*colors[1:])
    else:
        print("NO")

solve()