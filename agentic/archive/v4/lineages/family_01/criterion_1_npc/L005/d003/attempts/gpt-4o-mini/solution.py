def is_valid_assignment(n, m, restrictions):
    from collections import defaultdict

    # Create adjacency list for graph representation
    graph = defaultdict(set)
    for u, v in restrictions:
        graph[u].add(v)
        graph[v].add(u)

    # To store the assigned values for each position
    assignment = [0] * (n + 1)

    def backtrack(position):
        if position > n:
            return True  # Successfully assigned all positions
        for value in range(1, 4):  # Try values 1, 2, 3
            can_assign = True
            
            # Check for restrictions
            for neighbor in graph[position]:
                if assignment[neighbor] == value:
                    can_assign = False
                    break
            
            if can_assign:
                assignment[position] = value
                if backtrack(position + 1):
                    return True
                assignment[position] = 0  # Backtrack

        return False

    if backtrack(1):
        print("YES")
        print(' '.join(map(str, assignment[1:])))
    else:
        print("NO")

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
restrictions = [tuple(map(int, line.split())) for line in data[1:m + 1]]

is_valid_assignment(n, m, restrictions)