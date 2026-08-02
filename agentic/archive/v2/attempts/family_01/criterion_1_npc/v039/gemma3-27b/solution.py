def solve():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    def is_safe(node, color, assignment):
        for neighbor in adj[node]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True
    
    def backtrack(node, assignment):
        if node == n + 1:
            return True
        
        for color in range(1, 4):
            if is_safe(node, color, assignment):
                assignment[node] = color
                if backtrack(node + 1, assignment):
                    return True
                del assignment[node]
        
        return False
    
    assignment = {}
    if backtrack(1, assignment):
        result = [assignment[i] for i in range(1, n + 1)]
        print("YES")
        print(*result)
    else:
        print("NO")

solve()