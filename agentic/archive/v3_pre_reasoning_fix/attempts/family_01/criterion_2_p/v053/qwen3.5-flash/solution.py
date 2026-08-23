import sys
from collections import deque

# Increase recursion depth just in case, though we use iterative BFS.
sys.setrecursionlimit(300000)

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

    # Adjacency list for the graph
    # Using 1-based indexing for convenience
    adj = [[] for _ in range(n + 1)]
    
    # Read m edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # Array to store the color (bus assignment) of each module
    # 0: unassigned, 1: Bus 1, 2: Bus 2
    colors = [0] * (n + 1)
    
    # Iterate through all modules 1 to n
    # This ensures we process each connected component
    for i in range(1, n + 1):
        if colors[i] == 0:
            # If module i is unassigned, it belongs to a new connected component.
            # To achieve the lexicographically smallest assignment, we assign Bus 1 (color 1) 
            # to the first module encountered in the component. Since we iterate i from 1 to n,
            # i is the smallest index in this component. Assigning 1 is always better than 2.
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                # The neighbor must be assigned the other bus (1 -> 2, 2 -> 1)
                next_color = 3 - current_color
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    else:
                        # If neighbor is already assigned, check for conflict
                        if colors[v] == current_color:
                            print("NO")
                            return

    # If we successfully assign all modules without conflict
    print("YES")
    # Print the assignment for modules 1 to n
    # Using sys.stdout.write for efficiency with large output
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()