def can_allocate_channels(n, m, constraints):
    from collections import defaultdict

    # Build the conflict graph
    graph = defaultdict(set)
    for u, v in constraints:
        graph[u].add(v)
        graph[v].add(u)

    # Result array for channels
    channels = [-1] * (n + 1)

    # Function to check if we can assign channels recursively
    def assign_channel(unit):
        if unit > n:
            return True  # All units assigned successfully

        available_channels = {1, 2, 3}

        # Remove channels that are taken by conflicting units
        for neighbor in graph[unit]:
            if channels[neighbor] in available_channels:
                available_channels.remove(channels[neighbor])

        # Try to assign the smallest available channel
        for channel in sorted(available_channels):
            channels[unit] = channel
            if assign_channel(unit + 1):
                return True
            channels[unit] = -1  # Backtrack

        return False

    if assign_channel(1):
        print("YES")
        print(" ".join(map(str, channels[1:])))
    else:
        print("NO")

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
constraints = [tuple(map(int, line.split())) for line in data[1:m + 1]]

can_allocate_channels(n, m, constraints)