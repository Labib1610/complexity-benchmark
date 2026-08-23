def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list representation of conflicts
    adj = [[] for _ in range(n+1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    # Color the graph with 3 colors (1, 2, 3). This is a backtracking solution.
    # We'll use a greedy backtracking approach, trying colors 1,2,3 in order 
    # to ensure lexicographically smallest result.
    
    color = [0] * (n+1)  # color[i] represents the bank for block i
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for c in [1, 2, 3]:
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        return False
    
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, color[1:])))
    else:
        print("NO")

solve()