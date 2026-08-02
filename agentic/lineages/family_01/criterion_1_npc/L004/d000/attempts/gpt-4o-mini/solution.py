def assign_zones(n, m, edges):
    from collections import defaultdict, deque

    # Build the adjacency list for the interference graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # This will store the zone assignments
    zone_assignment = [0] * (n + 1)

    def bfs(start):
        queue = deque([start])
        zone_assignment[start] = 1  # Start with zone 1

        while queue:
            current = queue.popleft()
            current_zone = zone_assignment[current]

            for neighbor in graph[current]:
                if zone_assignment[neighbor] == 0:  # Not assigned yet
                    # Assign the next zone (cycle through 1, 2, 3)
                    zone_assignment[neighbor] = 1 if current_zone == 2 else 2 if current_zone == 3 else 3
                    queue.append(neighbor)
                elif zone_assignment[neighbor] == current_zone:  # Conflict found
                    return False
        return True

    for i in range(1, n + 1):
        if zone_assignment[i] == 0:  # Not assigned yet
            if not bfs(i):
                print("NO")
                return

    # We need to adjust the zones to ensure they are lexicographically smallest
    result = [zone_assignment[i] for i in range(1, n + 1)]
    print("YES")
    print(" ".join(map(str, result)))

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

assign_zones(n, m, edges)