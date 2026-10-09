def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list representation of conflicts
    conflicts = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        conflicts[u].add(v)
        conflicts[v].add(u)
        idx += 2
    
    # Try all 3^n assignments
    for assignment in product([1, 2, 3], repeat=n):
        valid = True
        for i in range(1, n + 1):
            for neighbor in conflicts[i]:
                if assignment[i - 1] == assignment[neighbor - 1]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()