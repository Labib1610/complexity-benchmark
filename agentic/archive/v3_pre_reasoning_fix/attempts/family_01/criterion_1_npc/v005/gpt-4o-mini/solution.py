def can_assign(n, incompatibilities):
    from itertools import combinations
    
    # Create an adjacency list for the incompatibility graph
    graph = [[] for _ in range(n + 1)]
    for u, v in incompatibilities:
        graph[u].append(v)
        graph[v].append(u)
    
    # Try to assign shifts using a backtracking approach
    assignments = [0] * (n + 1)  # Index 0 will not be used

    def backtrack(worker):
        if worker > n:
            return True  # All workers assigned
        
        for slot in range(1, 4):  # Three time slots
            # Check if we can assign this worker to the slot
            if all(assignments[neighbor] != slot for neighbor in graph[worker]):
                assignments[worker] = slot
                if backtrack(worker + 1):
                    return True
                assignments[worker] = 0  # Backtrack
        
        return False

    if backtrack(1):
        print("YES")
        print(' '.join(map(str, assignments[1:])))
    else:
        print("NO")

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
incompatibilities = [tuple(map(int, line.split())) for line in data[1:m + 1]]
can_assign(n, incompatibilities)