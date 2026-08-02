def find_committee(n, m, relationships):
    from collections import defaultdict
    
    # Create an adjacency list for co-authorships
    graph = defaultdict(set)
    
    for u, v in relationships:
        graph[u].add(v)
        graph[v].add(u)
    
    # Iterate through every expert and look for a committee of three
    for a in range(1, n + 1):
        for b in graph[a]:
            if b > a:  # Ensure a < b
                for c in graph[b]:
                    if c > b and c in graph[a]:  # Ensure b < c and (a, c) exists
                        return a, b, c

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
relationships = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = find_committee(n, m, relationships)
print(result[0], result[1], result[2])