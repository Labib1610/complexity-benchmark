from itertools import product

def dot_product(mode1, mode2):
    vectors = {1: (2, -1, -1), 2: (-1, 2, -1), 3: (-1, -1, 2)}
    v1 = vectors[mode1]
    v2 = vectors[mode2]
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    
    # Try all possible assignments
    for assignment in product([1, 2, 3], repeat=n):
        total_interference = 0
        for u, v in edges:
            total_interference += dot_product(assignment[u], assignment[v])
        
        if total_interference == -3 * m:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()