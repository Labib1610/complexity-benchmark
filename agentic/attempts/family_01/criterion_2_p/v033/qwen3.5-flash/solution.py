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
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # Array to store group assignment (0: unvisited, 1: group 1, 2: group 2)
    colors = [0] * (n + 1)
    
    # Iterate through each node to handle disconnected components.
    # Processing nodes in increasing order (1 to n) ensures that for each component,
    # we encounter the smallest-indexed node first. By assigning it to group 1,
    # we ensure the lexicographically smallest sequence.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS for the connected component containing node i
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                c = colors[u]
                next_c = 3 - c  # Toggle between 1 and 2 (1->2, 2->1)
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_c
                        queue.append(v)
                    elif colors[v] == c:
                        # If a neighbor has the same color, the graph is not bipartite
                        print("NO")
                        return

    # If the loop completes without conflicts, a valid assignment exists
    print("YES")
    # Print the colors for nodes 1 to n space-separated
    print(' '.join(map(str, colors[1:])))

if __name__ == '__main__':
    solve()