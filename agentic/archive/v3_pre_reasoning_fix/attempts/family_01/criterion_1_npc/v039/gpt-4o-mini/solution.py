def can_color_graph(n, edges):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * (n + 1)

    def is_valid(node, c):
        for neighbor in graph[node]:
            if color[neighbor] == c:
                return False
        return True

    def assign_colors(node):
        if node > n:
            return True
        
        for c in range(1, 4):
            if is_valid(node, c):
                color[node] = c
                if assign_colors(node + 1):
                    return True
                color[node] = 0
        
        return False

    if assign_colors(1):
        return color[1:]
    else:
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