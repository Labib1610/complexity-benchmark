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
    
    # Try all possible assignments (3^n possibilities)
    # But we can do better with backtracking
    assignment = [0] * (n + 1)  # 1-indexed
    
    def is_valid(person, rotation):
        # Check if assigning 'person' to 'rotation' conflicts with existing assignments
        for incompatible_person in incompatible[person]:
            if assignment[incompatible_person] == rotation:
                return False
        return True
    
    def backtrack(person):
        if person > n:
            return True
            
        for rotation in [1, 2, 3]:
            if is_valid(person, rotation):
                assignment[person] = rotation
                if backtrack(person + 1):
                    return True
                assignment[person] = 0  # backtrack
        
        return False
    
    if backtrack(1):
        print("YES")
        print(*assignment[1:])
    else:
        print("NO")

solve()