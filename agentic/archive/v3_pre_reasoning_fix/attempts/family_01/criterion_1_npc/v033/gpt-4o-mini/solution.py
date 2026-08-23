def can_assign_channels(n, m, edges):
    from collections import defaultdict, deque

    # Build adjacency list for the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Channel assignment array
    channels = [0] * (n + 1)

    def bfs(start):
        queue = deque([start])
        channels[start] = 1  # Start with channel 1

        while queue:
            node = queue.popleft()
            current_channel = channels[node]

            for neighbor in graph[node]:
                if channels[neighbor] == 0:  # Not assigned yet
                    # Assign the smallest channel that is not current
                    for channel in range(1, 4):
                        if channel != current_channel and all(channels[neigh] != channel for neigh in graph[neighbor]):
                            channels[neighbor] = channel
                            break
                    queue.append(neighbor)
                elif channels[neighbor] == current_channel:
                    return False  # Conflict found

        return True

    for i in range(1, n + 1):
        if channels[i] == 0:  # Not assigned yet
            if not bfs(i):
                return "NO", []

    return "YES", channels[1:]

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = can_assign_channels(n, m, edges)

if result[0] == "NO":
    print(result[0])
else:
    print(result[0])
    print(" ".join(map(str, result[1])))