def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    rules = []
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        l3 = int(data[index+2])
        index += 3
        rules.append((l1, l2, l3))
    
    # Try all 2^n possible assignments
    for mask in range(1 << n):
        valid = True
        # Check each rule
        for l1, l2, l3 in rules:
            # Check if at least one condition is satisfied
            ok = False
            for lit in [l1, l2, l3]:
                if lit > 0:
                    var = lit - 1
                    if (mask >> var) & 1:
                        ok = True
                        break
                else:
                    var = -lit - 1
                    if not ((mask >> var) & 1):
                        ok = True
                        break
            if not ok:
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