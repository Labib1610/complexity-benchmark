import sys
from collections import deque

# Increase recursion depth just in case, though we use iterative BFS.
sys.setrecursionlimit(300000)

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    # Create an iterator to traverse the input data
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return
    
    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    
    # Read m edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # Array to store the shift assignment for each worker (1 or 2)
    # 0 indicates unassigned
    shift = [0] * (n + 1)
    
    # Iterate through all workers to ensure all connected components are processed
    # Since we want the lexicographically smallest assignment, we prefer shift 1.
    # We process components in the order of their smallest node index.
    # For each component, we start with the smallest unvisited node and assign it shift 1.
    # If the component is bipartite, this determines the whole component uniquely.
    # If not bipartite, no solution exists.
    
    for i in range(1, n + 1):
        if shift[i] != 0:
            continue
        
        # Start BFS from node i
        shift[i] = 1
        queue = deque([i])
        
        while queue:
            u = queue.popleft()
            current_shift = shift[u]
            next_shift = 3 - current_shift  # Flip between 1 and 2
            
            for v in adj[u]:
                if shift[v] == 0:
                    shift[v] = next_shift
                    queue.append(v)
                elif shift[v] != next_shift:
                    # Conflict detected: adjacent nodes have the same shift
                    print("NO")
                    return

    # If we successfully assigned shifts to all workers
    print("YES")
    # Output the shifts for workers 1 to n
    print(" ".join(map(str, shift[1:])))

if __name__ == '__main__':
    solve()