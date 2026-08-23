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
    # 1-based indexing for employees
    adj = [[] for _ in range(n + 1)]
    
    # Read m edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the shift assignment (1 or 2)
    # 0 indicates unassigned
    color = [0] * (n + 1)
    
    # Iterate through all employees to handle disconnected components
    # We process nodes in increasing order of index to ensure lexicographically smallest assignment
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS from employee i
            # We assign shift 1 to i to ensure lexicographically smallest sequence
            # because i is the smallest index in this component (unvisited nodes are processed in order)
            color[i] = 1
            q = deque([i])
            
            while q:
                u = q.popleft()
                current_shift = color[u]
                next_shift = 3 - current_shift  # Switch between 1 and 2
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_shift
                        q.append(v)
                    elif color[v] == current_shift:
                        # Conflict found: two incompatible employees assigned to same shift
                        print("NO")
                        return

    # If we successfully assign shifts to all employees
    print("YES")
    # Output the assignments
    # Using sys.stdout.write for efficiency with large output
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()