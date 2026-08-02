def find_guilds(n, m, treaties):
    from collections import defaultdict
    
    # Create an adjacency list for the graph
    graph = defaultdict(set)
    for u, v in treaties:
        graph[u].add(v)
        graph[v].add(u)
    
    # Iterate through each pair of guilds to find a common third guild
    for a in range(1, n + 1):
        for b in graph[a]:
            if b > a:  # Ensure a < b to avoid duplicates
                # Find a common neighbor c
                common_neighbors = graph[a].intersection(graph[b])
                for c in sorted(common_neighbors):  # Sort to ensure lexicographical order
                    if c > b:  # Ensure b < c
                        return a, b, c

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
treaties = [tuple(map(int, line.split())) for line in data[1:m + 1]]

result = find_guilds(n, m, treaties)
print(*result)