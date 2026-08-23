def find_triplet(n, m, edges):
    from collections import defaultdict
    
    graph = defaultdict(set)
    
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    for a in range(1, n + 1):
        neighbors = list(graph[a])
        k = len(neighbors)
        for i in range(k):
            for j in range(i + 1, k):
                b = neighbors[i]
                c = neighbors[j]
                if b in graph[c]:
                    return a, b, c

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

a, b, c = find_triplet(n, m, edges)
print(a, b, c)