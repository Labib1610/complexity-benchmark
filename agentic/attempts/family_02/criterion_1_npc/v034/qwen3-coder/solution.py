def solve():
    n, m = map(int, input().split())
    
    # Read constraints
    constraints = []
    for _ in range(m):
        constraint = list(map(int, input().split()))
        constraints.append(constraint)
    
    # Try all possible configurations (2^n possibilities)
    for mask in range(1 << n):
        # Convert mask to valve configuration
        # bit 0 means closed (0), bit 1 means open (1)
        config = []
        for i in range(n):
            config.append((mask >> i) & 1)
        
        # Check if this configuration satisfies all constraints
        valid = True
        for constraint in constraints:
            satisfied = False
            for valve_req in constraint:
                valve_idx = abs(valve_req) - 1  # Convert to 0-based index
                required_state = 1 if valve_req > 0 else 0
                
                if config[valve_idx] == required_state:
                    satisfied = True
                    break
            
            if not satisfied:
                valid = False
                break
        
        if valid:
            print("YES")
            print(" ".join(map(str, config)))
            return
    
    print("NO")

solve()