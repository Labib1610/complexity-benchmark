import sys
input = sys.stdin.readline

def solve():
    q, t = map(int, input().split())
    n = 3 * q
    
    # Read all configurations
    configs = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        configs.append((a, b, c))
    
    # dp[mask] = True if mask is reachable
    # parent[mask] = configuration index that was added to reach this mask
    dp = [False] * (1 << n)
    parent = [-1] * (1 << n)
    dp[0] = True
    
    # Precompute configuration masks
    config_masks = []
    for a, b, c in configs:
        mask = (1 << (a-1)) | (1 << (b-1)) | (1 << (c-1))
        config_masks.append(mask)
    
    # DP
    for mask in range(1 << n):
        if not dp[mask]:
            continue
        for i in range(t):
            new_mask = mask | config_masks[i]
            if new_mask != mask and not dp[new_mask]:
                dp[new_mask] = True
                parent[new_mask] = i
    
    target = (1 << n) - 1
    
    if not dp[target]:
        print("NO")
        return
    
    print("YES")
    
    # Backtrack to find the configurations
    result = []
    current = target
    while current != 0:
        i = parent[current]
        result.append(configs[i])
        current = current ^ config_masks[i]
    
    for config in result:
        print(f"{config[0]} {config[1]} {config[2]}")

solve()