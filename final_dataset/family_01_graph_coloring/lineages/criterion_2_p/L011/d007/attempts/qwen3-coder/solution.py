import sys
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 means unvisited, 1 and 2 are the two colors
    color = [0] * n
    visited = [False] * n
    
    # Check each component
    for i in range(n):
        if not visited[i]:
            # BFS to check bipartiteness
            queue = deque()
            queue.append(i)
            color[i] = 1
            visited[i] = True
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 2 if current_color == 1 else 1
                
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        print("NO")
                        return
    
    # If we reach here, a valid assignment exists
    # We want the lexicographically smallest one
    # That means we prefer p_i = 1 over p_i = 2
    # In our coloring, we can map color 1 -> 1 and color 2 -> 2
    result = []
    for c in color:
        result.append(str(c))
    
    print("YES")
    print(' '.join(result))

solve()