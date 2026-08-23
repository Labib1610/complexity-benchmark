import sys
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
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
    
    # Check if bipartite for each connected component
    for i in range(n):
        if color[i] == 0:
            queue = deque()
            queue.append(i)
            color[i] = 1  # Start coloring with 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 3 - current_color  # Switch between 1 and 2
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        print("NO")
                        return
    
    # Verify all edges satisfy the constraint
    for u, v in edges:
        if color[u] + color[v] != 3:
            print("NO")
            return
    
    print("YES")
    # Convert back to 1-indexed values for output
    result = [str(c) for c in color]
    print(" ".join(result))

solve()