import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 = color 1, 2 = color 2
    color = [0] * (n + 1)
    
    # Check bipartiteness using BFS for each component
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque()
            queue.append(start)
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                neighbor_color = 3 - current_color  # flips 1->2 and 2->1
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = neighbor_color
                        queue.append(neighbor)
                    elif color[neighbor] != neighbor_color:
                        print("NO")
                        return
    
    # If we get here, the graph is bipartite
    print("YES")
    # For lexicographically smallest, we prefer color 1 when possible
    # Since we started with color 1 for component roots, this is already satisfied
    result = []
    for i in range(1, n + 1):
        result.append(str(color[i]))
    print(' '.join(result))

solve()