def can_assign_channels(n, m, constraints):
    from itertools import product

    # Create adjacency list for the graph
    graph = [[] for _ in range(n + 1)]
    for u, v in constraints:
        graph[u].append(v)
        graph[v].append(u)

    # Try all possible assignments using product
    for assignment in product(range(1, 4), repeat=n):
        valid = True
        for u in range(1, n + 1):
            for v in graph[u]:
                if assignment[u - 1] == assignment[v - 1]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            return assignment

    return None

import sys
input = sys.stdin.read
data = input().splitlines()

# Read input
n, m = map(int, data[0].split())
constraints = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Attempt to find valid channel assignments
assignment = can_assign_channels(n, m, constraints)

if assignment is None:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, assignment)))