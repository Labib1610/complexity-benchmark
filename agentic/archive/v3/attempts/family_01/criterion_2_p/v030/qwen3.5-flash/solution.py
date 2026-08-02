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
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store colors (modes) for each person
    # 0: uncolored, 1: Mode 1, 2: Mode 2
    colors = [0] * (n + 1)
    
    # Iterate through all personnel from 1 to n
    # This ensures we process each connected component and handle the lexicographical requirement
    for i in range(1, n + 1):
        if colors[i] == 0:
            # If person i is uncolored, they belong to a new connected component.
            # To achieve the lexicographically smallest assignment, we assign Mode 1
            # to the first uncolored person encountered in the component (which is i).
            # Since i is the smallest index in this component (due to loop order),
            # setting colors[i] = 1 minimizes the sequence globally.
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                # The neighbor must have the opposite mode (1 -> 2, 2 -> 1)
                next_color = 3 - current_color
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] == current_color:
                        # Conflict detected: adjacent nodes have the same mode.
                        # The graph is not bipartite, so no valid assignment exists.
                        print("NO")
                        return

    # If we reach here, a valid assignment exists
    print("YES")
    # Print the assignment sequence
    # Using sys.stdout.write for faster output with large N
    sys.stdout.write(" ".join(map(str, colors[1:])) + "\n")

if __name__ == '__main__':
    solve()