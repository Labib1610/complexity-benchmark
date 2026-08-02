def can_color_graph(n, edges):
    from itertools import product

    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    for colors in product(range(1, 4), repeat=n):
        valid = True
        for u in range(n):
            for v in graph[u]:
                if colors[u] == colors[v]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            return colors
    return None

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = can_color_graph(n, edges)
if result is None:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, result)))