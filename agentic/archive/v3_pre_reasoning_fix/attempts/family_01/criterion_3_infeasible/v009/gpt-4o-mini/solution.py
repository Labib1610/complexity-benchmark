def find_conflicting_triplet(n, m, conflicts):
    from collections import defaultdict
    
    # Build the adjacency set for quick lookups
    conflict_set = defaultdict(set)
    
    for u, v in conflicts:
        conflict_set[u].add(v)
        conflict_set[v].add(u)

    # We need to find a triple (a, b, c) such that:
    # a < b < c and (a, b), (a, c), (b, c) are all in conflicts
    for a in range(1, n + 1):
        for b in conflict_set[a]:
            if b > a:  # Ensure a < b
                for c in conflict_set[b]:
                    if c > b and c in conflict_set[a]:  # Ensure b < c and (a, c) is also in conflicts
                        return a, b, c

import sys
input = sys.stdin.read

data = input().strip().splitlines()
n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = find_conflicting_triplet(n, m, conflicts)
print(result[0], result[1], result[2])