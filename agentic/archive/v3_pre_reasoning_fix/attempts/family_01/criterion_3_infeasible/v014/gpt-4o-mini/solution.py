def find_triplet(n, m, restrictions):
    from collections import defaultdict
    
    # Create a set to store incompatible pairs
    incompatible = defaultdict(set)
    
    for u, v in restrictions:
        incompatible[u].add(v)
        incompatible[v].add(u)
    
    # Check for triplets
    for a in range(1, n + 1):
        for b in incompatible[a]:
            for c in incompatible[b]:
                if c != a and c in incompatible[a]:
                    return (a, b, c)
    
    return None

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
restrictions = [tuple(map(int, line.split())) for line in data[1:m + 1]]

triplet = find_triplet(n, m, restrictions)
if triplet:
    print(*sorted(triplet))