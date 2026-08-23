def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all possible colorings in lexicographical order
    # We use backtracking with pruning
    color = [0] * (n + 1)  # 0 means uncolored
    
    def is_valid(node, c):
        # Check if we can color node with color c
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for c in [1, 2, 3]:
            if is_valid(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0  # backtrack
        
        return False
    
    # This approach might be too slow for some cases
    # Let's use a more efficient approach with better ordering
    
    def solve_with_ordering():
        # Try coloring in order 1 to n
        for i in range(1, n + 1):
            found = False
            for c in [1, 2, 3]:
                valid = True
                for neighbor in adj[i]:
                    if neighbor < i and color[neighbor] == c:  # Only check already colored neighbors
                        valid = False
                        break
                if valid:
                    color[i] = c
                    found = True
                    break
            if not found:
                return False
        return True
    
    if solve_with_ordering():
        print("YES")
        print(*color[1:])
    else:
        print("NO")

solve()