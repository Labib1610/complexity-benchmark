def solve():
    import sys
    import itertools
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    requirements = []
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        l3 = int(data[idx+2])
        requirements.append((l1, l2, l3))
        idx += 3
    
    # Try all 2^n possible assignments
    for assignment in itertools.product([0, 1], repeat=n):
        valid = True
        for req in requirements:
            satisfied = False
            for lit in req:
                if lit > 0:  # Warm filter requested
                    spotlight = lit - 1
                    if assignment[spotlight] == 1:
                        satisfied = True
                        break
                else:  # Cool filter requested
                    spotlight = -lit - 1
                    if assignment[spotlight] == 0:
                        satisfied = True
                        break
            if not satisfied:
                valid = False
                break
        if valid:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()