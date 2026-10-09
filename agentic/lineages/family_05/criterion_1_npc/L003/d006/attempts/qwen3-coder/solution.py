from itertools import combinations

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    components = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        components.append((x, y, z))
    
    # We need to find k components such that the product of diversities equals k^3
    # This means each diversity must be k (k * k * k = k^3)
    # So we need all k values in each of the three categories
    
    target_values = set(range(1, k + 1))
    
    # Try all combinations of k components
    for combo in combinations(components, k):
        # Calculate diversities
        hardness_vals = set(comp[0] for comp in combo)
        malleability_vals = set(comp[1] for comp in combo)
        conductivity_vals = set(comp[2] for comp in combo)
        
        # Check if each diversity is exactly k
        if (len(hardness_vals) == k and 
            len(malleability_vals) == k and 
            len(conductivity_vals) == k):
            print("YES")
            for comp in combo:
                print(comp[0], comp[1], comp[2])
            return
    
    print("NO")

solve()