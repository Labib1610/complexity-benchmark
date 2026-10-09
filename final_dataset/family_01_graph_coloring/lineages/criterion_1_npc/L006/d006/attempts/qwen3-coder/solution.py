from itertools import product

def E(s_u, s_v):
    diff = s_u - s_v
    return 5 * (diff ** 4) - 25 * (diff ** 2) + 13

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Try all 3^n combinations
    for combo in product([1, 2, 3], repeat=n):
        total = 0
        for u, v in edges:
            total += E(combo[u], combo[v])
        if total == -7 * m:
            print("YES")
            print(" ".join(map(str, combo)))
            return
    
    print("NO")

solve()