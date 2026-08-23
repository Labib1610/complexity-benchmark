def can_assign_vaults(n, m, incompatible_pairs):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in incompatible_pairs:
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * (n + 1)  # -1 means uncolored

    def bfs(start):
        queue = deque([start])
        color[start] = 0  # Start coloring with vault 1 which is represented as 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # If not colored
                    color[neighbor] = (color[node] + 1) % 3
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # Conflict
                    return False
        return True

    for i in range(1, n + 1):
        if color[i] == -1:  # Not colored yet
            if not bfs(i):
                return "NO", []

    # Convert 0, 1, 2 to 1, 2, 3 for output
    result = [color[i] + 1 for i in range(1, n + 1)]
    return "YES", result

import sys
input = sys.stdin.read
data = input().strip().splitlines()

n, m = map(int, data[0].split())
incompatible_pairs = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = can_assign_vaults(n, m, incompatible_pairs)

if result[0] == "NO":
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, result[1])))