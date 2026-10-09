import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    modules = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        modules.append((x, y, z))
    
    # We need to select k modules such that:
    # sum of 2^(x-1) = 2^k - 1 for x
    # sum of 2^(y-1) = 2^k - 1 for y
    # sum of 2^(z-1) = 2^k - 1 for z
    # This means we need exactly one module with each value 1..k for each parameter
    
    # Group modules by their x value
    by_x = [[] for _ in range(k + 1)]
    for i, (x, y, z) in enumerate(modules):
        by_x[x].append((y, z, i))
    
    # For each x from 1 to k, we need to pick exactly one module
    # The chosen modules must have distinct y values (1..k) and distinct z values (1..k)
    
    # This is a bipartite matching problem for each x
    # We can use DP with bitmask
    
    # For each x, we have a set of possible (y, z) pairs
    # We need to select one pair from each x such that all y's are distinct and all z's are distinct
    
    # Let's build a bipartite graph for each x
    # Left side: y values (1..k)
    # Right side: z values (1..k)
    # For each x, we have edges representing available (y, z) pairs
    
    # We use DP: dp[mask_y][mask_z] = True if achievable
    # But this is O(4^k) which is too slow for k=22
    
    # Better approach: process x one by one, maintaining mask_y and mask_z
    # dp[mask_y][mask_z] = list of selected module indices
    
    # Since k <= 22, we need a more efficient approach
    # We can use meet-in-the-middle or Hungarian algorithm
    
    # Actually, let's try a different approach:
    # For each x, we need to pick one (y, z) pair
    # This is equivalent to finding a perfect matching in a 3D assignment problem
    # But since k is small (<=22), we can use DP with bitmask
    
    # Let's use DP where we process x from 1 to k
    # dp[mask_y][mask_z] = True if achievable with first i x values
    # But 2^22 * 2^22 is too large
    
    # Alternative: use bipartite matching for each x
    # We can model this as a 3D matching problem
    
    # Let's try a greedy approach with backtracking
    # For each x from 1 to k, try to assign a (y, z) pair that doesn't conflict
    
    # Actually, let's use a different DP approach
    # We'll use DP on mask_y only, and for each state, track which z values are used
    
    # Since k <= 22, we can use meet-in-the-middle
    # Split x values into two halves
    
    if k == 0:
        print("YES")
        return
    
    # Check if we have at least one module for each x value
    for x in range(1, k + 1):
        if not by_x[x]:
            print("NO")
            return
    
    # Use DP with bitmask for y and z
    # dp[mask_y][mask_z] = list of (x, y, z, idx) tuples
    
    # Since k <= 22, we need to be careful about memory
    # Let's use a dictionary-based DP
    
    from collections import defaultdict
    
    # dp[mask_y][mask_z] = list of selected indices
    # We'll use a dict of dicts
    
    # Process x from 1 to k
    # For each x, we update the DP
    
    # To save memory, we'll use a single dict for current state
    # Key: (mask_y, mask_z), Value: list of selected module indices
    
    # Initial state: empty selection
    dp = {(0, 0): []}
    
    for x in range(1, k + 1):
        new_dp = {}
        for (mask_y, mask_z), selected in dp.items():
            for y, z, idx in by_x[x]:
                bit_y = 1 << (y - 1)
                bit_z = 1 << (z - 1)
                if (mask_y & bit_y) == 0 and (mask_z & bit_z) == 0:
                    new_mask_y = mask_y | bit_y
                    new_mask_z = mask_z | bit_z
                    if (new_mask_y, new_mask_z) not in new_dp:
                        new_dp[(new_mask_y, new_mask_z)] = selected + [idx]
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    # Check if we have a complete selection
    target_mask = (1 << k) - 1
    for (mask_y, mask_z), selected in dp.items():
        if mask_y == target_mask and mask_z == target_mask:
            print("YES")
            for idx in selected:
                x, y, z = modules[idx]
                print(f"{x} {y} {z}")
            return
    
    print("NO")

solve()