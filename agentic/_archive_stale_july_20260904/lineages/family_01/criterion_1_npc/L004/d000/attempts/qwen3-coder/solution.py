def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Create adjacency list for incompatibilities
    incompatible = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        incompatible[u].append(v)
        incompatible[v].append(u)
        idx += 2
    
    # Try all possible assignments (3^n possibilities)
    # We want the lexicographically smallest one
    for assignment in product([1, 2, 3], repeat=n):
        # Check if this assignment is valid
        valid = True
        for i in range(1, n + 1):
            for neighbor in incompatible[i]:
                # Note: modules are 1-indexed, but assignment is 0-indexed
                if assignment[i-1] == assignment[neighbor-1]:
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

solve()