from itertools import combinations

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    paths = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        paths.append((x, y, z))
    
    target_sum = (1 << (k + 1)) - 2  # 2^(k+1) - 2
    
    # Try all combinations of exactly k paths
    for combo in combinations(paths, k):
        freq_sum = sum(1 << path[0] for path in combo)  # 2^x
        pol_sum = sum(1 << path[1] for path in combo)   # 2^y
        phase_sum = sum(1 << path[2] for path in combo) # 2^z
        
        if freq_sum == target_sum and pol_sum == target_sum and phase_sum == target_sum:
            print("YES")
            for path in combo:
                print(path[0], path[1], path[2])
            return
    
    print("NO")

solve()