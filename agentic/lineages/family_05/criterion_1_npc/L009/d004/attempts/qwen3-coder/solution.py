from itertools import combinations

def solve():
    k, t = map(int, input().split())
    
    if t == 0:
        print("NO")
        return
    
    paths = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        paths.append((x, y, z))
    
    target_sum = (1 << (k + 1)) - 2  # 2^(k+1) - 2
    
    # Try all combinations of k paths
    for combo in combinations(paths, k):
        # Check frequency energy
        freq_sum = sum(1 << x for x, _, _ in combo)
        if freq_sum != target_sum:
            continue
            
        # Check polarization energy
        pol_sum = sum(1 << y for _, y, _ in combo)
        if pol_sum != target_sum:
            continue
            
        # Check phase energy
        phase_sum = sum(1 << z for _, _, z in combo)
        if phase_sum != target_sum:
            continue
            
        # If we reach here, we found a valid configuration
        print("YES")
        for x, y, z in combo:
            print(x, y, z)
        return
    
    print("NO")

solve()