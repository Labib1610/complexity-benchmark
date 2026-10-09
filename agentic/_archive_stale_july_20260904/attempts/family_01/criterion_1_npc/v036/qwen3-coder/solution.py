import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list for conflicts
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all possible assignments in lexicographical order
    assignment = [0] * (n + 1)  # 1-indexed
    
    def is_valid(vehicle, block):
        for neighbor in adj[vehicle]:
            if assignment[neighbor] == block:
                return False
        return True
    
    def backtrack(vehicle):
        if vehicle > n:
            return True
            
        for block in [1, 2, 3]:
            if is_valid(vehicle, block):
                assignment[vehicle] = block
                if backtrack(vehicle + 1):
                    return True
                assignment[vehicle] = 0
        
        return False
    
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, assignment[1:])))
    else:
        print("NO")

solve()