def shift_assignment(n, m, conflicts):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in conflicts:
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * (n + 1)  # 0 means uncolored, 1 and 2 will be the two shifts

    def bfs(start):
        queue = deque([start])
        color[start] = 1  # Start coloring with 1

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == 0:  # Not colored
                    color[neighbor] = 3 - color[node]  # Alternate colors
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # Conflict detected
                    return False
        return True

    for worker in range(1, n + 1):
        if color[worker] == 0:  # Not yet colored
            if not bfs(worker):
                print("NO")
                return

    # Prepare the output
    print("YES")
    print(" ".join(map(str, color[1:])))

import sys
input = sys.stdin.read
data = input().strip().splitlines()
n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m + 1]]

shift_assignment(n, m, conflicts)