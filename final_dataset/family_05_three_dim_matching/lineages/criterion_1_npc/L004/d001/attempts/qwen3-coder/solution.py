from itertools import permutations

def solve():
    k, t = map(int, input().split())
    configs = []
    for _ in range(t):
        p1, p2, p3 = map(int, input().split())
        configs.append((p1, p2, p3))
    
    # Try all permutations of k configurations
    for perm in permutations(range(t), k):
        # Check if this permutation forms a valid schedule
        used_p1 = set()
        used_p2 = set()
        used_p3 = set()
        valid = True
        
        selected_configs = []
        for i in perm:
            p1, p2, p3 = configs[i]
            if p1 in used_p1 or p2 in used_p2 or p3 in used_p3:
                valid = False
                break
            used_p1.add(p1)
            used_p2.add(p2)
            used_p3.add(p3)
            selected_configs.append((p1, p2, p3))
        
        if valid and len(used_p1) == k and len(used_p2) == k and len(used_p3) == k:
            print("YES")
            for config in selected_configs:
                print(config[0], config[1], config[2])
            return
    
    print("NO")

solve()