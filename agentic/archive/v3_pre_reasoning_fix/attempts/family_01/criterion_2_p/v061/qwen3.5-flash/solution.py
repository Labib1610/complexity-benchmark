import sys
from collections import deque

def solve():
    # Read all input from standard input efficiently
    # sys.stdin.read().split() handles all whitespace (spaces, newlines)
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
    # Using 1-based indexing for devices 1 to n
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the segment assignment for each device
    # 0 represents unassigned, 1 represents segment 1, 2 represents segment 2
    colors = [0] * (n + 1)
    
    # Iterate through each device to handle disconnected components
    # We process devices in increasing order of index to ensure lexicographical minimality
    for i in range(1, n + 1):
        if colors[i] == 0:
            # If device i is unassigned, it starts a new connected component traversal.
            # To ensure the lexicographically smallest assignment sequence (s_1, s_2, ..., s_n),
            # we must assign the smallest possible valid color to the first unassigned device in the sequence.
            # Since i is the smallest index in this component (as we iterate 1..n and unvisited implies
            # no smaller index in the component), assigning segment 1 (color 1) is the greedy choice.
            colors[i] = 1
            queue = deque([i])
            
            # BFS to color the component and check for bipartiteness
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                next_color = 3 - current_color  # Toggle between 1 and 2
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] == current_color:
                        # Conflict detected: graph is not bipartite (contains odd cycle)
                        print("NO")
                        return

    # If no conflicts found, a valid assignment exists
    print("YES")
    # Output the assignment sequence s_1, s_2, ..., s_n
    sys.stdout.write(' '.join(map(str, colors[1:])) + '\n')

if __name__ == '__main__':
    solve()