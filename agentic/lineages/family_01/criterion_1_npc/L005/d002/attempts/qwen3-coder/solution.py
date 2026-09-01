def solve():
    import sys
    from collections import defaultdict
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
    adj = defaultdict(list)
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-indexed
        v = int(data[idx+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    # Try to color the graph with 3 colors using backtracking
    # Colors: 1, 2, 3 (we'll use 0, 1, 2 internally and add 1 at the end)
    color = [-1] * n
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        for c in range(3):  # Try colors 0, 1, 2
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1
        return False
    
    # Start backtracking from node 0
    if not backtrack(0):
        print("NO")
        return
    
    # Convert colors to 1-indexed
    result = [str(c + 1) for c in color]
    print("YES")
    print(" ".join(result))

solve()