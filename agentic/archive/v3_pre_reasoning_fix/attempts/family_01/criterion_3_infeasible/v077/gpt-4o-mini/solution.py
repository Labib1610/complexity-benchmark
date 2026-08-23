def find_conflicting_triplet(n, m, pairs):
    incompatibility = [set() for _ in range(n + 1)]
    
    for u, v in pairs:
        incompatibility[u].add(v)
        incompatibility[v].add(u)

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if b in incompatibility[a]:
                for c in range(b + 1, n + 1):
                    if c in incompatibility[a] and c in incompatibility[b]:
                        return a, b, c

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
pairs = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Find and print the result
result = find_conflicting_triplet(n, m, pairs)
print(*result)