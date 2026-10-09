from itertools import product

def solve():
    n, m = map(int, input().split())
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Precompute intrinsic energies for each state
    # E(s) = d * (s^4 - 5*s^2)
    def intrinsic_energy(d, s):
        return d * (s**4 - 5*s**2)
    
    # Precompute coupling energies
    # C(s1, s2) = 2*s1*s2*(3*s1*s2 + 5 - 2*s1^2 - 2*s2^2)
    def coupling_energy(s1, s2):
        return 2*s1*s2*(3*s1*s2 + 5 - 2*s1*s1 - 2*s2*s2)
    
    # Try all possible assignments
    for assignment in product([1, 2, 3], repeat=n):
        total_energy = 0
        
        # Calculate intrinsic energies
        for i in range(n):
            d = len(adj[i])
            total_energy += intrinsic_energy(d, assignment[i])
        
        # Calculate coupling energies
        for u, v in edges:
            total_energy += coupling_energy(assignment[u], assignment[v])
        
        if total_energy == -4 * m:
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()