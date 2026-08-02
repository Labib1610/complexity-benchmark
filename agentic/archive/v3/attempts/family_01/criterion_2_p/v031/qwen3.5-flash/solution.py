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
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the channel assignment (0: unassigned, 1: channel 1, 2: channel 2)
    colors = [0] * (n + 1)
    
    # Iterate through nodes 1 to n to handle all connected components.
    # Iterating in increasing order ensures that for any component, the node with the 
    # smallest index is processed first. To satisfy the lexicographically smallest requirement,
    # we assign the smallest possible channel (1) to this node.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS for the component containing node i
            colors[i] = 1
            q = deque([i])
            
            while q:
                u = q.popleft()
                current_channel = colors[u]
                next_channel = 3 - current_channel  # Toggle between 1 and 2
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_channel
                        q.append(v)
                    elif colors[v] != next_channel:
                        # Conflict detected: adjacent nodes have the same color
                        print("NO")
                        return
    
    # If all components are processed without conflicts
    print("YES")
    # Print the channels for nodes 1 through n separated by spaces
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()