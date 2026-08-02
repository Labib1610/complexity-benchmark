import sys
from collections import deque

def solve():
    # Use fast I/O by reading all input at once
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
    
    # Read m edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the schedule for each worker (0: unassigned, 1: Schedule 1, 2: Schedule 2)
    color = [0] * (n + 1)
    
    # We need to find a valid 2-coloring (bipartite check) that is lexicographically smallest.
    # We iterate through workers from 1 to n.
    # If a worker i is uncolored, it means we have encountered a new connected component.
    # Since we iterate in increasing order, i is the smallest index in this component.
    # To minimize the lexicographical order of the schedule sequence (s_1, s_2, ..., s_n),
    # we must assign the smallest possible value to s_i. Thus, we set color[i] = 1.
    # This choice propagates to all other nodes in the component.
    # If we encounter a conflict during propagation, the graph is not bipartite.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                c = color[u]
                # The neighbor must have the opposite color (1 -> 2, 2 -> 1)
                next_c = 3 - c
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_c
                        queue.append(v)
                    elif color[v] != next_c:
                        # Conflict detected: adjacent nodes have the same color
                        print("NO")
                        return

    # If we successfully assigned schedules for all workers
    print("YES")
    # Output the schedules separated by space
    # Using sys.stdout.write for efficiency with large output
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()