def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # The classification string (1-indexed)
    pattern = "XOOXCOCCX"
    
    # For each product p = s_u * s_v, check if it produces 'X'
    # Products can be 1*1=1, 1*2=2, 1*3=3, 2*2=4, 2*3=6, 3*3=9
    # Check which products give 'X'
    forbidden_products = set()
    for p in range(1, 10):
        if pattern[p - 1] == 'X':
            forbidden_products.add(p)
    
    # If there are no edges, any assignment works
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Try all 3^n assignments
    for mask in range(3**n):
        # Extract assignment from mask
        assignment = []
        temp = mask
        for i in range(n):
            assignment.append((temp % 3) + 1)
            temp //= 3
        
        # Check if this assignment is valid
        valid = True
        for u, v in edges:
            product = assignment[u - 1] * assignment[v - 1]
            if product in forbidden_products:
                valid = False
                break
        
        if valid:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()