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

    # Build the graph using an adjacency list
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Array to store the color (mode) of each transceiver
    # 0: unvisited, 1: mode 1, 2: mode 2
    colors = [0] * (n + 1)
    
    # Iterate through each node to handle disconnected components.
    # By iterating from 1 to n, when we encounter an unvisited node 'i',
    # it is the smallest index in its connected component.
    # To obtain the lexicographically smallest sequence, we must assign
    # the smallest possible value (1) to this node.
    for i in range(1, n + 1):
        if colors[i] == 0:
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                c = colors[u]
                # The required color for neighbors is 3 - c (1 becomes 2, 2 becomes 1)
                next_c = 3 - c
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_c
                        queue.append(v)
                    elif colors[v] != next_c:
                        # Conflict detected: adjacent nodes have the same color
                        # This implies the graph is not bipartite
                        print("NO")
                        return

    # If no conflicts were found, a valid assignment exists
    print("YES")
    # Print the colors for nodes 1 to n, separated by spaces
    print(*(colors[1:]))

if __name__ == '__main__':
    solve()