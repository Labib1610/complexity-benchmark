def find_incompatible_triplet(n, m, pairs):
    incompatibles = [set() for _ in range(n + 1)]
    
    for u, v in pairs:
        incompatibles[u].add(v)
        incompatibles[v].add(u)
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if b in incompatibles[a]:
                for c in range(b + 1, n + 1):
                    if c in incompatibles[a] and c in incompatibles[b]:
                        return a, b, c

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
pairs = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = find_incompatible_triplet(n, m, pairs)
print(*result)