import sys
from itertools import combinations

def find_bottleneck(n, m, edges):
    # Create adjacency list representation
    adj = [set() for _ in range(n + 1)]
    edge_set = set()
    
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
        edge_set.add((min(u, v), max(u, v)))
    
    # Check all combinations of 3 nodes
    for combo in combinations(range(1, n + 1), 3):
        a, b, c = sorted(combo)
        
        # Check if all three pairs are connected (form a triangle)
        if (a, b) in edge_set and (a, c) in edge_set and (b, c) in edge_set:
            return [a, b, c]
        
        # If not a triangle, check all 8 assignments
        found_valid = False
        for mask in range(8):
            # Assign each node to line 0 or 1 based on bits in mask
            assignment = [(mask >> i) & 1 for i in range(3)]
            
            # Check if this assignment causes any collisions
            valid = True
            for i in range(3):
                for j in range(i + 1, 3):
                    # If nodes i and j are connected and on same line
                    if (combo[i], combo[j]) in edge_set and assignment[i] == assignment[j]:
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                found_valid = True
                break
        
        if not found_valid:
            return [a, b, c]
    
    return None

# Read input
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

# Find and output the bottleneck
result = find_bottleneck(n, m, edges)
print(' '.join(map(str, result)))