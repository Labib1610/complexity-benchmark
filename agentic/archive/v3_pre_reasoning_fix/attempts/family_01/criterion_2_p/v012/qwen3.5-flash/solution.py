import sys
from collections import deque

def solve():
    # Read all input from standard input at once for efficiency
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for the graph, 1-based indexing
    adj = [[] for _ in range(n + 1)]
    
    # Read m edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
            
    # Colors array: 0 = uncolored, 1 = work period 1, 2 = work period 2
    colors = [0] * (n + 1)
    
    # Iterate through all nodes from 1 to n
    # Iterating in increasing order ensures we encounter the smallest index of each component first.
    # To achieve the lexicographically smallest sequence, we assign the first node of a component
    # (which is the smallest index in that component) to work period 1.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start a BFS for the connected component containing i
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                next_color = 3 - current_color # Toggle between 1 and 2
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] == current_color:
                        # Conflict detected: adjacent nodes have the same color
                        # This implies the graph is not bipartite
                        print("NO")
                        return
    
    # If no conflicts found after checking all nodes
    print("YES")
    # Print the work periods for personnel 1 to n separated by spaces
    print(*(colors[1:]))

if __name__ == '__main__':
    solve()