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

    # Adjacency list for the graph, 1-indexed
    adj = [[] for _ in range(n + 1)]
    
    # Parse m edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # Array to store the setting of each unit
    # 0 indicates unvisited
    colors = [0] * (n + 1)
    
    # Iterate through all units from 1 to n
    # This ensures that when we encounter an unvisited node i,
    # it is the smallest index in its connected component.
    # To achieve the lexicographically smallest assignment, we must assign setting 1 to this smallest index.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS for the new component
            # We arbitrarily choose colors[i] = 1. Since i is the smallest index in the component,
            # this choice minimizes the sequence lexicographically for this component.
            # If the graph is bipartite, this is always a valid start.
            colors[i] = 1
            q = deque([i])
            
            while q:
                u = q.popleft()
                current_color = colors[u]
                next_color = 3 - current_color # Flip between 1 and 2
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        q.append(v)
                    else:
                        # If already visited, check for consistency
                        if colors[v] != next_color:
                            # Conflict detected: adjacent nodes have the same color
                            print("NO")
                            return

    # If we successfully colored all components without conflicts
    print("YES")
    # Output the assignment sequence
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()