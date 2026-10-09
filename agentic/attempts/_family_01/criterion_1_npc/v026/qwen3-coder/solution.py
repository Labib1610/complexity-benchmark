def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list for the graph
    adj = defaultdict(set)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # If no edges, we can assign all to frequency 1
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Try to 3-color the graph using backtracking
    color = [0] * (n + 1)  # color[i] represents the frequency for stream i
    
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
            
        for c in range(1, 4):
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        return False
    
    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        result = []
        for i in range(1, n + 1):
            result.append(str(color[i]))
        print(" ".join(result))
    else:
        print("NO")

solve()