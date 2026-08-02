import sys
from collections import deque

def solve():
    # Read all input from standard input at once for efficiency
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
    # Sensors are 1-indexed
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the channel assignment for each sensor
    # 0: unassigned, 1: channel 1, 2: channel 2
    colors = [0] * (n + 1)
    
    # Iterate through each sensor from 1 to n
    for i in range(1, n + 1):
        if colors[i] == 0:
            # If sensor i is not assigned, it belongs to a new connected component.
            # Since we iterate in increasing order, i is the smallest index in this component.
            # To achieve the lexicographically smallest sequence, we must assign channel 1 to i.
            colors[i] = 1
            queue = deque([i])
            
            # Perform BFS to color the entire component
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                next_color = 3 - current_color  # 3 - 1 = 2, 3 - 2 = 1
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] == current_color:
                        # If a neighbor has the same color, the graph is not bipartite
                        print("NO")
                        return
    
    # If we successfully colored all sensors without conflicts
    print("YES")
    # Output the sequence s_1, s_2, ..., s_n
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()