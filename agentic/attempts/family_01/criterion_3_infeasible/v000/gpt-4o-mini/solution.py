import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
conflicts = defaultdict(set)

for i in range(1, m + 1):
    u, v = map(int, data[i].split())
    conflicts[u].add(v)
    conflicts[v].add(u)

# Search for a triangle in the conflict graph
for a in range(1, n + 1):
    for b in conflicts[a]:
        if b > a:  # Ensure a < b to avoid duplicates
            for c in conflicts[b]:
                if c > b and c in conflicts[a]:  # Ensure b < c and a conflict with both
                    print(a, b, c)
                    sys.exit()