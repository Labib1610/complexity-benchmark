def can_assign_shifts(n, m, conflicts):
    from itertools import product

    # Build the adjacency matrix for conflicts
    conflict_matrix = [[False] * n for _ in range(n)]
    for u, v in conflicts:
        conflict_matrix[u - 1][v - 1] = True
        conflict_matrix[v - 1][u - 1] = True

    # Try all possible combinations of shifts (1, 2, 3)
    for shifts in product(range(1, 4), repeat=n):
        valid = True
        for i in range(n):
            for j in range(i + 1, n):
                if conflict_matrix[i][j] and shifts[i] == shifts[j]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            return shifts

    return None

import sys
input = sys.stdin.read
data = input().strip().splitlines()

n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = can_assign_shifts(n, m, conflicts)
if result is None:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, result)))