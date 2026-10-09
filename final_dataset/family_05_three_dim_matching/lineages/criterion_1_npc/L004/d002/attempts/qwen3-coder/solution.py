from itertools import combinations

def solve():
    k, t = map(int, input().split())
    configs = []
    for _ in range(t):
        p1, p2, p3 = map(int, input().split())
        configs.append((p1, p2, p3))
    
    # Try all combinations of k configurations
    for combo in combinations(range(t), k):
        selected = [configs[i] for i in combo]
        
        # Check if all values from 1 to k are present in each position
        p1_vals = set(config[0] for config in selected)
        p2_vals = set(config[1] for config in selected)
        p3_vals = set(config[2] for config in selected)
        
        if (len(p1_vals) == k and p1_vals == set(range(1, k+1)) and
            len(p2_vals) == k and p2_vals == set(range(1, k+1)) and
            len(p3_vals) == k and p3_vals == set(range(1, k+1))):
            print("YES")
            for config in selected:
                print(config[0], config[1], config[2])
            return
    
    print("NO")

solve()