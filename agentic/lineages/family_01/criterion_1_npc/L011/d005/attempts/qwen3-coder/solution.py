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
    
    # Try all possible colorings, prioritizing those with smaller W(C)
    # We'll use backtracking with pruning
    # Since we want to minimize W(C) = sum(c_i * 4^(n-i)), we should try to assign
    # smaller values to earlier indices (higher powers of 4)
    
    coloring = [0] * (n + 1)  # coloring[i] is the color of node i (1-indexed)
    
    def is_valid(node, color):
        for neighbor in adj[node]:
            if coloring[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        # Try colors in order 1, 2, 3 to minimize W(C)
        for color in [1, 2, 3]:
            if is_valid(node, color):
                coloring[node] = color
                if backtrack(node + 1):
                    return True
                coloring[node] = 0  # backtrack
                
        return False
    
    # Check if graph is 3-colorable
    if backtrack(1):
        print("YES")
        print(*coloring[1:])
    else:
        print("NO")

solve()