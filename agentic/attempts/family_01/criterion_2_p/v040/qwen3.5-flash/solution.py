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
    
    # Read m edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the color of each node (0: uncolored, 1: color 1, 2: color 2)
    color = [0] * (n + 1)
    
    # Iterate through all nodes from 1 to n.
    # This order ensures that for any connected component, we process it 
    # starting from the node with the smallest index.
    for i in range(1, n + 1):
        if color[i] == 0:
            # Node i is uncolored, so it starts a new component.
            # To minimize the sequence lexicographically, we must assign the smallest possible
            # channel (1) to the first node in the sequence that belongs to this component.
            # Since we iterate i from 1 to n, i is the smallest index in this component.
            color[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 3 - current_color  # Toggle between 1 and 2
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] == current_color:
                        # Conflict detected: graph is not bipartite
                        print("NO")
                        return

    # If valid assignment found for all components
    print("YES")
    # Print the colors for nodes 1 to n separated by spaces
    print(*(color[1:]))

if __name__ == '__main__':
    solve()