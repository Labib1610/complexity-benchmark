def find_fault_group(n, m, pairs):
    from collections import defaultdict

    # Create an adjacency list for the interference graph
    graph = defaultdict(set)
    
    for u, v in pairs:
        graph[u].add(v)
        graph[v].add(u)

    # Iterate through all possible pairs and check for triangles
    for a in range(1, n + 1):
        neighbors = sorted(graph[a])  # Sort neighbors to ensure lexicographical order
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                b = neighbors[i]
                c = neighbors[j]
                if b in graph[c]:  # Check if b and c are connected
                    return a, b, c  # Found a triangle

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
pairs = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Finding and printing the fault group
result = find_fault_group(n, m, pairs)
print(result[0], result[1], result[2])