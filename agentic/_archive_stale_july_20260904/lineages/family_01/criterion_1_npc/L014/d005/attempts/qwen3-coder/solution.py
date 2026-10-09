from itertools import product

def dot_product(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

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
    
    # Signature vectors
    V = {
        1: (1, 1, 1, 1),
        2: (1, -1, 1, -1),
        3: (1, 1, -1, -1)
    }
    
    # Precompute dot products
    dot = {}
    for i in range(1, 4):
        for j in range(1, 4):
            dot[(i, j)] = dot_product(V[i], V[j])
    
    # Try all possible assignments in lexicographical order
    for assignment in product([1, 2, 3], repeat=n):
        total = 0
        for u, v in edges:
            total += dot[(assignment[u], assignment[v])]
        
        if total == 0:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()