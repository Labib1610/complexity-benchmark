def can_partition(n, m, incompatible_pairs):
    from itertools import product

    # Create a graph representation for the incompatible pairs
    graph = [[] for _ in range(n + 1)]
    for u, v in incompatible_pairs:
        graph[u].append(v)
        graph[v].append(u)

    # Check all possible assignments of personnel to windows (1, 2, or 3)
    for assignment in product(range(1, 4), repeat=n):
        valid = True
        for u in range(1, n + 1):
            for v in graph[u]:
                if assignment[u - 1] == assignment[v - 1]:  # Check if they share the same window
                    valid = False
                    break
            if not valid:
                break

        if valid:
            return "YES", assignment

    return "NO",

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
incompatible_pairs = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = can_partition(n, m, incompatible_pairs)

if result[0] == "NO":
    print(result[0])
else:
    print(result[0])
    print(' '.join(map(str, result[1])))