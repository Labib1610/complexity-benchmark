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

    # Build the graph using adjacency list
    # Nodes are 1-indexed, so size is n + 1
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # Array to store the mode (color) of each personnel
    # 0: unassigned, 1: Mode 1, 2: Mode 2
    color = [0] * (n + 1)
    
    # Iterate through all personnel to handle connected components
    # We want the lexicographically smallest assignment sequence (s_1, s_2, ..., s_n).
    # This means we want s_1 to be 1 if possible, then s_2 to be 1 if possible, etc.
    # For a connected component, the assignment is determined by the color of one node.
    # Specifically, if we fix the color of the node with the smallest index in the component,
    # all other nodes in the component are determined.
    # Since we iterate i from 1 to n, the first uncolored node i we encounter is the 
    # smallest index in its connected component.
    # To minimize the sequence lexicographically, we must set color[i] = 1.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS for the new component
            # Assign color 1 to the smallest index node in this component
            color[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_c = color[u]
                # The neighbor must have the opposite color
                target_c = 3 - current_c  # 1->2, 2->1
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = target_c
                        queue.append(v)
                    else:
                        # If neighbor is already colored, check for conflict
                        if color[v] != target_c:
                            print("NO")
                            return

    # If we finish without conflicts, a valid assignment exists
    print("YES")
    # Print the assignment sequence for nodes 1 to n
    # Using sys.stdout.write for efficiency with large output
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()