def solve():
    import sys
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
    
    # For the token game, it's a Nim-like game.
    # The first player wins if and only if the XOR of the two firm IDs is not zero.
    # Since firm IDs are 1, 2, 3, the XOR values are:
    # 1^1=0, 1^2=3, 1^3=2
    # 2^1=3, 2^2=0, 2^3=1
    # 3^1=2, 3^2=1, 3^3=0
    # So first player wins unless both departments have the same firm.
    
    # But the problem says first player must have a guaranteed winning strategy.
    # So we need XOR != 0, which means the two departments must have DIFFERENT firm IDs.
    
    # This is equivalent to a 3-coloring problem where adjacent nodes must have different colors.
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all 3-colorings lexicographically
    # We can use backtracking
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