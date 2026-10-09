from itertools import combinations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    configs = []
    idx = 2
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        z = int(data[idx+2])
        configs.append((x, y, z))
        idx += 3
    
    # Try all combinations of k configurations
    for combo in combinations(range(t), k):
        selected = [configs[i] for i in combo]
        
        # Check if all resources are used
        freqs = set(conf[0] for conf in selected)
        posns = set(conf[1] for conf in selected)
        keys = set(conf[2] for conf in selected)
        
        if len(freqs) == k and len(posns) == k and len(keys) == k:
            print("YES")
            for conf in selected:
                print(conf[0], conf[1], conf[2])
            return
    
    print("NO")

solve()