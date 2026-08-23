def can_schedule(n, m, conflicts):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in conflicts:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * (n + 1)  # 0 means unassigned, 1, 2, or 3 are window assignments

    def bfs(start):
        queue = deque([start])
        colors[start] = 1  # Start coloring with 1
        while queue:
            node = queue.popleft()
            current_color = colors[node]
            next_color = 1 if current_color == 3 else current_color + 1
            
            for neighbor in graph[node]:
                if colors[neighbor] == 0:  # If not colored
                    colors[neighbor] = next_color
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:  # Conflict found
                    return False
        return True

    for i in range(1, n + 1):
        if colors[i] == 0:  # Not colored yet
            if not bfs(i):
                print("NO")
                return

    print("YES")
    print(" ".join(map(str, colors[1:])))

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m + 1]]
can_schedule(n, m, conflicts)