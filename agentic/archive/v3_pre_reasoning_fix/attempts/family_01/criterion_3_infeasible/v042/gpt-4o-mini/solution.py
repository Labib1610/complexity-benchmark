def find_triplet(n, m, incompatible_pairs):
    from collections import defaultdict
    
    incompatible = defaultdict(set)
    
    # Fill the incompatible pairs in a set for fast lookup
    for u, v in incompatible_pairs:
        incompatible[u].add(v)
        incompatible[v].add(u)
    
    # Check for each combination of three reagents
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if b in incompatible[a]:  # a and b must be incompatible
                for c in range(b + 1, n + 1):
                    if c in incompatible[a] and c in incompatible[b]:  # a and c, b and c must also be incompatible
                        return (a, b, c)

import sys
input = sys.stdin.read

data = input().splitlines()
n, m = map(int, data[0].split())
incompatible_pairs = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = find_triplet(n, m, incompatible_pairs)
print(result[0], result[1], result[2])