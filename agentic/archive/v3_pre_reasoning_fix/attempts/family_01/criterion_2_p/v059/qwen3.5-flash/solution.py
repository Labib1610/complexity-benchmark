import sys
from collections import deque

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Build adjacency list for the graph
    # Using 1-based indexing for stations 1 to n
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the frequency band for each station
    # 0 indicates unvisited, 1 and 2 are the available bands
    color = [0] * (n + 1)
    
    # Iterate through all stations to handle all connected components
    # This ensures we visit every station and handle disconnected parts of the graph
    for i in range(1, n + 1):
        if color[i] == 0:
            # We found a new connected component.
            # To achieve the lexicographically smallest configuration, we should assign
            # the smallest possible value to the earliest station in the component.
            # Since we iterate i from 1 to n, 'i' is the smallest index in this component.
            # We assign band 1 to station i. This forces the assignment of all other
            # stations in this component due to the constraints.
            color[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                
                # If station u is in band 1, its neighbors must be in band 2.
                # If station u is in band 2, its neighbors must be in band 1.
                # This can be computed as 3 - color[u].
                target_color = 3 - color[u]
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = target_color
                        queue.append(v)
                    elif color[v] != target_color:
                        # Conflict detected: adjacent stations have the same frequency band.
                        # This means the graph is not bipartite.
                        print("NO")
                        return

    # If no conflicts were found, a valid configuration exists.
    print("YES")
    # Output the configuration for stations 1 to n
    print(" ".join(map(str, color[1:])))

if __name__ == '__main__':
    solve()