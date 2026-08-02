def find_conflicting_triplet(n, m, conflicts):
    from collections import defaultdict
    
    # Create an adjacency list for conflicts
    conflict_graph = defaultdict(set)
    
    for u, v in conflicts:
        conflict_graph[u].add(v)
        conflict_graph[v].add(u)
    
    # We need to find a triplet (a, b, c) such that all pairs are in conflict
    for a in range(1, n + 1):
        # Check all pairs of conflicts with a
        for b in conflict_graph[a]:
            if b > a:  # Ensure b > a for lexicographical order
                for c in conflict_graph[b]:
                    if c > b and c in conflict_graph[a]:  # Ensure c > b and a-c conflict
                        return a, b, c
    
    return None

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m+1]]

result = find_conflicting_triplet(n, m, conflicts)
print(result[0], result[1], result[2])