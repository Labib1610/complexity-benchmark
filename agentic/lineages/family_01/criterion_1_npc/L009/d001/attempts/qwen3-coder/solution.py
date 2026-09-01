def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Create adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all 3-colorings
    color = [0] * n  # 0 means uncolored
    
    def is_valid(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        # Try colors 1, 2, 3 in order for lexicographically smallest result
        for c in range(1, 4):
            if is_valid(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0  # Backtrack
                
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()