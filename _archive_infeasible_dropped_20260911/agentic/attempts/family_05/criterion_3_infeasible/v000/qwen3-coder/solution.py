k, t = map(int, input().split())

# Set to store specialists that appear in at least one combination
used_specialists = set()

# Read all combinations
for _ in range(t):
    x, y, z = map(int, input().split())
    used_specialists.add(x)

# Find the smallest specialist not in the used set
for i in range(1, k + 1):
    if i not in used_specialists:
        print(i)
        break