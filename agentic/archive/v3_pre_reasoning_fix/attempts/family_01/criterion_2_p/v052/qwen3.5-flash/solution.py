import sys
from collections import deque

def solve():
    # Use sys.stdin.read to read all input at once for performance
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list to represent the graph
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
    
    # Array to store the channel assignment for each node
    # 0: unassigned, 1: channel 1, 2: channel 2
    color = [0] * (n + 1)
    
    # Iterate through all nodes from 1 to n.
    # This order ensures that for any connected component, the node with the smallest index
    # is the first one encountered. We assign it channel 1, which is lexicographically smallest.
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS traversal for the connected component containing i
            # To minimize lexicographically, we must assign the smallest available channel (1)
            # to the first node of the component (which is i, since we iterate 1..n).
            color[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 3 - current_color  # Toggle between 1 and 2 (1->2, 2->1)
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] == current_color:
                        # Conflict found: adjacent nodes have the same color
                        # This implies the graph is not bipartite
                        print("NO")
                        return
    
    # If the loop completes without conflicts, a valid assignment exists
    print("YES")
    # Print the assignments for nodes 1 to n as space-separated integers
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()