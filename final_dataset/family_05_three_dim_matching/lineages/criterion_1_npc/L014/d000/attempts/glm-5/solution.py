import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    reactions = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        reactions.append((x-1, y-1, z-1))  # 0-indexed
    
    # We need to find k reactions such that:
    # - All x are distinct (0 to k-1)
    # - All y are distinct (0 to k-1)
    # - All z are distinct (0 to k-1)
    
    # Group reactions by x (base fluid)
    by_x = [[] for _ in range(k)]
    for idx, (x, y, z) in enumerate(reactions):
        by_x[x].append((y, z, idx))
    
    # State: (used_y_mask, used_z_mask) -> (prev_x, prev_y, prev_z, reaction_idx)
    # We use DP to find if we can select k reactions
    # dp[x][used_y][used_z] = True if possible
    
    # Since k <= 22, we can use bitmask DP
    # dp[used_y][used_z] = set of x's used (or we track which x we're at)
    
    # Alternative: process x from 0 to k-1, for each x, try to pick one reaction
    # dp[x][used_y][used_z] = True if possible to select x+1 reactions
    
    # But 2^22 * 2^22 is too large. We need a different approach.
    
    # Since we must use each x exactly once, we process x in order
    # dp[used_y][used_z] = True if we can select reactions for x=0..current_x
    
    # Actually, we can use meet-in-the-middle or other techniques
    # But let's try a different approach: 3D matching via reduction to bipartite matching
    
    # Reduction: Create a bipartite graph where left side is (y, z) pairs and right side is x
    # But this doesn't directly work...
    
    # Let's use DP with pruning
    # dp[mask_y][mask_z] = True if possible
    # We iterate through x and update
    
    # For k=22, 2^22 * 2^22 is way too large
    # We need to be smarter
    
    # Observation: We can use DP where we track (used_y, used_z) but only for reachable states
    # The number of reachable states might be much smaller
    
    from collections import defaultdict
    
    # dp[x][used_y][used_z] = (prev_y, prev_z, reaction_idx) for reconstruction
    # We'll use a dictionary to store only reachable states
    
    # dp[used_y][used_z] = x (the number of x's processed)
    # Actually, let's use: dp[(used_y, used_z)] = (x, parent_state, reaction_idx)
    
    # Start: dp[(0, 0)] = (0, None, None) means we've processed 0 x's
    # For each state, we try to add a reaction with x = current_x
    
    # But we need to process x in order, so we know which x we're adding
    
    # Let's use: dp[x] = dict mapping (used_y, used_z) to (prev_used_y, prev_used_z, reaction_idx)
    
    dp = [defaultdict(lambda: None) for _ in range(k+1)]
    dp[0][(0, 0)] = (-1, -1, -1)  # dummy entry
    
    for x in range(k):
        for (used_y, used_z), (prev_y, prev_z, prev_idx) in list(dp[x].items()):
            if dp[x][(used_y, used_z)] is None:
                continue
            for y, z, idx in by_x[x]:
                if not (used_y & (1 << y)) and not (used_z & (1 << z)):
                    new_used_y = used_y | (1 << y)
                    new_used_z = used_z | (1 << z)
                    if dp[x+1][(new_used_y, new_used_z)] is None:
                        dp[x+1][(new_used_y, new_used_z)] = (used_y, used_z, idx)
    
    # Check if we have a valid state at dp[k]
    valid_state = None
    for (used_y, used_z), _ in dp[k].items():
        if used_y == (1 << k) - 1 and used_z == (1 << k) - 1:
            valid_state = (used_y, used_z)
            break
    
    if valid_state is None:
        print("NO")
        return
    
    # Reconstruct the solution
    result = []
    state = valid_state
    for x in range(k, 0, -1):
        prev_y, prev_z, idx = dp[x][state]
        result.append(reactions[idx])
        state = (prev_y, prev_z)
    
    result.reverse()
    print("YES")
    for x, y, z in result:
        print(x+1, y+1, z+1)

solve()