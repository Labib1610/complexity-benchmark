import sys
from collections import deque

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Initialize adjacency list for the graph (1-based indexing)
    adj = [[] for _ in range(n + 1)]
    
    # Read m edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the bus line assignment (color) for each hub
    # 0: unvisited, 1: bus line 1, 2: bus line 2
    colors = [0] * (n + 1)
    
    # Iterate through each hub from 1 to n
    # This order ensures that for each connected component, we start with the smallest index node
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS for the component containing node i
            # To achieve the lexicographically smallest sequence, we assign color 1 to the 
            # smallest index node in the component (which is 'i' here).
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
                        # Conflict detected: adjacent nodes have the same color
                        # This implies the graph is not bipartite
                        sys.stdout.write("NO\n")
                        return

    # If no conflicts are found, a valid assignment exists
    sys.stdout.write("YES\n")
    # Output the assignment sequence for nodes 1 to n
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()