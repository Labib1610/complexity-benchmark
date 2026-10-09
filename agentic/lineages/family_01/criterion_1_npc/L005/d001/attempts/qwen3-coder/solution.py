def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    
    # Create adjacency list representation of the graph
    adj = [[] for _ in range(n+1)]
    index = 2
    for _ in range(m):
        u, v = int(data[index]), int(data[index+1])
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Color array to store the vault assignment (0 means unvisited)
    color = [0] * (n+1)
    
    # Try to 3-color the graph using DFS
    def dfs(node, c):
        color[node] = c
        for neighbor in adj[node]:
            if color[neighbor] == 0:
                if not dfs(neighbor, (c % 3) + 1):  # Cycle through colors 1, 2, 3
                    return False
            elif color[neighbor] == c:
                return False
        return True
    
    # Check each component of the graph
    for i in range(1, n+1):
        if color[i] == 0:
            if not dfs(i, 1):
                print("NO")
                return
    
    print("YES")
    print(*color[1:])

solve()