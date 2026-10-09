def solve():
    n, m = map(int, input().split())
    
    # Create adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to color the graph with 3 colors
    # Colors: 0 = unassigned, 1, 2, 3 = shifts
    color = [0] * (n + 1)
    
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
                color[node] = 0
        
        return False
    
    # Since max degree is 39 and we have 40 nodes, 
    # and each node has at most 39 conflicts,
    # a valid 3-coloring should exist if possible.
    
    if backtrack(1):
        print("YES")
        print(*color[1:])
    else:
        print("NO")

solve()