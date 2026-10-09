def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # We need to assign values from {1,2,3} to each node such that for every edge (u,v),
    # 4x^2 + 3xy + 4y^2 + 11(u+v)(x+y) is NOT divisible by 11
    # Let's simplify this modulo 11.
    # Since we're checking divisibility by 11, we can take everything mod 11.
    # V = 4x^2 + 3xy + 4y^2 + 11(u+v)(x+y)
    # Since 11*(u+v)(x+y) ≡ 0 (mod 11), we have:
    # V ≡ 4x^2 + 3xy + 4y^2 (mod 11)
    # So we want 4x^2 + 3xy + 4y^2 ≢ 0 (mod 11) for all edges
    
    # Precompute forbidden combinations
    # For each pair of values (x,y) where x,y in {1,2,3}, check if 4x^2 + 3xy + 4y^2 ≡ 0 (mod 11)
    forbidden = [[False]*4 for _ in range(4)]  # index 0 unused
    for x in [1,2,3]:
        for y in [1,2,3]:
            val = (4*x*x + 3*x*y + 4*y*y) % 11
            if val == 0:
                forbidden[x][y] = True
                
    # Now we need to color the graph with 3 colors {1,2,3} such that no edge connects two nodes 
    # whose colors are a forbidden pair.
    # This is a constraint satisfaction problem. We'll use backtracking.
    
    if m == 0:
        print("YES")
        print(" ".join(["1"]*n))
        return
        
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    # Try all possible assignments using backtracking
    assignment = [0] * n  # 0 means unassigned
    
    def is_valid(node, color):
        for neighbor in adj[node]:
            if assignment[neighbor] != 0:
                if forbidden[color][assignment[neighbor]]:
                    return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
            
        for color in [1,2,3]:
            if is_valid(node, color):
                assignment[node] = color
                if backtrack(node+1):
                    return True
                assignment[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    main()