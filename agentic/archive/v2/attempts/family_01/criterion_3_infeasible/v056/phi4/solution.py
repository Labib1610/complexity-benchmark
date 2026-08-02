import sys

# Read the number of employees and conflict rules
n, m = map(int, sys.stdin.readline().split())

# Initialize a dictionary to store conflicts for each employee
conflicts = {i: set() for i in range(1, n + 1)}

# Read the conflict pairs and populate the conflicts dictionary
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    if u > v:
        u, v = v, u
    conflicts[u].add(v)

# Find the lexicographically smallest triplet (a, b, c)
found = False
for a in sorted(conflicts.keys()):
    for b in sorted(conflicts[a]):
        if found: break
        for c in sorted(conflicts[a] & conflicts[b]):
            print(a, b, c)
            found = True
            break