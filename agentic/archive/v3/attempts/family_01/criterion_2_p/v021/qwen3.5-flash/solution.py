<code>
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
    # Nodes are 1-indexed
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Color array: 0 = uncolored, 1 = channel 1, 2 = channel 2
    color = [0] * (n + 1)
    
    # Iterate through all nodes to handle connected components
    # Processing in order 1 to n ensures we make lexicographically smallest choices
    # because for each component, the first node encountered (smallest index) gets color 1.
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS for the component containing i
            # Assign channel 1 to i to minimize lexicographically
            color[i] = 1
            q = deque([i])
            
            while q:
                u = q.popleft()
                current_color = color[u]
                next_color = 2 if current_color == 1 else 1
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_color
                        q.append(v)
                    elif color[v] == current_color:
                        # Conflict: adjacent nodes have same color -> Not bipartite
                        print("NO")
                        return
    
    # Valid assignment found
    print("YES")
    print(' '.join(map(str, color[1:])))

if __name__ == '__main__':
    solve()
</code>