def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # For each node, we'll keep track of forbidden colors
    # Try all possible colorings using backtracking
    # Since n <= 40 and we have 3 colors, and graph is general, 
    # but chromatic number is at most 3, let's try greedy + backtracking approach
    
    # Actually, since we need to check if 3-coloring exists,
    # and n is small enough, we can try all 3^n possibilities for small n
    # But 3^40 is too large. However, we can use backtracking with pruning.
    
    # Let's build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to 3-color the graph
    color = [-1] * n  # -1 means uncolored
    
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
    
    # Start backtracking from node 0
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()