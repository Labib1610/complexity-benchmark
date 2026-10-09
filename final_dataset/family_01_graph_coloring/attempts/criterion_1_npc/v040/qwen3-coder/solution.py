def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to 3-color the graph
    color = [0] * (n + 1)  # 0 means uncolored, 1, 2, 3 are colors
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        if color[node] != 0:
            return backtrack(node + 1)
            
        for c in range(1, 4):
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
                
        return False
    
    # Handle disconnected components
    visited = [False] * (n + 1)
    
    def dfs(v):
        visited[v] = True
        component.append(v)
        for u in adj[v]:
            if not visited[u]:
                dfs(u)
    
    # Process each connected component
    for i in range(1, n + 1):
        if not visited[i] and adj[i]:  # Non-isolated node
            component = []
            dfs(i)
            
            # Try to color this component
            old_color = color[:]
            if not backtrack(min(component)):
                print("NO")
                return
            # Verify the coloring worked
            valid = True
            for u, v in edges:
                if color[u] == color[v] and color[u] != 0:
                    valid = False
                    break
            if not valid:
                print("NO")
                return
    
    # Assign color 1 to isolated nodes (nodes with no edges)
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
    
    print("YES")
    print(" ".join(map(str, color[1:])))

solve()