def can_assign_channels(n, m, restrictions):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in restrictions:
        graph[u].append(v)
        graph[v].append(u)

    channels = [0] * (n + 1)

    def bfs(start):
        queue = deque([start])
        channels[start] = 1  # Start assigning channel 1

        while queue:
            current = queue.popleft()
            current_channel = channels[current]

            for neighbor in graph[current]:
                if channels[neighbor] == 0:  # Not assigned yet
                    channels[neighbor] = 3 - current_channel  # Assign opposite channel (1 <-> 2, 3 <-> 2)
                    queue.append(neighbor)
                elif channels[neighbor] == current_channel:  # Conflict detected
                    return False
        return True

    for technician in range(1, n + 1):
        if channels[technician] == 0:  # Not assigned
            if not bfs(technician):
                return "NO", []

    # Now assign the remaining channels to achieve lexicographically smallest result
    for i in range(1, n + 1):
        if channels[i] == 0:  # Not assigned at all
            channels[i] = 1  # Assign channel 1 as it is preferred

    return "YES", channels[1:]

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
restrictions = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result, assignment = can_assign_channels(n, m, restrictions)
if result == "NO":
    print(result)
else:
    print(result)
    print(" ".join(map(str, assignment)))