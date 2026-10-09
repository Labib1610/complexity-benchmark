import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    if k == 0:
        print("YES")
        return
    
    # configs[x] = list of (y, z) for configurations with frequency band x
    configs = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        configs[x].append((y, z))
    
    # Check if any x has no configurations
    for x in range(1, k + 1):
        if not configs[x]:
            print("NO")
            return
    
    full_mask = (1 << k) - 1
    
    # Precompute for each x: list of (y_bit, z_bit, y, z)
    x_options = []
    for x in range(1, k + 1):
        opts = []
        for (y, z) in configs[x]:
            opts.append((1 << (y - 1), 1 << (z - 1), y, z))
        x_options.append(opts)
    
    # Precompute popcount
    popcount = [0] * (1 << k)
    for i in range(1, 1 << k):
        popcount[i] = popcount[i >> 1] + (i & 1)
    
    # Remaining y values available = k - popcount(used_y)
    # Remaining z values available = k - popcount(used_z)
    # Remaining x values to assign = k - x_index
    
    result = [None] * k
    
    def backtrack(x_idx, used_y, used_z):
        if x_idx == k:
            return True
        
        remaining = k - x_idx  # including current x
        avail_y = k - popcount[used_y]
        avail_z = k - popcount[used_z]
        
        if avail_y < remaining or avail_z < remaining:
            return False
        
        for (y_bit, z_bit, y, z) in x_options[x_idx]:
            if not (used_y & y_bit) and not (used_z & z_bit):
                result[x_idx] = (x_idx + 1, y, z)
                if backtrack(x_idx + 1, used_y | y_bit, used_z | z_bit):
                    return True
        return False
    
    if backtrack(0, 0, 0):
        print("YES")
        for (x, y, z) in result:
            print(f"{x} {y} {z}")
    else:
        print("NO")

solve()