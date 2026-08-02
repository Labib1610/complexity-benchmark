from itertools import product

# Reading inputs
n, m = map(int, input().split())
incompatibilities = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    incompatibilities[u].add(v)
    incompatibilities[v].add(u)

# Check each combination of bands
for bands in product(range(3), repeat=n):
    valid = True
    for i in range(n):
        for j in incompatibilities[i]:
            if bands[i] == bands[j]:  # If two incompatible streams are on the same band, it's invalid.
                valid = False
                break
        if not valid:
            break
    
    if valid:
        print("YES")
        print(*[band + 1 for band in bands])  # Output bands incremented by 1 to match the problem statement (1-indexed)
        exit()

print("NO")