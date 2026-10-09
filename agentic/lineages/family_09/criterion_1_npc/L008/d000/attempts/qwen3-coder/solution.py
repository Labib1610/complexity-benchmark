from itertools import combinations

n, m, k = map(int, input().split())
anomalies = set()
for _ in range(m):
    u, v = map(int, input().split())
    anomalies.add((min(u, v), max(u, v)))

# Generate all possible combinations of k modules
modules = list(range(1, n + 1))

# Check each combination
for combo in combinations(modules, k):
    # Check if this combination has any anomalies
    valid = True
    for u, v in combinations(combo, 2):
        if (u, v) in anomalies:
            valid = False
            break
    
    if valid:
        print("YES")
        print(*combo)
        exit()

print("NO")