import sys
from collections import deque

def solve():
    # Read all input from stdin efficiently
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
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # Array to store colors (0: uncolored, 1: shift 1, 2: shift 2)
    colors = [0] * (n + 1)
    
    # Iterate through all workers to handle disconnected components
    # We iterate 1 to n to ensure lexicographically smallest assignment
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS for this component
            # To ensure lexicographically smallest assignment,
            # we assign the smallest worker in the component (which is i) to shift 1.
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                next_color = 3 - current_color  # 3-1=2, 3-2=1
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] != next_color:
                        # Conflict detected: graph is not bipartite
                        print("NO")
                        return
    
    # If no conflicts found
    print("YES")
    # Print colors for workers 1 to n
    # Using sys.stdout.write for efficiency with large output
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()