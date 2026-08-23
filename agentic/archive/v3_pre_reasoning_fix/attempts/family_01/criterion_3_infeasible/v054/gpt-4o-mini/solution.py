import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
interference = defaultdict(set)

for i in range(1, m + 1):
    u, v = map(int, data[i].split())
    interference[u].add(v)
    interference[v].add(u)

for a in range(1, n + 1):
    for b in interference[a]:
        if b > a:  # Ensure a < b
            for c in interference[b]:
                if c > b and c in interference[a]:  # Ensure b < c and a < c
                    print(a, b, c)
                    sys.exit()