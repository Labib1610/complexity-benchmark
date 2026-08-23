def find_triangle(n, m, edges):
    from collections import defaultdict
    
    # Create an adjacency list
    graph = defaultdict(set)
    
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    # Check each pair of nodes for a common neighbor
    for a in range(1, n + 1):
        for b in graph[a]:
            if b > a:  # Ensure a < b
                # Find common neighbors between a and b
                common_neighbors = graph[a].intersection(graph[b])
                for c in sorted(common_neighbors):
                    if c > b:  # Ensure b < c
                        return a, b, c

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m+1]]

# Find and print the triangle
result = find_triangle(n, m, edges)
print(*result)