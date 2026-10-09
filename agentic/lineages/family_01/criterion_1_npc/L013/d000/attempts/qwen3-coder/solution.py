def solve():
    n, m = map(int, input().split())
    
    # Create adjacency list representation of the graph
    # where each employee is a node and incompatible pairs are edges
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to 3-color the graph
    # color[i] will be 0 if unassigned, or 1, 2, 3 for the three periods
    color = [0] * (n + 1)
    
    def is_safe(node, c):
        # Check if we can assign color c to node
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
    
    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        print(*color[1:])
    else:
        print("NO")

solve()