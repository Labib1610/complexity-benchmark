import sys
from collections import deque

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for the graph (1-based indexing)
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Color array: 0 = uncolored, 1 = team 1, 2 = team 2
    color = [0] * (n + 1)
    
    # Iterate through all nodes 1 to n.
    # This ensures we process each connected component.
    # By processing in increasing order of indices, we can enforce
    # the lexicographically smallest assignment.
    # For any component, the node with the smallest index encountered
    # determines the assignment for the whole component.
    # We always choose '1' for this node to ensure lexicographical minimality.
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS from node i
            color[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_c = color[u]
                next_c = 3 - current_c  # Toggle between 1 and 2
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_c
                        queue.append(v)
                    elif color[v] == current_c:
                        # Conflict detected: Not a bipartite graph
                        print("NO")
                        return

    # If no conflicts found, output YES and the assignment
    print("YES")
    # Join the colors for output
    sys.stdout.write(' '.join(map(str, color[1:])) + '\n')

if __name__ == '__main__':
    solve()