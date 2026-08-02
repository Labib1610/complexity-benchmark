def find_conflict_trio(n, m, restrictions):
    from collections import defaultdict
    
    # Create an adjacency list to store the safety restrictions
    graph = defaultdict(set)
    for u, v in restrictions:
        graph[u].add(v)
        graph[v].add(u)

    # Iterate through all pairs of personnel
    for a in range(1, n + 1):
        for b in graph[a]:
            if b > a:  # Ensure a < b
                for c in graph[b]:
                    if c > b and c in graph[a]:  # Ensure b < c and a, b, c are all connected
                        return a, b, c

# Read input
import sys
input = sys.stdin.read
data = input().strip().splitlines()

n, m = map(int, data[0].split())
restrictions = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Find and output the conflict trio
result = find_conflict_trio(n, m, restrictions)
print(*result)