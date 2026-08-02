import sys

def find_lexicographically_smallest_triplet(n, restrictions):
    # Create an adjacency list for each employee
    graph = {i: set() for i in range(1, n+1)}
    
    # Fill the adjacency list with given restrictions
    for u, v in restrictions:
        graph[u].add(v)
        graph[v].add(u)

    # Sort the employees to ensure lexicographical order when checking triples
    employees = sorted(graph.keys())

    # Check each triplet (i, j, k) where i < j < k
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                a, b, c = employees[i], employees[j], employees[k]
                if b in graph[a] and c in graph[a] and c in graph[b]:
                    return a, b, c

# Read input
input_data = sys.stdin.read().strip().split()
n, m = int(input_data[0]), int(input_data[1])
restrictions = [tuple(map(int, input_data[i:i+2])) for i in range(2, len(input_data), 2)]

# Find and print the result
result = find_lexicographically_smallest_triplet(n, restrictions)
print(" ".join(map(str, result)))