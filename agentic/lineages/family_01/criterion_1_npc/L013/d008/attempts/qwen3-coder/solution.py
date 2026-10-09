def solve():
    n, m = map(int, input().split())
    
    # Read constraints
    constraints = []
    for _ in range(m):
        u, v = map(int, input().split())
        constraints.append((u, v))
    
    # Try all possible assignments
    for mask in range(3**n):
        # Generate assignment
        assignment = []
        temp_mask = mask
        for i in range(n):
            assignment.append((temp_mask % 3) + 1)
            temp_mask //= 3
        
        # Check all constraints
        valid = True
        for u, v in constraints:
            u_idx = u - 1
            v_idx = v - 1
            
            eu = assignment[u_idx]
            ev = assignment[v_idx]
            
            F1 = (u * eu * eu + v * ev * ev) % 41
            F2 = (u * ev * ev + v * eu * eu) % 41
            
            if F1 == F2:
                valid = False
                break
        
        if valid:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()