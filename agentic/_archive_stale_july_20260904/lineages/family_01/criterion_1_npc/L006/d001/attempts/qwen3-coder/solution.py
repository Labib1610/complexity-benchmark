def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u, v = int(data[idx]), int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    # Try to color the graph with 3 colors (1, 2, 3)
    # We want the lexicographically smallest assignment
    color = [0] * (n + 1)
    
    def is_valid(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for c in range(1, 4):
            if is_valid(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        return False
    
    # Since we want lexicographically smallest, we just try colors 1,2,3 in order
    # for each node in sequence 1 to n. This is exactly what our backtrack does.
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, color[1:])))
    else:
        print("NO")

solve()