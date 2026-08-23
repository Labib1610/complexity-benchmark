import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
incompatibilities = defaultdict(set)

for i in range(1, m + 1):
    u, v = map(int, data[i].split())
    incompatibilities[u].add(v)
    incompatibilities[v].add(u)

for a in range(1, n + 1):
    for b in incompatibilities[a]:
        if b > a:
            for c in incompatibilities[b]:
                if c > b and c in incompatibilities[a]:
                    print(a, b, c)
                    sys.exit()