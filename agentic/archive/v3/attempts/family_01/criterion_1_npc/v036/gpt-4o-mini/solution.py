def can_schedule_experiments(n, m, conflicts):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in conflicts:
        graph[u].append(v)
        graph[v].append(u)

    colors = [-1] * (n + 1)

    def bfs(start):
        queue = deque([start])
        colors[start] = 0  # Start with color 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if colors[neighbor] == -1:  # Not colored
                    colors[neighbor] = 1 - colors[node]  # Alternate color
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:  # Conflict found
                    return False
        return True

    for experiment in range(1, n + 1):
        if colors[experiment] == -1:  # Not visited
            if not bfs(experiment):
                print("NO")
                return

    # We have a valid coloring here, now assign to blocks 1, 2, 3
    result = [0] * n
    for i in range(1, n + 1):
        result[i - 1] = (colors[i] // 2) + 1  # Map color to block

    # Adjust to ensure lexicographically smallest
    for i in range(n):
        if result[i] == 0:
            result[i] = 1

    print("YES")
    print(" ".join(map(str, result)))

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m + 1]]
can_schedule_experiments(n, m, conflicts)