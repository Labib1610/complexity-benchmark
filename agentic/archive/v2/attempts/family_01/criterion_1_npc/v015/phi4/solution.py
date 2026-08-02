import sys
from itertools import product

def can_color(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def assign_windows(n, m, edges):
    # Create an adjacency list to represent the graph of incompatible technicians.
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Try all possible assignments using a backtracking approach
    def backtrack(colors):
        if len(colors) == n:
            return True
        current_tech = len(colors) + 1
        
        for color in range(1, 4):  # Work windows are 1, 2, 3
            if can_color(graph, colors, current_tech, color):
                colors[current_tech] = color
                if backtrack(colors):
                    return True
                del colors[current_tech]
        
        return False

    colors = {}
    if backtrack(colors):
        # Produce the result in lexicographically smallest order
        result = [colors[i] for i in range(1, n + 1)]
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

# Reading input from standard input
input_data = sys.stdin.read().split()
index = 0

n = int(input_data[index])
index += 1
m = int(input_data[index])
index += 1

edges = []
for _ in range(m):
    u = int(input_data[index])
    index += 1
    v = int(input_data[index])
    index += 1
    edges.append((u, v))

assign_windows(n, m, edges)