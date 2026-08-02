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

    # Adjacency list for the graph. Using 1-based indexing.
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break

    # Array to store colors: 0 = unvisited, 1 = color 1, 2 = color 2
    color = [0] * (n + 1)
    
    # Iterate through each node from 1 to n to handle disconnected components
    for i in range(1, n + 1):
        if color[i] == 0:
            # If node i is unvisited, it belongs to a new component.
            # We assign it color 1. Since we iterate from 1 to n, 
            # i is the smallest index in this component. Assigning 1 to the 
            # smallest index ensures the lexicographically smallest assignment 
            # for this component.
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
                    elif color[v] != next_color:
                        # If a neighbor has the same color, the graph is not bipartite
                        print("NO")
                        return

    # If we successfully colored all nodes without conflict
    print("YES")
    # Print the colors for nodes 1 to n separated by spaces
    print(' '.join(map(str, color[1:])))

if __name__ == '__main__':
    solve()