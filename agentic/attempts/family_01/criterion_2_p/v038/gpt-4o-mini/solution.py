def roster_allocation(n, m, incompatibilities):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in incompatibilities:
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * (n + 1)  # 0 means uncolored, 1 and 2 will be the two colors
    is_bipartite = True

    def bfs(start):
        nonlocal is_bipartite
        queue = deque([start])
        color[start] = 1  # Start with color 1

        while queue and is_bipartite:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == 0:  # Not colored yet
                    color[neighbor] = 3 - color[node]  # Alternate color (1 <-> 2)
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # Conflict found
                    is_bipartite = False
                    break

    for i in range(1, n + 1):
        if color[i] == 0:  # Not colored yet
            bfs(i)
            if not is_bipartite:
                print("NO")
                return

    print("YES")
    # Create the output array, mapping 1 to 1 and 2 to 2
    result = [color[i] for i in range(1, n + 1)]
    print(' '.join(map(str, result)))

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
incompatibilities = [tuple(map(int, line.split())) for line in data[1:m + 1]]

roster_allocation(n, m, incompatibilities)