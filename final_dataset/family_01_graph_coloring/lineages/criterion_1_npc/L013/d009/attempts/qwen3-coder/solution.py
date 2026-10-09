from itertools import product

def W(eu, ev):
    diff = eu - ev
    return diff**4 - 5*diff**2 + 7

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
    
    # Try all possible assignments of excitation states
    for assignment in product([1, 2, 3], repeat=n):
        total_energy = 0
        for u, v in edges:
            total_energy += W(assignment[u], assignment[v])
        
        if total_energy == 3 * m:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()