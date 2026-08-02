import sys
from itertools import product

# Read n and m
n, m = map(int, input().split())

# Create adjacency list for conflicts
adj_list = {i: set() for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].add(v)
    adj_list[v].add(u)

# Try to assign modes lexicographically smallest valid way
def is_valid_assignment(assignment):
    for i in range(1, n + 1):
        mode_i = assignment[i - 1]
        for j in adj_list[i]:
            if assignment[j - 1] == mode_i:
                return False
    return True

# Try all permutations of modes starting from the smallest lexicographical order
modes = [1, 2, 3]
for perm in sorted(product(modes, repeat=n)):
    # Check if this permutation is valid
    if is_valid_assignment(perm):
        print("YES")
        print(*perm)
        sys.exit()

print("NO")