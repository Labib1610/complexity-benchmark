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
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # Array to store the slot assignment (color) for each person
    # 0: unassigned, 1: Slot 1, 2: Slot 2
    colors = [0] * (n + 1)
    
    # Iterate through all personnel from 1 to n.
    # This ensures we process components in an order that allows us to 
    # greedily assign Slot 1 to the smallest index node in each component,
    # achieving the lexicographically smallest sequence.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start a BFS traversal for the connected component containing i
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                next_color = 3 - current_color  # Flip between 1 and 2
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] == current_color:
                        # Conflict detected: adjacent nodes have the same color
                        # This means the graph is not bipartite
                        print("NO")
                        return
    
    # If we successfully assigned slots without conflicts
    print("YES")
    # Print the assignment for personnel 1 to n
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()