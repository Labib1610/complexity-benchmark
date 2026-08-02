def allocate_shifts(n, m, incompatibilities):
    from itertools import product

    # Create a graph for incompatibilities
    graph = [[] for _ in range(n + 1)]
    for u, v in incompatibilities:
        graph[u].append(v)
        graph[v].append(u)

    # Try all combinations of shifts for personnel
    for shifts in product(range(1, 4), repeat=n):
        valid = True
        for u in range(1, n + 1):
            for v in graph[u]:
                if shifts[u - 1] == shifts[v - 1]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            print("YES")
            print(" ".join(map(str, shifts)))
            return

    print("NO")

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
incompatibilities = [tuple(map(int, line.split())) for line in data[1:m + 1]]
allocate_shifts(n, m, incompatibilities)