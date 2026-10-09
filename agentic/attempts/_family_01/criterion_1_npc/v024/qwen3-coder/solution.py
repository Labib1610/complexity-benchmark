def solve():
    n, m = map(int, input().split())
    
    # Create adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to 3-color the graph
    color = [0] * (n + 1)  # 0 means uncolored, 1, 2, 3 are the colors
    
    def is_safe(node, c):
        # Check if color c is safe for node
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for c in range(1, 4):
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0  # backtrack
        
        return False
    
    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        print(*color[1:])
    else:
        print("NO")

solve()