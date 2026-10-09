def solve():
    import sys
    import itertools
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-indexed
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Check all possible assignments
    for assignment in itertools.product([1, 2, 3], repeat=n):
        valid = True
        for u, v in edges:
            bu = assignment[u]
            bv = assignment[v]
            sum_squares = bu * bu + bv * bv
            product = bu * bv
            if product != 0 and sum_squares % product == 0:
                valid = False
                break
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

solve()