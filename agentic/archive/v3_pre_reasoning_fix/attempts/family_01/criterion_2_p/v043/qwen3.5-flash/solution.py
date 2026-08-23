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
    # Using 0-based indexing for nodes 0 to n-1
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
        
    # Colors array: 0 = unvisited, 1 = Shift 1, 2 = Shift 2
    colors = [0] * n
    
    # Iterate through all personnel to handle disconnected components
    for i in range(n):
        if colors[i] == 0:
            # Start BFS for the connected component containing i
            # To achieve lexicographically smallest assignment, we assign Shift 1 
            # to the smallest index node in the component (which is 'i' since we iterate 0 to n-1).
            colors[i] = 1
            q = deque([i])
            
            while q:
                u = q.popleft()
                current_color = colors[u]
                neighbor_color = 3 - current_color  # Toggle between 1 and 2
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = neighbor_color
                        q.append(v)
                    elif colors[v] != neighbor_color:
                        # Conflict detected: adjacent nodes have the same shift
                        print("NO")
                        return
    
    print("YES")
    # Print the resulting shifts as space-separated integers
    print(" ".join(map(str, colors)))

if __name__ == '__main__':
    solve()