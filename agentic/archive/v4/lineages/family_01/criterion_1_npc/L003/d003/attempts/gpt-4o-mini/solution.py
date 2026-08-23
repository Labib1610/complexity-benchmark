def can_assign_phases(n, m, constraints):
    from collections import defaultdict, deque

    # Create an adjacency list for the graph
    graph = defaultdict(list)
    for u, v in constraints:
        graph[u].append(v)
        graph[v].append(u)

    # To store the phase assigned to each module (1-indexed)
    phases = [0] * (n + 1)

    # BFS for coloring the graph with 3 colors
    def bfs(start):
        queue = deque([start])
        phases[start] = 1  # Start coloring with phase 1

        while queue:
            node = queue.popleft()
            current_phase = phases[node]
            for neighbor in graph[node]:
                if phases[neighbor] == 0:  # Not colored yet
                    # Assign a phase that is different from the current node
                    for phase in range(1, 4):
                        if phase != current_phase and all(phases[neigh] != phase for neigh in graph[neighbor]):
                            phases[neighbor] = phase
                            queue.append(neighbor)
                            break
                elif phases[neighbor] == current_phase:  # Conflict found
                    return False
        return True

    # Try to color each component of the graph
    for module in range(1, n + 1):
        if phases[module] == 0:  # Not assigned yet
            if not bfs(module):
                print("NO")
                return

    # Output the result if successful
    print("YES")
    print(" ".join(map(str, phases[1:])))
    
import sys
input = sys.stdin.read
data = input().strip().splitlines()
n, m = map(int, data[0].split())
constraints = [tuple(map(int, line.split())) for line in data[1:m + 1]]
can_assign_phases(n, m, constraints)