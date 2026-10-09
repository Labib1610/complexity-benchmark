def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Package tracking capabilities
    # Package 1: Temperature(0), Salinity(1), Pressure(2)
    # Package 2: Temperature(0), Salinity(1), Turbidity(3)
    # Package 3: Temperature(0), Pressure(2), Turbidity(3)
    packages = [
        {0, 1, 2},      # Package 1
        {0, 1, 3},      # Package 2
        {0, 2, 3}       # Package 3
    ]
    
    # All metrics
    all_metrics = {0, 1, 2, 3}
    
    # Try all possible assignments (3^n possibilities)
    for mask in range(3**n):
        assignment = []
        temp_mask = mask
        for _ in range(n):
            assignment.append(temp_mask % 3)
            temp_mask //= 3
        
        # Check if this assignment satisfies all constraints
        valid = True
        for u, v in edges:
            metrics_u = packages[assignment[u]]
            metrics_v = packages[assignment[v]]
            union_metrics = metrics_u | metrics_v
            if union_metrics != all_metrics:
                valid = False
                break
        
        if valid:
            print("YES")
            result = [str(assignment[i] + 1) for i in range(n)]  # Convert back to 1-indexed packages
            print(" ".join(result))
            return
    
    print("NO")

solve()