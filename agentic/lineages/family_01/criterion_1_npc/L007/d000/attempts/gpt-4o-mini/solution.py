def can_assign_channels(n, m, constraints):
    from collections import defaultdict

    # Build the adjacency list for the graph
    graph = defaultdict(list)
    for u, v in constraints:
        graph[u].append(v)
        graph[v].append(u)

    # This will hold the channel assignment for each process
    assignment = [0] * (n + 1)

    def backtrack(process):
        if process > n:
            return True
        
        # Try to assign the smallest possible channel (1, 2, or 3)
        for channel in range(1, 4):
            # Check if this channel can be assigned to the process
            conflict = False
            for neighbor in graph[process]:
                if assignment[neighbor] == channel:
                    conflict = True
                    break
            
            if not conflict:
                assignment[process] = channel
                if backtrack(process + 1):
                    return True
                assignment[process] = 0  # Reset on backtrack
        
        return False

    if backtrack(1):
        print("YES")
        print(" ".join(map(str, assignment[1:])))
    else:
        print("NO")


import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
constraints = [tuple(map(int, line.split())) for line in data[1:m + 1]]

can_assign_channels(n, m, constraints)