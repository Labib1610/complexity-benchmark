def solve():
    n, m = map(int, input().split())
    
    # Read criteria
    criteria = []
    for _ in range(m):
        line = list(map(int, input().split()))
        criteria.append(line)
    
    # Try all possible configurations (2^n possibilities)
    for config_num in range(1 << n):
        # Convert config_num to binary representation
        config = []
        for i in range(n):
            config.append((config_num >> i) & 1)
        
        # Check if this configuration satisfies all criteria
        valid = True
        for criterion in criteria:
            satisfied = False
            for req in criterion:
                valve_idx = abs(req) - 1  # Convert to 0-based index
                required_state = 1 if req > 0 else 0
                
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