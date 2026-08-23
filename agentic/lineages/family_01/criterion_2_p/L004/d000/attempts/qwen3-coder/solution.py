import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 = zone 1, 2 = zone 2
    color = [0] * (n + 1)
    
    # Check each component
    for start in range(1, n + 1):
        if color[start] == 0:  # Unvisited node
            # BFS to color this component
            queue = deque([start])
            color[start] = 1  # Start with zone 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                # Check all neighbors
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        # Color with opposite color
                        color[neighbor] = 3 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Conflict found
                        print("NO")
                        return
    
    # If we get here, a valid assignment exists
    print("YES")
    # For lexicographically smallest, we want first node to be in zone 1
    # If first node was assigned zone 2, we need to flip all assignments
    if color[1] == 2:
        # Flip all colors
        for i in range(1, n + 1):
            color[i] = 3 - color[i]
    
    print(' '.join(map(str, color[1:])))

solve()