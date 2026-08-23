def assign_modes(n, m, conflicts):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in conflicts:
        graph[u].append(v)
        graph[v].append(u)

    modes = [0] * (n + 1)  # 0 means unassigned, 1 means mode 1, 2 means mode 2

    def bfs(start):
        queue = deque([start])
        modes[start] = 1  # Start by assigning mode 1
        while queue:
            node = queue.popleft()
            current_mode = modes[node]
            next_mode = 2 if current_mode == 1 else 1
            
            for neighbor in graph[node]:
                if modes[neighbor] == 0:  # Not assigned yet
                    modes[neighbor] = next_mode
                    queue.append(neighbor)
                elif modes[neighbor] == current_mode:  # Conflict detected
                    return False
        return True

    for i in range(1, n + 1):
        if modes[i] == 0:  # Unvisited node
            if not bfs(i):
                print("NO")
                return

    print("YES")
    print(" ".join(map(str, modes[1:])))

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m+1]]
assign_modes(n, m, conflicts)