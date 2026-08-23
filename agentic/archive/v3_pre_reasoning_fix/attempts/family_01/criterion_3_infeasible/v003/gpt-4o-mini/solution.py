def find_mutual_interference(n, m, edges):
    from collections import defaultdict
    
    graph = defaultdict(set)
    
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    for a in range(1, n + 1):
        for b in graph[a]:
            if b > a:  # Ensure a < b
                for c in graph[b]:
                    if c > b and c in graph[a]:  # Ensure b < c and a, b, c mutually interfere
                        return a, b, c

import sys
input = sys.stdin.read
data = input().splitlines()

first_line = data[0].split()
n = int(first_line[0])
m = int(first_line[1])

edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]
result = find_mutual_interference(n, m, edges)

print(*result)