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
    # Nodes are 1-indexed, so we use size n + 1
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
        
    # Array to store the unit assignment for each compound (1 or 2)
    # 0 indicates not yet assigned
    color = [0] * (n + 1)
    
    # Iterate through each compound from 1 to n to handle all connected components
    # We process nodes in increasing order to ensure lexicographically smallest sequence.
    for i in range(1, n + 1):
        if color[i] == 0:
            # If compound i is not assigned, it's a new component.
            # To achieve the lexicographically smallest sequence, we must assign unit 1 to the 
            # first node of the component encountered (which is i).
            # This determines the rest of the component's coloring.
            color[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_unit = color[u]
                next_unit = 3 - current_unit # If 1 then 2, if 2 then 1
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_unit
                        queue.append(v)
                    elif color[v] != next_unit:
                        # If neighbor is already assigned to the same unit, it's impossible
                        # to satisfy the condition (graph is not bipartite)
                        print("NO")
                        return

    # If we successfully assigned units to all compounds
    print("YES")
    # Print the sequence s_1, s_2, ..., s_n
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()