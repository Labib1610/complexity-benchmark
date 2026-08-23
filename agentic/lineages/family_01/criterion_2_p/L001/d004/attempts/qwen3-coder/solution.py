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
    
    # Check if bipartite and find lexicographically smallest coloring
    for start in range(1, n + 1):
        if color[start] == 0:
            # BFS to color component
            queue = deque()
            queue.append((start, 1))  # node, color
            color[start] = 1
            
            while queue:
                node, c = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - c  # Flip color (1->2, 2->1)
                        queue.append((neighbor, 3 - c))
                    elif color[neighbor] == c:
                        print("NO")
                        return
    
    # If we get here, a valid coloring exists
    # To get lexicographically smallest, we prefer color 1 (coordinate 1) 
    # for each node if possible. Since our BFS already ensures a valid 2-coloring,
    # and we start with color 1 for the first node in each component, 
    # this gives us one valid solution. But to ensure lexicographically 
    # smallest, we need to verify our coloring approach.
    
    # Actually, our BFS starting from the lowest index node and always 
    # assigning the first available color (1) to unvisited nodes will 
    # produce the lexicographically smallest result.
    
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == 1:
            result.append("1")
        else:
            result.append("2")
    print(" ".join(result))

solve()