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

    # Adjacency list for the graph (1-based indexing)
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # Array to store the color (frequency band) of each device. 0 means unvisited.
    # 1 represents band 1, 2 represents band 2.
    colors = [0] * (n + 1)
    
    # Iterate through each device from 1 to n.
    # If a device is unvisited, it belongs to a new connected component.
    # To ensure the lexicographically smallest sequence, we assign band 1 
    # to the first unvisited node in the component (which is the smallest index in that component).
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS for this component
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                next_color = 3 - current_color  # Toggle between 1 and 2
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] == current_color:
                        # If a neighbor has the same color, the graph is not bipartite
                        print("NO")
                        return
    
    # If we successfully colored all devices without conflicts
    print("YES")
    # Print the configuration for devices 1 to n
    print(' '.join(map(str, colors[1:])))

if __name__ == '__main__':
    solve()