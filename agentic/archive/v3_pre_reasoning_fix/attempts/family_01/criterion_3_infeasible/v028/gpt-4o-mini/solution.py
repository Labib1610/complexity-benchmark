def find_lexicographically_smallest_cluster(n, m, edges):
    from collections import defaultdict

    # Build the adjacency list
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # Iterate through all pairs of nodes to find triangles
    result = None
    for u in range(1, n + 1):
        neighbors = list(graph[u])
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                v = neighbors[i]
                w = neighbors[j]
                # Check if v and w are connected
                if w in graph[v]:
                    # Found a triangle (u, v, w)
                    triangle = tuple(sorted((u, v, w)))
                    if result is None or triangle < result:
                        result = triangle

    return result

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

a, b, c = find_lexicographically_smallest_cluster(n, m, edges)
print(a, b, c)