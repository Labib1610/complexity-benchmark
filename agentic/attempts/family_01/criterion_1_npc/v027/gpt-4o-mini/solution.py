def can_allocate_frequencies(n, m, edges):
    from collections import defaultdict, deque
    
    # Create an adjacency list for the interference graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Frequency assignment array
    frequencies = [0] * (n + 1)  # Index 0 is unused

    def bfs(start):
        queue = deque([start])
        frequencies[start] = 1  # Start with frequency 1
        
        while queue:
            current = queue.popleft()
            current_freq = frequencies[current]
            next_freq = 1
            
            for neighbor in graph[current]:
                if frequencies[neighbor] == 0:  # Unassigned
                    while next_freq == current_freq or any(frequencies[nbr] == next_freq for nbr in graph[neighbor]):
                        next_freq += 1
                    frequencies[neighbor] = next_freq
                    queue.append(neighbor)
                elif frequencies[neighbor] == current_freq:
                    return False  # Conflict detected
        
        return True

    # Check all components in the graph
    for transmitter in range(1, n + 1):
        if frequencies[transmitter] == 0:  # Not yet assigned
            if not bfs(transmitter):
                return "NO", []

    # Return the answer in lexicographically smallest order
    result = frequencies[1:]  # Ignore index 0
    return "YES", result


import sys
input = sys.stdin.read

data = input().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m+1]]

result = can_allocate_frequencies(n, m, edges)

if result[0] == "NO":
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, result[1])))