def find_bottleneck(n, m, conflicts):
    from collections import defaultdict
    
    conflict_graph = defaultdict(set)
    
    for u, v in conflicts:
        conflict_graph[u].add(v)
        conflict_graph[v].add(u)
    
    for a in range(1, n + 1):
        for b in conflict_graph[a]:
            if b > a:  # Ensure a < b
                for c in conflict_graph[b]:
                    if c > b and c in conflict_graph[a]:  # Ensure b < c and (a, c) conflict
                        return a, b, c

import sys
input = sys.stdin.read

data = input().strip().split('\n')
n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m + 1]]

a, b, c = find_bottleneck(n, m, conflicts)
print(a, b, c)