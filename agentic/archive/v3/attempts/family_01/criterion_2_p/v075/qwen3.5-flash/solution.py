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

    # Build adjacency list
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
        
    # Array to store the shift assignment for each technician
    # 0: unassigned, 1: shift 1, 2: shift 2
    colors = [0] * (n + 1)
    
    # Iterate through each node from 1 to n to process connected components.
    # The loop order ensures that for each component, the smallest index node
    # (which appears first in the sequence) is processed first.
    # To achieve the lexicographically smallest sequence, we must assign shift 1
    # to the smallest index node of each component.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Found a new component.
            # Assign shift 1 to the first node encountered (smallest index in component).
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_c = colors[u]
                next_c = 3 - current_c # 1 -> 2, 2 -> 1
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_c
                        queue.append(v)
                    elif colors[v] == current_c:
                        # Conflict detected: adjacent nodes have the same color
                        print("NO")
                        return

    print("YES")
    # Print the assignment sequence s_1, s_2, ..., s_n
    print(*(colors[1:]))

if __name__ == '__main__':
    solve()