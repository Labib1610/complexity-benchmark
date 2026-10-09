import sys
from itertools import combinations

def solve():
    n, m = map(int, input().split())
    
    # Create adjacency list for incompatibilities
    incompatible = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        incompatible[u].append(v)
        incompatible[v].append(u)
    
    # Try all possible assignments
    # For each technician, try colors 1, 2, 3
    assignment = [0] * (n + 1)  # 1-indexed
    
    def is_valid(tech, color):
        # Check if assigning 'color' to 'tech' conflicts with neighbors
        for neighbor in incompatible[tech]:
            if assignment[neighbor] == color:
                return False
        return True
    
    def backtrack(tech):
        if tech > n:
            return True
            
        for color in [1, 2, 3]:
            if is_valid(tech, color):
                assignment[tech] = color
                if backtrack(tech + 1):
                    return True
                assignment[tech] = 0
        
        return False
    
    if backtrack(1):
        print("YES")
        print(*assignment[1:])
    else:
        print("NO")

solve()