def can_assign(n, m, restrictions):
    from itertools import product
    
    # Create a conflict graph
    graph = [[] for _ in range(n)]
    for u, v in restrictions:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Check all possible assignments (1, 2, 3) for each personnel
    for assignment in product(range(1, 4), repeat=n):
        valid = True
        for u in range(n):
            for v in graph[u]:
                if assignment[u] == assignment[v]:
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

n, m = map(int, data[0].split())
restrictions = [tuple(map(int, line.split())) for line in data[1:m + 1]]

assignment = can_assign(n, m, restrictions)

if assignment is None:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, assignment)))