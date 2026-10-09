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
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
    
    # Color the graph with 3 colors
    color = [0] * (n + 1)  # 0 means uncolored
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def graph_coloring(node):
        if node > n:
            return True
            
        for c in range(1, 4):  # Try colors 1, 2, 3
            if is_safe(node, c):
                color[node] = c
                if graph_coloring(node + 1):
                    return True
                color[node] = 0  # Backtrack
        
        return False
    
    # Start coloring from node 1
    if graph_coloring(1):
        print("YES")
        print(" ".join(map(str, color[1:])))
    else:
        print("NO")

solve()