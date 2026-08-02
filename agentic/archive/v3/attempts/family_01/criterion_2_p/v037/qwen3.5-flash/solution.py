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

    # Build the graph using adjacency list
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the shift for each person (1 or 2), 0 means unassigned
    shift = [0] * (n + 1)
    
    # Iterate through all personnel to handle disconnected components
    # The loop order 1 to n ensures we process the lexicographically smallest
    # unassigned node first for each component.
    for i in range(1, n + 1):
        if shift[i] == 0:
            # Start a new component traversal (BFS)
            # To ensure lexicographically smallest assignment, we assign shift 1
            # to the first node encountered in this component.
            shift[i] = 1
            q = deque([i])
            
            while q:
                u = q.popleft()
                current_shift = shift[u]
                # Neighbors must have the opposite shift (3 - shift)
                target_shift = 3 - current_shift
                
                for v in adj[u]:
                    if shift[v] == 0:
                        shift[v] = target_shift
                        q.append(v)
                    elif shift[v] != target_shift:
                        # Incompatible pair assigned the same shift -> Impossible
                        print("NO")
                        return

    # If we successfully assigned shifts to all personnel
    print("YES")
    # Print the assignments separated by spaces
    sys.stdout.write(" ".join(map(str, shift[1:])) + "\n")

if __name__ == '__main__':
    solve()