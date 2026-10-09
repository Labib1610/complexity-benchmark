from itertools import product

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Try all possible assignments of clock speeds (1, 2, 3)
    for assignment in product([1, 2, 3], repeat=n):
        valid = True
        for u, v in edges:
            x = assignment[u]
            y = assignment[v]
            
            # Calculate V_u and V_w
            V_u = (v * x * x + y) % x
            V_w = (u * y * y + x) % y
            
            if V_u == V_w:
                valid = False
                break
        
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

solve()