import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # Group configurations by x
    configs_by_x = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        configs_by_x[x].append((y, z))
    
    # Check all x values have at least one config
    for x in range(1, k + 1):
        if not configs_by_x[x]:
            print("NO")
            return
    
    full_mask = (1 << k) - 1
    result = [None] * k
    
    # Memoization: (x_index, used_y, used_z) -> bool
    memo = {}
    
    def backtrack(x, used_y, used_z):
        if x > k:
            return used_y == full_mask and used_z == full_mask
        
        key = (x, used_y, used_z)
        if key in memo:
            return memo[key]
        
        for (y, z) in configs_by_x[x]:
            ybit = 1 << (y - 1)
            zbit = 1 << (z - 1)
            if (used_y & ybit) == 0 and (used_z & zbit) == 0:
                result[x - 1] = (x, y, z)
                if backtrack(x + 1, used_y | ybit, used_z | zbit):
                    memo[key] = True
                    return True
        
        memo[key] = False
        return False
    
    if backtrack(1, 0, 0):
        print("YES")
        for x, y, z in result:
            print(x, y, z)
    else:
        print("NO")

solve()