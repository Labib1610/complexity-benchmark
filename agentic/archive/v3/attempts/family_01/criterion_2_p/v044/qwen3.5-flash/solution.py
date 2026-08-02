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

    # Build the graph using an adjacency list
    # Stations are 1-indexed, so size is n + 1
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the channel assignment for each station
    # 0: unassigned, 1: Channel 1, 2: Channel 2
    colors = [0] * (n + 1)
    
    # Iterate through all stations to handle disconnected components
    # Since we want the lexicographically smallest sequence, we iterate i from 1 to n.
    # For each unvisited component, the first node encountered (which is i) is the 
    # smallest index in that component. To minimize the sequence, we assign Channel 1 to it.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS for the connected component containing i
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                # The color for neighbors must be the opposite (1->2, 2->1)
                next_color = 3 - current_color
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] == current_color:
                        # Conflict detected: adjacent stations have same channel
                        # This means the graph is not bipartite
                        print("NO")
                        return

    # If no conflicts found, print YES and the assignment
    print("YES")
    # Output the sequence of channels for stations 1 to n
    # Using sys.stdout.write for efficient output of the large array
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()