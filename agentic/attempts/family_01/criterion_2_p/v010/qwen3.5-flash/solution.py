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
    # Nodes are 1-indexed, so size is n + 1
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the team assignment
    # 0: unvisited, 1: Team 1, 2: Team 2
    color = [0] * (n + 1)
    
    # Iterate through all nodes to handle disconnected components
    # We want the lexicographically smallest assignment.
    # Since we iterate i from 1 to n, the first unvisited node i we encounter
    # is the smallest index in its connected component.
    # To minimize the sequence lexicographically, we must assign Team 1 to this node
    # if possible (since 1 < 2). If the component is bipartite, both assignments
    # (starting with 1 or 2) are valid, so we choose the one starting with 1.
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS for the component containing i
            color[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                
                # The color for neighbors must be the opposite of u's color
                # If u is 1, neighbor is 2. If u is 2, neighbor is 1.
                next_c = 3 - color[u]
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_c
                        queue.append(v)
                    elif color[v] == color[u]:
                        # Conflict detected: adjacent nodes have the same team
                        # This implies the graph is not bipartite
                        print("NO")
                        return
    
    # If we successfully processed all nodes without conflicts
    print("YES")
    # Output the assignments for nodes 1 to n
    print(" ".join(map(str, color[1:])))

if __name__ == '__main__':
    solve()