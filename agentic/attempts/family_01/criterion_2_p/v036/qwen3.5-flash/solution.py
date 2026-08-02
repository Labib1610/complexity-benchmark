import sys
from collections import deque

# Increase recursion depth just in case, though we use iterative approach.
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

    # Build adjacency list
    # Using 1-based indexing for convenience
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
        
    # Array to store zone assignments: 0 = unvisited, 1 = Zone 1, 2 = Zone 2
    colors = [0] * (n + 1)
    
    # Iterate through each worker to handle disconnected components
    # We iterate from 1 to n to ensure we process nodes in increasing order of index.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Found a new component.
            # To achieve the lexicographically smallest sequence s_1, s_2, ..., s_n,
            # we must assign the smallest index node in the component to Zone 1.
            # Since we iterate i from 1 to n, 'i' is the smallest index 
            # in this component that hasn't been visited yet.
            colors[i] = 1
            
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                # The other zone must be 3 - c (since 3-1=2, 3-2=1)
                next_color = 3 - current_color
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] == current_color:
                        # Bipartite check failed: adjacent nodes have the same color
                        print("NO")
                        return

    # If we successfully colored all components
    print("YES")
    # Output the assignment for workers 1 to n
    # Using sys.stdout.write with join for efficiency
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()