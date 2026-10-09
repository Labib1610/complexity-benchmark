import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # If no edges, any assignment works
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Protocol versions and their channels
    # Version 1: X,Y
    # Version 2: Y,Z
    # Version 3: Z,X
    channels = {
        1: {"X", "Y"},
        2: {"Y", "Z"},
        3: {"Z", "X"}
    }
    
    # Function to check if two versions share exactly one channel
    def compatible(v1, v2):
        ch1 = channels[v1]
        ch2 = channels[v2]
        intersection = ch1.intersection(ch2)
        return len(intersection) == 1
    
    # Try all 3^n assignments
    assignment = [0] * n
    
    def backtrack(node):
        if node == n:
            return True
            
        for version in [1, 2, 3]:
            assignment[node] = version
            valid = True
            
            # Check compatibility with all neighbors
            for neighbor in adj[node]:
                if neighbor < node:  # Only check if neighbor is already assigned
                    if not compatible(assignment[node], assignment[neighbor]):
                        valid = False
                        break
            
            if valid and backtrack(node + 1):
                return True
                
        assignment[node] = 0
        return False
    
    # Optimization: if any node has degree > 2, we might need to be more careful
    # But let's just try backtracking first
    
    if backtrack(0):
        print("YES")
        result = [str(assignment[i]) for i in range(n)]
        print(" ".join(result))
    else:
        print("NO")

solve()