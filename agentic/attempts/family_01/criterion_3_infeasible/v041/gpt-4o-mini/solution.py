def find_conflict_triple(n, m, pairs):
    from collections import defaultdict

    conflicts = defaultdict(set)

    # Build the conflict graph
    for u, v in pairs:
        conflicts[u].add(v)
        conflicts[v].add(u)

    # Search for the lexicographically smallest triple
    for a in range(1, n + 1):
        for b in conflicts[a]:
            if b > a:  # Ensure a < b
                for c in conflicts[b]:
                    if c > b and c in conflicts[a]:  # Ensure b < c and a, c are in conflict
                        return a, b, c

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
pairs = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Find the result and print
result = find_conflict_triple(n, m, pairs)
print(*result)