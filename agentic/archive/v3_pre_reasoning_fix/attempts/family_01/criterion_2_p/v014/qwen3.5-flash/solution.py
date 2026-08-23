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

    # Array to store the period assignment (0: unassigned, 1: period 1, 2: period 2)
    assignment = [0] * (n + 1)
    
    # Iterate through each staff member to process connected components
    # We want the lexicographically smallest sequence, so for each unassigned component,
    # we start coloring from the smallest index in that component with period 1.
    for i in range(1, n + 1):
        if assignment[i] != 0:
            continue
        
        # Start BFS for the component containing i
        assignment[i] = 1
        queue = deque([i])
        
        while queue:
            u = queue.popleft()
            current_color = assignment[u]
            next_color = 3 - current_color  # Switch between 1 and 2
            
            for v in adj[u]:
                if assignment[v] == 0:
                    assignment[v] = next_color
                    queue.append(v)
                elif assignment[v] == current_color:
                    # Conflict detected: adjacent vertices have the same color
                    print("NO")
                    return

    # If we successfully colored the entire graph
    print("YES")
    # Output the assignment for staff 1 to n
    sys.stdout.write(" ".join(map(str, assignment[1:])) + "\n")

if __name__ == '__main__':
    solve()