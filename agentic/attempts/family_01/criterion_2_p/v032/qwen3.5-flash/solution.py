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
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # Array to store the state of each unit (1 or 2), 0 means unvisited
    colors = [0] * (n + 1)
    
    # Iterate through all units to handle connected components.
    # We process units in increasing order of index (1 to n).
    # For each connected component, the first node we encounter (which is the smallest index in that component)
    # will be assigned state 1. This ensures that the resulting sequence (s_1, s_2, ..., s_n)
    # is lexicographically minimized because s_i is the first value contributed by the component
    # containing node i, and we prefer 1 over 2.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS from node i
            # We assign state 1 to i to minimize the sequence lexicographically
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_state = colors[u]
                required_state = 3 - current_state  # If u is 1, neighbor must be 2; if u is 2, neighbor must be 1
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = required_state
                        queue.append(v)
                    else:
                        # If neighbor is already visited, check for consistency
                        if colors[v] != required_state:
                            print("NO")
                            return

    # If we successfully assign states to all units without conflict
    print("YES")
    print(*(colors[1:]))

if __name__ == '__main__':
    solve()