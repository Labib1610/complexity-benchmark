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

    # Initialize adjacency list for the graph using 1-based indexing
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break

    # Array to store the laboratory assignment:
    # 0: unvisited, 1: Laboratory 1, 2: Laboratory 2
    color = [0] * (n + 1)
    
    # Iterate through all researchers from 1 to n.
    # This order ensures that for any connected component, the first researcher
    # we encounter (which will be the one with the smallest index in that component)
    # is processed first.
    # To achieve the lexicographically smallest assignment sequence, we must assign
    # this first researcher to Laboratory 1 (color 1), as 1 < 2.
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS for the connected component containing i
            color[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                
                for v in adj[u]:
                    if color[v] == 0:
                        # Assign the opposite laboratory to the neighbor
                        color[v] = 3 - current_color
                        queue.append(v)
                    elif color[v] == current_color:
                        # Conflict detected: adjacent researchers in the same laboratory
                        # The graph is not bipartite
                        print("NO")
                        return

    # If we successfully colored all components without conflict
    print("YES")
    # Print the assignment sequence for researchers 1 to n
    print(*(color[1:]))

if __name__ == '__main__':
    solve()