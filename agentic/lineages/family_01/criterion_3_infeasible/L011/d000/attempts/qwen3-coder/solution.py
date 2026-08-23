import sys
from itertools import combinations

def find_unresolvable_trio(n, m, edges):
    # Build adjacency list
    adj = [set() for _ in range(n + 1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate through all combinations of 3 nodes in sorted order
    for a, b, c in combinations(range(1, n + 1), 3):
        # Check if all three pairs are connected (form a triangle)
        if b in adj[a] and c in adj[a] and c in adj[b]:
            return a, b, c
    
    # This shouldn't happen according to problem statement
    return None

# Read input
input_lines = sys.stdin.read().splitlines()
n, m = map(int, input_lines[0].split())
edges = [tuple(map(int, line.split())) for line in input_lines[1:]]

# Find and print the result
result = find_unresolvable_trio(n, m, edges)
print(result[0], result[1], result[2])