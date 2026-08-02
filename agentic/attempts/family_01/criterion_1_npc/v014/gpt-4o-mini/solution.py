def can_assign_shifts(n, m, conflicts):
    from itertools import combinations
    
    # Create adjacency list for the incompatibilities
    graph = [[] for _ in range(n + 1)]
    for u, v in conflicts:
        graph[u].append(v)
        graph[v].append(u)

    # Shift assignment array
    shifts = [0] * (n + 1)

    def is_valid_assignment(worker, shift):
        for neighbor in graph[worker]:
            if shifts[neighbor] == shift:
                return False
        return True

    def assign_shifts(worker):
        if worker > n:
            return True

        for shift in range(1, 4):
            if is_valid_assignment(worker, shift):
                shifts[worker] = shift
                if assign_shifts(worker + 1):
                    return True
                shifts[worker] = 0  # backtrack

        return False
    
    if assign_shifts(1):
        return "YES\n" + ' '.join(map(str, shifts[1:]))
    else:
        return "NO"

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
conflicts = [tuple(map(int, line.split())) for line in data[1:m + 1]]

print(can_assign_shifts(n, m, conflicts))