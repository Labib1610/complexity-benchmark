def find_conflicting_triplet(n, m, conflicts):
    from collections import defaultdict
    
    # Create a graph where edges represent conflicts
    graph = defaultdict(set)
    for u, v in conflicts:
        graph[u].add(v)
        graph[v].add(u)

    # Check each pair of workers for the third mutual conflict
    for a in range(1, n + 1):
        neighbors = list(graph[a])
        k = len(neighbors)

        # Check pairs of neighbors to find a third worker
        for i in range(k):
            for j in range(i + 1, k):
                b = neighbors[i]
                c = neighbors[j]
                if b in graph[c]:  # Check if b and c also conflict
                    return (a, min(b, c), max(b, c))

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = find_conflicting_triplet(n, m, conflicts)
print(*result)