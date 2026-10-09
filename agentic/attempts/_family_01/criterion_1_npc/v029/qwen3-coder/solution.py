def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(set)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Try to 3-color the graph
    color = [-1] * n  # -1 means uncolored, 0,1,2 are the three colors
    
    def is_valid(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        if color[node] != -1:
            return backtrack(node + 1)
            
        for c in range(3):
            if is_valid(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1
        
        return False
    
    # Start with node 0 colored with 0
    color[0] = 0
    if backtrack(1):
        print("YES")
        print(" ".join(str(c + 1) for c in color))
    else:
        # Try starting with other colors for node 0
        color[0] = -1
        found = False
        for c in range(3):
            color[0] = c
            if backtrack(1):
                print("YES")
                print(" ".join(str(c + 1) for c in color))
                found = True
                break
            color[0] = -1
        
        if not found:
            print("NO")

solve()