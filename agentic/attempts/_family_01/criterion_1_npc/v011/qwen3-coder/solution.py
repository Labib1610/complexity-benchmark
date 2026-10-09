def solve():
    import sys
    from itertools import product
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # If no interfering pairs, all artifacts can go to module 1
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index + 1]) - 1
        edges.append((u, v))
        index += 2
    
    # Try all 3^n possible assignments
    for assignment in product([1, 2, 3], repeat=n):
        valid = True
        for u, v in edges:
            if assignment[u] == assignment[v]:
                valid = False
                break
        if valid:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()