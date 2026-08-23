import sys
from itertools import product

input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
incompatibilities = [tuple(map(int, line.split())) for line in data[1:m+1]]

# Create adjacency matrix for incompatibility constraints
incompat_matrix = [[False] * n for _ in range(n)]
for u, v in incompatibilities:
    incompat_matrix[u-1][v-1] = True
    incompat_matrix[v-1][u-1] = True

# Check if the assignment is valid
def is_valid_assignment(assignment):
    for u, v in incompatibilities:
        if assignment[u-1] * assignment[v-1] not in {2, 3, 6}:
            return False
    return True

# Generate all possible assignments
for assignment in product(range(1, 4), repeat=n):
    if is_valid_assignment(assignment):
        print("YES")
        print(" ".join(map(str, assignment)))
        break
else:
    print("NO")