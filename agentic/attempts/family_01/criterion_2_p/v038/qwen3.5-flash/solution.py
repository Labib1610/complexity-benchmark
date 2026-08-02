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
        
    # Color array: 0 = uncolored, 1 = period 1, 2 = period 2
    color = [0] * (n + 1)
    
    # Iterate through each staff member to handle connected components
    # We process nodes in increasing order of index (1 to n).
    # For each uncolored node i, it belongs to a connected component.
    # Since i is the smallest index in its component (otherwise it would have been colored),
    # we must assign s_i = 1 to ensure the lexicographically smallest sequence.
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            q = deque([i])
            
            while q:
                u = q.popleft()
                current_color = color[u]
                required_color = 3 - current_color # Flip between 1 and 2
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = required_color
                        q.append(v)
                    elif color[v] != required_color:
                        # Conflict detected: graph is not bipartite
                        print("NO")
                        return

    # If we successfully colored all nodes without conflict
    print("YES")
    # Output the sequence s_1, s_2, ..., s_n
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()