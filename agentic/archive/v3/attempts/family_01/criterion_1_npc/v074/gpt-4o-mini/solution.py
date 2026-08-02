def factory_roster_optimization(n, m, incompatibilities):
    from collections import defaultdict, deque
    
    # Build adjacency list for the incompatibilities
    graph = defaultdict(list)
    for u, v in incompatibilities:
        graph[u].append(v)
        graph[v].append(u)
    
    # To store the color of each operator (1, 2, or 3)
    color = [0] * (n + 1)
    
    def bfs(start):
        queue = deque([start])
        color[start] = 1  # Start coloring with 1
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == 0:  # Not colored yet
                    color[neighbor] = 3 - color[node]  # Color with opposite
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # Conflict
                    return False
        return True
    
    for operator in range(1, n + 1):
        if color[operator] == 0:  # Not visited
            if not bfs(operator):
                print("NO")
                return

    # Now we have a valid 2-coloring, we need to assign the third color
    result = [0] * n
    for i in range(1, n + 1):
        if color[i] == 1:
            result[i - 1] = 1
        elif color[i] == 2:
            result[i - 1] = 2
    
    # Fill remaining with 3 to ensure all operators are assigned
    for i in range(n):
        if result[i] == 0:
            result[i] = 3

    print("YES")
    print(" ".join(map(str, result)))

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
incompatibilities = [tuple(map(int, line.split())) for line in data[1:m + 1]]
factory_roster_optimization(n, m, incompatibilities)