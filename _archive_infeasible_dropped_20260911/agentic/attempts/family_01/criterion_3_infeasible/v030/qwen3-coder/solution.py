import sys
from collections import defaultdict

def find_lexicographically_smallest_triangle(n, edges):
    # Create adjacency list using sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # For each node, get its neighbors
    neighbors = [list(adj[i]) for i in range(n + 1)]
    # Sort neighbors for consistent processing
    for i in range(1, n + 1):
        neighbors[i].sort()
    
    # Check each edge to see if it forms a triangle with any common neighbor
    best_triangle = None
    
    # Process edges in a way that ensures we find the lexicographically smallest triangle
    for a in range(1, n + 1):
        for b in neighbors[a]:
            if b <= a:  # Ensure we don't double count and maintain order
                continue
            # Look for a node c that connects to both a and b
            for c in neighbors[a]:
                if c <= b:  # Maintain a < b < c order
                    continue
                if c in adj[b]:  # Found a triangle
                    triangle = (a, b, c)
                    if best_triangle is None or triangle < best_triangle:
                        best_triangle = triangle
    
    return best_triangle

# Read input
input_data = sys.stdin.read().split()
n, m = int(input_data[0]), int(input_data[1])
edges = []
index = 2
for _ in range(m):
    u, v = int(input_data[index]), int(input_data[index + 1])
    edges.append((u, v))
    index += 2

# Find and print the result
result = find_lexicographically_smallest_triangle(n, edges)
print(result[0], result[1], result[2])