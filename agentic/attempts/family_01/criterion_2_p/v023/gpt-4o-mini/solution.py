def can_allocate_channels(N, M, edges):
    from collections import defaultdict, deque
    
    # Create an adjacency list for the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Array to store the channel for each post (1 or 2), initialized to 0 (unassigned)
    channels = [0] * (N + 1)
    
    def bfs(start):
        queue = deque([start])
        channels[start] = 1  # Start with channel 1
        
        while queue:
            node = queue.popleft()
            current_channel = channels[node]
            next_channel = 2 if current_channel == 1 else 1
            
            for neighbor in graph[node]:
                if channels[neighbor] == 0:  # Not assigned
                    channels[neighbor] = next_channel
                    queue.append(neighbor)
                elif channels[neighbor] == current_channel:  # Conflict
                    return False
        return True

    for post in range(1, N + 1):
        if channels[post] == 0:  # Not visited yet
            if not bfs(post):
                return "NO"
    
    return "YES", channels[1:]

import sys
input = sys.stdin.read
data = input().strip().splitlines()
N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]

result = can_allocate_channels(N, M, edges)

if result == "NO":
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, result[1])))