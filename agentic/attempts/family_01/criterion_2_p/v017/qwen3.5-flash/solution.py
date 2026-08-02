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
    # Workers are 1-indexed
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # colors[i] stores the shift of worker i
    # 0: unvisited, 1: Shift 1, 2: Shift 2
    colors = [0] * (n + 1)
    
    # Iterate through all workers to handle disconnected components
    # We iterate from 1 to n to ensure we process components in lexicographical order
    # of their first member.
    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS for the new connected component
            # To achieve the lexicographically smallest sequence s_1, ..., s_n,
            # we must assign the smallest possible shift to the first worker
            # encountered in the component (which is 'i' since we iterate 1..n).
            # The smallest shift is 1.
            colors[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = colors[u]
                next_color = 3 - current_color  # If current is 1, next is 2; if 2, next is 1
                
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = next_color
                        queue.append(v)
                    elif colors[v] == current_color:
                        # Conflict detected: adjacent workers have the same shift
                        # This means the graph is not bipartite
                        print("NO")
                        return

    # If we finish without conflicts, a valid assignment exists
    print("YES")
    # Print the shift assignments for workers 1 to n
    print(" ".join(map(str, colors[1:])))

if __name__ == '__main__':
    solve()