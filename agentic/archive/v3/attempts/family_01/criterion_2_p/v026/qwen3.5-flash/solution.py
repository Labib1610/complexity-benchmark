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
    # Using 1-based indexing for nodes
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store channel assignments: 0 = unassigned, 1 = Channel 1, 2 = Channel 2
    color = [0] * (n + 1)
    
    # We need to check if the graph is bipartite and find the lexicographically smallest valid assignment.
    # For a bipartite graph, each connected component can be colored in 2 ways (swapping channels).
    # To minimize the sequence (s_1, s_2, ..., s_n) lexicographically, we must prioritize smaller values for smaller indices.
    # For each connected component, the node with the smallest index determines the coloring choice.
    # Since we iterate i from 1 to n, the first uncolored node we encounter belongs to a new component
    # and is the smallest index in that component. We must assign it Channel 1 to ensure lexicographical minimality.
    # Then we propagate the coloring to the rest of the component.
    
    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        
        # Start BFS for the component containing node i
        # Assign channel 1 to the smallest index node in this component
        color[i] = 1
        queue = deque([i])
        
        while queue:
            u = queue.popleft()
            current_color = color[u]
            next_color = 3 - current_color  # If current is 1, next is 2; if 2, next is 1
            
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = next_color
                    queue.append(v)
                elif color[v] == current_color:
                    # Conflict detected: adjacent nodes have the same color
                    # The graph is not bipartite
                    print("NO")
                    return

    # If we successfully processed all nodes without conflict
    print("YES")
    # Output the assignment vector
    sys.stdout.write(' '.join(map(str, color[1:])) + '\n')

if __name__ == '__main__':
    solve()