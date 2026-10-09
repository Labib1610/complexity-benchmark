import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    configs = [[] for _ in range(k)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        configs[x-1].append((y-1, z-1))
    
    # Precompute for each actuator the list of options
    # We'll use bitmasks for y and z
    
    full_mask = (1 << k) - 1
    
    # Memoization: (mask_y, mask_z) -> bool (whether can complete)
    memo = {}
    # To reconstruct, we can store the choice made at each state
    choice = {}
    
    # We'll process actuators in order of index, but we can also reorder for pruning.
    # Let's first try a simple recursive with order 0..k-1.
    
    def dfs(mask_y, mask_z):
        # number of actuators processed = popcount(mask_y) (should equal popcount(mask_z))
        idx = bin(mask_y).count('1')
        if idx == k:
            return mask_y == full_mask and mask_z == full_mask
        if (mask_y, mask_z) in memo:
            return memo[(mask_y, mask_z)]
        # Try all options for actuator idx
        for y, z in configs[idx]:
            if not (mask_y & (1 << y)) and not (mask_z & (1 << z)):
                if dfs(mask_y | (1 << y), mask_z | (1 << z)):
                    choice[(mask_y, mask_z)] = (y, z)
                    memo[(mask_y, mask_z)] = True
                    return True
        memo[(mask_y, mask_z)] = False
        return False
    
    if dfs(0, 0):
        # Reconstruct
        result = []
        mask_y, mask_z = 0, 0
        while mask_y != full_mask:
            idx = bin(mask_y).count('1')
            y, z = choice[(mask_y, mask_z)]
            result.append((idx+1, y+1, z+1))
            mask_y |= (1 << y)
            mask_z |= (1 << z)
        print("YES")
        for x, y, z in result:
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()