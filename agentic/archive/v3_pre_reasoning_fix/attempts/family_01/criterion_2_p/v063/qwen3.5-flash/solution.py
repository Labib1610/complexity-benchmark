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
    adj = [[] for _ in range(n + 1)]
    
    # Parse edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
        
    # Array to store colors (0: uncolored, 1: color A, 2: color B)
    colors = [0] * (n + 1)
    
    # Iterate through all nodes to handle disconnected components
    # We iterate from 1 to n to ensure we process components in an order
    # that respects the lexicographical requirement.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Found a new component. 
            # To get lexicographically smallest sequence, assign 1 to the smallest index node (i).
            # Since i is the first uncolored node encountered, it is the minimum index in this component.
            colors[i] = 1
            q = deque([i])
            
            while q:
                u = q.popleft()
                current_color = colors[u]
                next_color = 3 - current_color  # Flip between 1 and 2
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        q.append(v)
                    elif colors[v] == current_color:
                        # Conflict detected: graph is not bipartite
                        print("NO")
                        return
    
    # If we reach here, a valid assignment exists
    print("YES")
    # Print the assignment for nodes 1 to n
    # Using sys.stdout.write for efficiency with large outputs
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()