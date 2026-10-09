def solve():
    import sys
    from collections import defaultdict, deque
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # If no edges, any assignment works
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Try all possible 3-colorings using backtracking
    # But since n can be up to 40, we need a more efficient approach
    # However, since we only have 3 colors and the graph is not necessarily bipartite,
    # we can try a greedy approach or check if it's 3-colorable
    
    # Let's use a backtracking approach with optimizations
    color = [0] * (n + 1)  # 0 means uncolored
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        if color[node] != 0:
            return backtrack(node + 1)
            
        for c in [1, 2, 3]:
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        return False
    
    # Optimization: Start with nodes that have highest degree
    degrees = [(len(adj[i]), i) for i in range(1, n + 1)]
    degrees.sort(reverse=True)
    
    # Try to color the graph
    if backtrack(1):
        print("YES")
        print(" ".join(str(color[i]) for i in range(1, n + 1)))
    else:
        print("NO")

solve()