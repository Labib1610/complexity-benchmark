def solve():
    import sys
    from collections import defaultdict, deque
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
    adj = defaultdict(list)
    index = 2
    edges = []
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        index += 2
    
    # Try all 3^n combinations in lexicographical order using backtracking
    # But since n can be up to 40, we need a more efficient approach
    # This is a graph coloring problem with 3 colors where adjacent nodes must have different colors
    # We can use backtracking with pruning
    
    # Since n <= 40, and it's a graph coloring problem, let's try to model it properly
    # We'll use backtracking with constraint propagation
    
    color = [-1] * n  # -1 means unassigned
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        for c in [1, 2, 3]:
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1
        return False
    
    # For better performance, we should process nodes in a smart order
    # Let's sort nodes by degree descending (most constrained first)
    degrees = [(len(adj[i]), i) for i in range(n)]
    degrees.sort(reverse=True)
    order = [x[1] for x in degrees]
    
    # Reorder the search
    color_order = [-1] * n
    
    def is_safe_order(pos, c):
        node = order[pos]
        for neighbor in adj[node]:
            if color_order[neighbor] == c:
                return False
        return True
    
    def backtrack_order(pos):
        if pos == n:
            return True
            
        node = order[pos]
        for c in [1, 2, 3]:
            if is_safe_order(pos, c):
                color_order[node] = c
                if backtrack_order(pos + 1):
                    return True
                color_order[node] = -1
        return False
    
    if m == 0:
        # No constraints, all 1s
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Check if the graph is 3-colorable
    if backtrack_order(0):
        # Reorder the result to match original node indices
        result = [0] * n
        for i in range(n):
            result[i] = color_order[i]
        print("YES")
        print(" ".join(map(str, result)))
    else:
        print("NO")

solve()