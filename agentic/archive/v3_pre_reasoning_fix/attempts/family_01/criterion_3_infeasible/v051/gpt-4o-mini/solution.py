def find_conflict_triad(n, m, edges):
    from collections import defaultdict
    
    # Adjacency list for conflicts
    conflicts = defaultdict(set)
    
    # Populate the adjacency list
    for u, v in edges:
        conflicts[u].add(v)
        conflicts[v].add(u)

    # Find the lexicographically smallest triple
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if b in conflicts[a]:  # Check if (a, b) is a conflict
                for c in range(b + 1, n + 1):
                    if c in conflicts[a] and c in conflicts[b]:  # Check (a, c) and (b, c)
                        return a, b, c

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = find_conflict_triad(n, m, edges)
print(*result)