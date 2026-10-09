from itertools import combinations

n, m, k = map(int, input().split())

# Read interference pairs
interference = set()
for _ in range(m):
    u, v = map(int, input().split())
    interference.add((min(u, v), max(u, v)))

# Generate all possible combinations of k markers
markers = list(range(1, n + 1))

# Check each combination
for combo in combinations(markers, k):
    # Check if this combination is stable
    stable = True
    for i in range(k):
        for j in range(i + 1, k):
            u, v = combo[i], combo[j]
            if (min(u, v), max(u, v)) in interference:
                stable = False
                break
        if not stable:
            break
    
    if stable:
        print("YES")
        print(" ".join(map(str, combo)))
        exit()

print("NO")