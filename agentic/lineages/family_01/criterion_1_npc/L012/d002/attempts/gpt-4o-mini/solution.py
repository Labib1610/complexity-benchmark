def can_assign_shifts(n, m, conflicts):
    from collections import defaultdict, deque
    
    # Create an adjacency list for the conflicts
    graph = defaultdict(list)
    for u, v in conflicts:
        graph[u].append(v)
        graph[v].append(u)

    # Array to store the shift assignments
    shifts = [0] * (n + 1)  # 1-based indexing

    # Try to assign shifts
    for i in range(1, n + 1):
        if shifts[i] == 0:  # Not assigned yet
            # Attempt to assign the smallest available shift
            available_shifts = {1, 2, 3}
            for neighbor in graph[i]:
                if shifts[neighbor] in available_shifts:
                    available_shifts.remove(shifts[neighbor])
            # Assign the smallest available shift
            shifts[i] = min(available_shifts)

            # Propagate the assignment to neighbors
            queue = deque([i])
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if shifts[neighbor] == 0:  # Not assigned yet
                        # Attempt to assign the smallest available shift
                        available_shifts = {1, 2, 3}
                        for conflict_neighbor in graph[neighbor]:
                            if shifts[conflict_neighbor] in available_shifts:
                                available_shifts.remove(shifts[conflict_neighbor])
                        shifts[neighbor] = min(available_shifts)
                        queue.append(neighbor)

    # Check if any conflicts exist
    for u in range(1, n + 1):
        for v in graph[u]:
            if shifts[u] == shifts[v]:
                return "NO", []

    return "YES", shifts[1:]

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result, assignment = can_assign_shifts(n, m, conflicts)

if result == "NO":
    print(result)
else:
    print(result)
    print(' '.join(map(str, assignment)))