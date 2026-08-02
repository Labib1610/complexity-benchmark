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

    # Adjacency list for the graph
    # Using 1-based indexing for convenience
    adj = [[] for _ in range(n + 1)]
    
    # Read m edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # Color array: 0 = uncolored, 1 = sector 1, 2 = sector 2
    color = [0] * (n + 1)
    
    # Iterate through all nodes to handle disconnected components.
    # To achieve the lexicographically smallest sequence (s_1, s_2, ..., s_n),
    # we want the earliest possible index to have the smallest possible sector (1).
    # Since components are independent, for each component, we can choose the bipartition orientation.
    # When we encounter the first uncolored node 'i' (which is the smallest index in its component),
    # we assign it sector 1. This is the optimal greedy choice for that position in the sequence.
    # This choice determines the colors for all other nodes in the component.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS for the component containing i
            color[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 3 - current_color # 3-1=2, 3-2=1
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] != next_color:
                        # Conflict detected: graph is not bipartite
                        print("NO")
                        return

    # If we successfully colored the graph without conflicts
    print("YES")
    # Output the assignments for 1 to n
    # Using sys.stdout.write for efficiency with large output
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()