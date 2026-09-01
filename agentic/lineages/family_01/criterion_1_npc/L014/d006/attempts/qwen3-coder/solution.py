from itertools import product

def dot_product(w1, w2):
    return sum(a * b for a, b in zip(w1, w2))

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index + 1]) - 1
        edges.append((u, v))
        index += 2
    
    # Define the operational vectors
    W = {
        1: (2, 2, 2),
        2: (-2, 2, -2),
        3: (2, -2, -2)
    }
    
    # Precompute all possible dot products
    dp = {}
    for i in range(1, 4):
        for j in range(1, 4):
            dp[(i, j)] = dot_product(W[i], W[j])
    
    target_sum = -4 * m
    
    # Try all 3^n assignments in lexicographical order
    for assignment in product([1, 2, 3], repeat=n):
        total = 0
        for u, v in edges:
            total += dp[(assignment[u], assignment[v])]
            if total > target_sum:
                break
        if total == target_sum:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()