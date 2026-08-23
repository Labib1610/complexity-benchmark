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
    # Using 1-based indexing for workers
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the shift assignment (1 or 2). 0 means unvisited.
    s = [0] * (n + 1)
    
    # Iterate through each worker to handle connected components
    # We process workers in increasing order of their index to ensure
    # lexicographically smallest assignment.
    for i in range(1, n + 1):
        if s[i] == 0:
            # i is the smallest index in its connected component.
            # To minimize the assignment lexicographically, we must assign shift 1 to i.
            # Then we propagate constraints to the rest of the component.
            s[i] = 1
            q = deque([i])
            
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if s[v] == 0:
                        # Assign opposite shift
                        s[v] = 3 - s[u]
                        q.append(v)
                    elif s[v] == s[u]:
                        # Conflict detected: the graph is not bipartite
                        print("NO")
                        return

    # If we complete the traversal without conflicts, a valid assignment exists
    print("YES")
    # Output the assignment for workers 1 to n
    # Using sys.stdout.write for faster output handling
    sys.stdout.write(' '.join(map(str, s[1:])) + '\n')

if __name__ == '__main__':
    solve()