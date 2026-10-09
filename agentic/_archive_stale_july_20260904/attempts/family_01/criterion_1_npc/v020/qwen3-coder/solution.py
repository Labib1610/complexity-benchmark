def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list for incompatibilities
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    # Try all 3^n assignments, but we can do better with backtracking
    # For small n (up to 40) and only 3 colors, we need an efficient approach
    
    # Actually, since n <= 40 and we have 3 colors, let's try greedy with backtracking
    # But even better - let's try all assignments in lexicographical order
    
    # Since 3^40 is too large, we need to be smarter
    # This is essentially a 3-coloring problem
    
    # Let's use backtracking with constraint checking
    assignment = [0] * (n + 1)
    
    def is_valid(node, color):
        for neighbor in adj[node]:
            if assignment[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True
            
        for color in [1, 2, 3]:
            if is_valid(node, color):
                assignment[node] = color
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        return False
    
    # Special case: if there are no edges, just assign all to 1
    if m == 0:
        result = [1] * n
        print("YES")
        print(' '.join(map(str, result)))
        return
    
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, assignment[1:])))
    else:
        print("NO")

solve()