def schedule_partitioning(n, m, incompatible_pairs):
    from itertools import product

    # Create a compatibility list
    incompatible = [set() for _ in range(n)]
    for u, v in incompatible_pairs:
        incompatible[u - 1].add(v - 1)
        incompatible[v - 1].add(u - 1)

    # Try all combinations of assignments
    for assignment in product(range(1, 4), repeat=n):
        valid = True
        for i in range(n):
            for j in incompatible[i]:
                if assignment[i] == assignment[j]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            return "YES", assignment
    
    return "NO", []

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
incompatible_pairs = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Get the result
result = schedule_partitioning(n, m, incompatible_pairs)

# Print output
if result[0] == "NO":
    print(result[0])
else:
    print(result[0])
    print(" ".join(map(str, result[1])))