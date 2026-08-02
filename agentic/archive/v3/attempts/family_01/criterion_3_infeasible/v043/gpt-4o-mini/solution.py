from sys import stdin, stdout
from itertools import combinations

input = stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Using a set for quick lookup
interference = [set() for _ in range(n + 1)]
for u, v in edges:
    interference[u].add(v)
    interference[v].add(u)

# Find the lexicographically smallest triple (a, b, c)
result = None

for a in range(1, n + 1):
    for b in interference[a]:
        if b > a:  # Ensure a < b
            for c in interference[b]:
                if c > b and c in interference[a]:  # Ensure b < c and a < c, and (a, c) exists
                    candidate = (a, b, c)
                    if result is None or candidate < result:
                        result = candidate

stdout.write(f"{result[0]} {result[1]} {result[2]}\n")