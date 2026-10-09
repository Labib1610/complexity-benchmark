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
    
    conflicts = set()
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        conflicts.add((u, v))
        conflicts.add((v, u))
        idx += 2
    
    # Try all 3^n assignments
    for assignment in product([1, 2, 3], repeat=n):
        valid = True
        for u, v in conflicts:
            if assignment[u] == assignment[v]:
                valid = False
                break
        if valid:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()