def is_stable(fu, fv):
    return fu**3 + fv**3 > (fu + fv) * fu * fv

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-indexed
        v = int(data[idx+1]) - 1
        edges.append((u, v))
        idx += 2
    
    # Try all possible assignments in lexicographical order
    for mask in range(3**n):
        assignment = []
        temp_mask = mask
        valid = True
        
        # Extract the assignment from the mask
        for i in range(n):
            assignment.append((temp_mask % 3) + 1)
            temp_mask //= 3
        
        # Check if this assignment is stable for all edges
        for u, v in edges:
            if not is_stable(assignment[u], assignment[v]):
                valid = False
                break
        
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

solve()