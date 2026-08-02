import sys

def find_mutually_interfering_triple(n, m, pairs):
    # Create a graph using adjacency lists
    graph = [[] for _ in range(n + 1)]
    for u, v in pairs:
        if u < v:  # Ensure the smaller node is first to maintain order
            graph[u].append(v)
        else:
            graph[v].append(u)

    # Sort the adjacency lists to help find lexicographically smallest triplets
    for neighbors in graph:
        neighbors.sort()

    # Iterate over each possible starting node 'a'
    for a in range(1, n + 1):
        for b in graph[a]:
            if b > a:  # Ensure b > a
                # Check for mutual interference between a and c, and b and c
                common_neighbors = set(graph[a]) & set(graph[b])
                for c in sorted(common_neighbors):
                    if c > b:
                        return (a, b, c)

# Read input from standard input
input_data = sys.stdin.read().split()
n = int(input_data[0])
m = int(input_data[1])

pairs = []
index = 2
for _ in range(m):
    u = int(input_data[index])
    v = int(input_data[index + 1])
    pairs.append((u, v))
    index += 2

# Find and print the result
result = find_mutually_interfering_triple(n, m, pairs)
print(" ".join(map(str, result)))