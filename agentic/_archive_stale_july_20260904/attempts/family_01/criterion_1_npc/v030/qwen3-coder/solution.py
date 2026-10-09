def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # We need to find a valid 3-coloring that is lexicographically smallest
    # We'll try all 3^n combinations, but in lexicographical order
    # Since n <= 40, but 3^40 is too large, we need a smarter approach
    
    # Actually, let's use backtracking with constraint propagation
    # and always try colors in order 1,2,3 to ensure lexicographical minimality
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to color the graph with 3 colors
    color = [0] * n  # 0 means uncolored
    
    def is_valid(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        
        for c in [1, 2, 3]:
            if is_valid(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

solve()