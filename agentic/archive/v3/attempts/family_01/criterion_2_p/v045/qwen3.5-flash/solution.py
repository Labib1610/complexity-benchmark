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
    # Using 1-based indexing for modules 1 to n
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array to store the mode assignment
    # 0 represents unassigned, 1 represents Mode 1, 2 represents Mode 2
    color = [0] * (n + 1)
    
    # Iterate through all modules from 1 to n
    # This order ensures we process components and handle the lexicographical requirement
    for i in range(1, n + 1):
        if color[i] == 0:
            # If module i is not assigned, it belongs to a new connected component.
            # Since i is the smallest index in this component (as we iterate 1..n and skip visited),
            # assigning Mode 1 to i is the greedy choice to minimize the sequence lexicographically.
            color[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 3 - current_color  # Switch between 1 and 2
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] == current_color:
                        # Conflict detected: adjacent modules have the same mode
                        print("NO")
                        return
    
    # If no conflicts are found, print YES and the assignment
    print("YES")
    # Output the modes for modules 1 to n separated by spaces
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()