def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list for the graph
    adj = defaultdict(set)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
    
    # Try to 3-color the graph with backtracking, minimizing lex order
    color = [0] * (n + 1)  # color[i] represents the tier of module i
    
    def is_safe(node, c):
        """Check if we can assign color c to node"""
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        """Try to color nodes from 'node' to n, return True if possible"""
        if node > n:
            return True
            
        for c in [1, 2, 3]:
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                # No need to unassign since we'll overwrite or finish
        
        return False
    
    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        print(*color[1:])
    else:
        print("NO")

solve()