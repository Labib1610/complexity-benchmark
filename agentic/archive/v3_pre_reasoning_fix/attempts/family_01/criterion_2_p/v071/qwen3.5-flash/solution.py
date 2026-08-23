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

    # Adjacency list for the graph
    # Using 1-based indexing for compounds (size n + 1)
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Array to store the vault assignment (0: unassigned, 1: Vault 1, 2: Vault 2)
    colors = [0] * (n + 1)
    
    # Iterate through each compound to handle disconnected components.
    # Processing in increasing order of index ensures lexicographically smallest sequence.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS for the component containing i.
            # To achieve lexicographically smallest sequence, assign color 1 to the smallest index node
            # encountered so far in this component traversal.
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                next_color = 3 - current_color  # If 1, next is 2; if 2, next is 1
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] == current_color:
                        # Conflict detected: graph is not bipartite
                        print("NO")
                        return

    # If valid assignment found for all components
    print("YES")
    # Output the assignments for 1 to n
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()