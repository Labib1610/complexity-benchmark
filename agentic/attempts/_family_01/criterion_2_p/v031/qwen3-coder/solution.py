import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color each component using BFS
    colors = [0] * (n + 1)  # 0 means uncolored, 1 and 2 are colors
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
            
        # BFS to color this component
        queue = deque([start])
        colors[start] = 1
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            current_color = colors[node]
            next_color = 3 - current_color  # flips 1->2, 2->1
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    colors[neighbor] = next_color
                    queue.append(neighbor)
                elif colors[neighbor] != next_color:
                    print("NO")
                    return
    
    print("YES")
    result = []
    for i in range(1, n + 1):
        if colors[i] == 0:
            result.append("1")
        else:
            result.append(str(colors[i]))
    print(" ".join(result))

solve()