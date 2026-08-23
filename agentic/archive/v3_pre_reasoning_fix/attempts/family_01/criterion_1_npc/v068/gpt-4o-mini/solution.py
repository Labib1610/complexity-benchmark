def can_color(n, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * (n + 1)  # 0 means uncolored, 1, 2, 3 are the possible colors

    def bfs(start):
        queue = deque([start])
        colors[start] = 1  # Start coloring with 1

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if colors[v] == 0:  # If not colored
                    # Color it with the next available color
                    for c in range(1, 4):
                        if c != colors[u] and all(colors[neighbour] != c for neighbour in graph[v]):
                            colors[v] = c
                            queue.append(v)
                            break
                    else:
                        return False  # No valid coloring found
                elif colors[v] == colors[u]:  # Conflict found
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
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]
can_color(n, edges)