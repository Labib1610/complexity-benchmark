def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    clauses = []
    index = 2
    for _ in range(m):
        f1 = int(data[index])
        f2 = int(data[index+1])
        f3 = int(data[index+2])
        index += 3
        clauses.append((f1, f2, f3))
    
    # Try all possible assignments
    for mask in range(1 << n):
        valid = True
        for f1, f2, f3 in clauses:
            satisfied = False
            # Check f1
            sensor1 = abs(f1)
            required_state1 = 1 if f1 > 0 else 0
            actual_state1 = (mask >> (sensor1 - 1)) & 1
            if actual_state1 == required_state1:
                satisfied = True
            
            # Check f2
            sensor2 = abs(f2)
            required_state2 = 1 if f2 > 0 else 0
            actual_state2 = (mask >> (sensor2 - 1)) & 1
            if actual_state2 == required_state2:
                satisfied = True
                
            # Check f3
            sensor3 = abs(f3)
            required_state3 = 1 if f3 > 0 else 0
            actual_state3 = (mask >> (sensor3 - 1)) & 1
            if actual_state3 == required_state3:
                satisfied = True
                
            if not satisfied:
                valid = False
                break
        
        if valid:
            print("YES")
            result = []
            for i in range(n):
                result.append(str((mask >> i) & 1))
            print(" ".join(result))
            return
    
    print("NO")

solve()