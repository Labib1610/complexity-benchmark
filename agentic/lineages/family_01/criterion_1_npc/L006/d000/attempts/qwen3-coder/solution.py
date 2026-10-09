import sys
from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Try all possible colorings using backtracking
    def is_valid_coloring(coloring):
        for u, v in edges:
            if coloring[u] == coloring[v]:
                return False
        return True
    
    # Simple greedy approach with backtracking
    coloring = [0] * (n + 1)  # 1-indexed
    
    def backtrack(worker):
        if worker > n:
            return True
            
        for color in [1, 2, 3]:
            coloring[worker] = color
            valid = True
            # Check if this color conflicts with any neighbor
            for neighbor in adj[worker]:
                if neighbor < worker and coloring[neighbor] == color:
                    valid = False
                    break
            
            if valid and backtrack(worker + 1):
                return True
        
        coloring[worker] = 0
        return False
    
    if backtrack(1):
        print("YES")
        print(" ".join(map(str, coloring[1:])))
    else:
        print("NO")

solve()