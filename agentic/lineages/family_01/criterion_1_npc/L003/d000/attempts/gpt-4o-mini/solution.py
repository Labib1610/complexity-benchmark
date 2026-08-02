def can_assign_shifts(n, m, conflicts):
    from collections import defaultdict, deque

    # Create adjacency list for the graph
    graph = defaultdict(list)
    for u, v in conflicts:
        graph[u].append(v)
        graph[v].append(u)

    # This will hold the shift assignments
    shifts = [0] * (n + 1)

    # Function to perform BFS and try to color the graph
    def bfs(start):
        queue = deque([start])
        shifts[start] = 1  # Start assigning the first shift

        while queue:
            current = queue.popleft()
            current_shift = shifts[current]

            for neighbor in graph[current]:
                if shifts[neighbor] == 0:  # If not assigned yet
                    # Assign the next available shift
                    shifts[neighbor] = 3 - current_shift if current_shift in (1, 2) else 1
                    queue.append(neighbor)
                elif shifts[neighbor] == current_shift:  # Conflict found
                    return False
        return True

    # Try to color the graph
    for employee in range(1, n + 1):
        if shifts[employee] == 0:  # Not yet colored
            if not bfs(employee):
                print("NO")
                return

    # Adjust shifts to be in {1, 2, 3} and ensure lexicographical order
    for i in range(1, n + 1):
        if shifts[i] == 0:
            shifts[i] = 1  # Default to shift 1 for uncolored
        if shifts[i] > 3:
            shifts[i] = 1  # Normalize to valid shifts

    print("YES")
    print(" ".join(map(str, shifts[1:])))
    

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m+1]]

can_assign_shifts(n, m, conflicts)