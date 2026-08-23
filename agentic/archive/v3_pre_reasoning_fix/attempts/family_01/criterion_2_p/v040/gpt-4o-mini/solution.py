def channel_assignment(n, m, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * (n + 1)  # 0 means uncolored, 1 and 2 will be our two colors
    def bfs(start):
        queue = deque([start])
        colors[start] = 1  # Start coloring with color 1
        while queue:
            node = queue.popleft()
            current_color = colors[node]
            next_color = 2 if current_color == 1 else 1
            for neighbor in graph[node]:
                if colors[neighbor] == 0:  # If uncolored
                    colors[neighbor] = next_color
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:  # Conflict in coloring
                    return False
        return True

    for i in range(1, n + 1):
        if colors[i] == 0:  # Not colored yet
            if not bfs(i):
                print("NO")
                return

    result = colors[1:]  # Exclude index 0
    print("YES")
    print(' '.join(map(str, result)))

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m+1]]
channel_assignment(n, m, edges)