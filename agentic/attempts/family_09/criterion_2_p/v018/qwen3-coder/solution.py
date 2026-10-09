import sys
from collections import defaultdict, deque

def solve():
    n, m, k = map(int, input().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Bipartite graph coloring
    color = [-1] * (n + 1)  # -1: unvisited, 0: color A, 1: color B
    partition = [[], []]  # partition[0] for color 0, partition[1] for color 1
    
    # Check each connected component
    for start in range(1, n + 1):
        if color[start] == -1:  # unvisited node
            queue = deque([start])
            color[start] = 0
            partition[0].append(start)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 1 - current_color
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = next_color
                        partition[next_color].append(neighbor)
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # This shouldn't happen according to problem constraints
                        # but let's handle it gracefully
                        print("NO")
                        return
    
    # Try to select k nodes with no edges between them
    # Since the graph is bipartite, we can select all nodes from one partition
    # as long as that partition has at least k nodes
    
    if len(partition[0]) >= k:
        print("YES")
        print(*partition[0][:k])
    elif len(partition[1]) >= k:
        print("YES")
        print(*partition[1][:k])
    else:
        print("NO")

solve()