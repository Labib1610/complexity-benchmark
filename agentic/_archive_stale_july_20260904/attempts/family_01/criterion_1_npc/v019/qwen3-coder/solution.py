def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Try all possible colorings starting from the first domain
    # We want the lexicographically smallest solution
    colors = [0] * (n + 1)  # 0 means uncolored
    
    def is_valid(node, color):
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for color in [1, 2, 3]:
            if is_valid(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0
        return False
    
    # Check if a valid coloring exists
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, colors[1:])))
    else:
        print("NO")

solve()