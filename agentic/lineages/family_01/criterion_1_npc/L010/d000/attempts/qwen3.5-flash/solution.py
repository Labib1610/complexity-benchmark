import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    # Store incompatible pairs
    incompat = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        incompat[u].add(v)
        incompat[v].add(u)
    
    # Assignment array
    assignment = [0] * (n + 1)
    found = False
    
    def backtrack(i):
        nonlocal found
        if found:
            return True
        
        if i > n:
            found = True
            return True
        
        for shift in [1, 2, 3]:
            # Check if this shift is valid for worker i
            valid = True
            for other in incompat[i]:
                if other <= n and assignment[other] == shift:
                    valid = False
                    break
            
            if valid:
                assignment[i] = shift
                if backtrack(i + 1):
                    return True
                assignment[i] = 0
        
        return False
    
    backtrack(1)
    
    if found:
        print("YES")
        print(" ".join(str(assignment[i]) for i in range(1, n + 1)))
    else:
        print("NO")

solve()