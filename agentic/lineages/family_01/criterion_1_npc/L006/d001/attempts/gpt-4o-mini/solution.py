def can_schedule_tasks(n, m, conflicts):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    
    for u, v in conflicts:
        graph[u].append(v)
        graph[v].append(u)

    # This will store the color (time window) for each task
    colors = [0] * (n + 1)

    def bfs(start):
        queue = deque([start])
        colors[start] = 1  # Starting color
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if colors[neighbor] == 0:  # If not colored
                    # Assign the next color (1, 2, or 3) but not the same as the current node's color
                    colors[neighbor] = 3 - colors[node] if colors[node] in (1, 2) else 1
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:  # Conflict found
                    return False
        return True

    for task in range(1, n + 1):
        if colors[task] == 0:  # Not colored yet
            if not bfs(task):
                print("NO")
                return

    # Now we have a valid coloring
    # Fix the 3-coloring to be lexicographically smallest
    for i in range(1, n + 1):
        if colors[i] == 0:
            colors[i] = 1  # Assign the first available color

    print("YES")
    print(" ".join(map(str, colors[1:])))

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m + 1]]
can_schedule_tasks(n, m, conflicts)