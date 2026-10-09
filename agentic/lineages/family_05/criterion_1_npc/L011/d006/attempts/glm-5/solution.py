import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    configs = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        configs.append((x-1, y-1, z-1))  # 0-indexed
    
    # We need to select k configurations such that:
    # - All x values are distinct (and cover 0..k-1)
    # - All y values are distinct (and cover 0..k-1)
    # - All z values are distinct (and cover 0..k-1)
    
    # Group configurations by their x value
    by_x = [[] for _ in range(k)]
    for idx, (x, y, z) in enumerate(configs):
        by_x[x].append((y, z, idx))
    
    # For each x, compute the bitmask of valid (y,z) pairs
    # We'll use DP: dp[mask_y][mask_z] = list of (x, config_idx) pairs
    
    # Since k <= 22, we can't have 2^22 * 2^22 states
    # But we can iterate over x from 0 to k-1 and maintain reachable states
    
    # dp is a dict: (mask_y, mask_z) -> list of selected config indices
    # Start with empty state
    dp = {(0, 0): []}
    
    for x in range(k):
        new_dp = {}
        for (mask_y, mask_z), selected in dp.items():
            for y, z, idx in by_x[x]:
                if (mask_y >> y) & 1:
                    continue
                if (mask_z >> z) & 1:
                    continue
                new_mask_y = mask_y | (1 << y)
                new_mask_z = mask_z | (1 << z)
                if (new_mask_y, new_mask_z) not in new_dp:
                    new_dp[(new_mask_y, new_mask_z)] = selected + [idx]
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    # Check if we have a complete solution
    full_mask = (1 << k) - 1
    for (mask_y, mask_z), selected in dp.items():
        if mask_y == full_mask and mask_z == full_mask:
            print("YES")
            for idx in selected:
                x, y, z = configs[idx]
                print(f"{x+1} {y+1} {z+1}")
            return
    
    print("NO")

if __name__ == "__main__":
    solve()