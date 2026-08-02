import sys
from collections import deque

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for the graph
    adj = [[] for _ in range(N + 1)]
    
    # Parse edges
    for _ in range(M):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
        
    colors = [0] * (N + 1)
    
    # Iterate through each node to ensure all components are processed
    # We process nodes in order 1 to N to ensure lexicographically smallest result
    for i in range(1, N + 1):
        if colors[i] == 0:
            # Start BFS for the connected component containing i
            # To achieve lexicographically smallest sequence, we assign color 1 to i
            # because i is the smallest index in this component encountered so far.
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                next_color = 3 - current_color
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] == current_color:
                        # Conflict detected: graph is not bipartite
                        print("NO")
                        return

    # If no conflicts were found
    print("YES")
    # Output the coloring sequence
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()