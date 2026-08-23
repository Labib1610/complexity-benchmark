def schedule_compatibility(n, m, incompatibilities):
    from itertools import combinations

    # Create a graph for incompatibilities
    graph = [[] for _ in range(n + 1)]
    for u, v in incompatibilities:
        graph[u].append(v)
        graph[v].append(u)

    # Function to check if a coloring is valid
    def is_valid(coloring):
        for u in range(1, n + 1):
            for v in graph[u]:
                if coloring[u] == coloring[v]:
                    return False
        return True

    # Try to color the graph using backtracking
    def backtrack(index, coloring):
        if index == n + 1:  # All staff members are colored
            return is_valid(coloring)
        
        for time_block in range(1, 4):
            coloring[index] = time_block
            if backtrack(index + 1, coloring):
                return True
            coloring[index] = 0  # Reset
            
        return False

    # Store the coloring result
    coloring = [0] * (n + 1)
    
    if backtrack(1, coloring):
        print("YES")
        print(" ".join(map(str, coloring[1:])))
    else:
        print("NO")

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
incompatibilities = [tuple(map(int, line.split())) for line in data[1:m + 1]]
schedule_compatibility(n, m, incompatibilities)