def find_mutual_crosstalk_triplet(n, m, edges):
    from collections import defaultdict

    adjacency_list = defaultdict(set)

    # Build the adjacency list for crosstalk relationships
    for u, v in edges:
        adjacency_list[u].add(v)
        adjacency_list[v].add(u)

    # Sort keys to ensure lexicographical order
    transmitters = sorted(adjacency_list.keys())

    # Look for triplets
    for a in transmitters:
        neighbors = sorted(adjacency_list[a])
        neighbor_count = len(neighbors)
        for i in range(neighbor_count):
            b = neighbors[i]
            for j in range(i + 1, neighbor_count):
                c = neighbors[j]
                if c in adjacency_list[b]:
                    return a, b, c

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = find_mutual_crosstalk_triplet(n, m, edges)
print(*result)