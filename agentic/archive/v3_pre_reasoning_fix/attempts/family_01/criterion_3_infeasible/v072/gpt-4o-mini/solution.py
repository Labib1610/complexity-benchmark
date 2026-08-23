def find_triangle(n, edges):
    from collections import defaultdict
    
    graph = defaultdict(set)
    
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    # Iterate through each pair of nodes
    for a in range(1, n + 1):
        for b in graph[a]:
            if b <= a:
                continue  # Ensure a < b
            for c in graph[a]:
                if c <= b or c == b:
                    continue  # Ensure b < c
                if c in graph[b]:  # Check if b and c are connected
                    return (a, b, c)

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = find_triangle(n, edges)
print(result[0], result[1], result[2])