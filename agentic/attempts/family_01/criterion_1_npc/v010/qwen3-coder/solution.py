def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color the graph with 3 colors (1, 2, 3)
    # Try to find a valid 3-coloring that is lexicographically smallest
    color = [0] * (n + 1)  # color[i] is the color of worker i
    
    def is_valid(node, c):
        # Check if we can assign color c to node
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
                # No need to undo since we return immediately when found
        return False
    
    # Try to color nodes in order 1, 2, ..., n to get lexicographically smallest
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, color[1:])))
    else:
        print("NO")

solve()