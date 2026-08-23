def dual_band_transceiver(n, m, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * (n + 1)  # 0 means uncolored, 1 and 2 will be the colors
    def bfs(start):
        queue = deque([start])
        colors[start] = 1  # Start coloring with 1
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if colors[neighbor] == 0:  # Not colored
                    colors[neighbor] = 2 if colors[node] == 1 else 1
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:  # Conflict
                    return False
        return True

    for i in range(1, n + 1):
        if colors[i] == 0:  # Not colored yet
            if not bfs(i):
                print("NO")
                return

    # If we reach here, we have a valid coloring
    print("YES")
    print(' '.join(map(str, colors[1:])))

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]
dual_band_transceiver(n, m, edges)