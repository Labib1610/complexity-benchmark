def find_incompatible_triplet(n, m, pairs):
    from collections import defaultdict
    
    incompatibility_graph = defaultdict(set)
    
    for u, v in pairs:
        incompatibility_graph[u].add(v)
        incompatibility_graph[v].add(u)
    
    for a in range(1, n + 1):
        for b in incompatibility_graph[a]:
            for c in incompatibility_graph[b]:
                if c > b and c in incompatibility_graph[a]:
                    return a, b, c

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
pairs = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = find_incompatible_triplet(n, m, pairs)
print(" ".join(map(str, result)))