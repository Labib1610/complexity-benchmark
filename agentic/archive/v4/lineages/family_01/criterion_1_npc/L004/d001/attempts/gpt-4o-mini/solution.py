def assign_channels(n, m, incompatibilities):
    from itertools import product

    # Create an adjacency list for the incompatibilities
    graph = [[] for _ in range(n)]
    for u, v in incompatibilities:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Try all possible assignments using a lexicographical order
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
            print("YES")
            print(" ".join(map(str, assignment)))
            return

    print("NO")

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
incompatibilities = [tuple(map(int, line.split())) for line in data[1:m + 1]]

assign_channels(n, m, incompatibilities)