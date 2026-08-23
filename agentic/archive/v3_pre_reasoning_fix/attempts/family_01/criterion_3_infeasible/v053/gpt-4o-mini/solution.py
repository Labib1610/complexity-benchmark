def find_incompatible_triplet(n, m, incompatibilities):
    incompatible_set = [set() for _ in range(n + 1)]
    
    for u, v in incompatibilities:
        incompatible_set[u].add(v)
        incompatible_set[v].add(u)
        
    for a in range(1, n + 1):
        for b in incompatible_set[a]:
            if b > a:  # Ensure b > a
                for c in incompatible_set[b]:
                    if c > b and c in incompatible_set[a]:  # Ensure c > b and a, b, c are incompatible
                        return a, b, c

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
incompatibilities = [tuple(map(int, line.split())) for line in data[1:m + 1]]
result = find_incompatible_triplet(n, m, incompatibilities)
print(*result)