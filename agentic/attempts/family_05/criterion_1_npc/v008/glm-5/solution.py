import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # We need to find k triples (x,y,z) such that each x,y,z in 1..k is used exactly once.
    # This is a 3-dimensional matching problem. With k <= 22, we can use DP over subsets.
    # We fix the order of specialists (x) from 1..k, and for each x we try to assign a pair (y,z).
    # State: subset of used y's (or z's). But we need both y and z to be unique.
    # Since k <= 22, we can use a bitmask for y, and for each y we track which z is used.
    # Actually we can use DP over subsets of y, and for each subset store a bitmask of used z's.
    # But that's 2^22 * 2^22 which is too large.
    # Alternative: DP over subsets of y, and for each subset store the set of possible z-bitmasks.
    # That's still too large in worst case.
    # 
    # Better approach: Since we process x in order, we can use DP[mask_y] = set of possible mask_z.
    # But the number of possible mask_z per mask_y could be large.
    # 
    # However, k <= 22 and t <= k^3. We can use meet-in-the-middle or backtracking with pruning.
    # Given the constraints, let's try backtracking with good pruning and ordering.
    # 
    # Actually, a standard approach for 3D matching with small k is to use DP over subsets of one
    # dimension and iterate. Let's use DP over subsets of y (size up to 2^22 ~ 4M), and for each
    # subset store the corresponding z-mask if unique, or a set of z-masks.
    # 
    # But to keep it manageable, we can use the fact that we process x one by one, and at step i
    # (having assigned x=1..i), we have a dict mapping mask_y -> set of mask_z.
    # The number of reachable states might be manageable due to t being limited.
    # 
    # Let's implement this DP with dictionaries.
    
    # Group triples by x
    triples_by_x = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        triples_by_x[x].append((y, z))
    
    # DP: dict mapping mask_y -> dict mapping mask_z -> prev_info for reconstruction
    # We process x from 1 to k. At each step, we only keep states where popcount(mask_y) == x.
    # 
    # To save memory, we store for each (mask_y, mask_z) the chosen (y,z) and previous state.
    # But storing full reconstruction might be heavy. Let's store parent pointers.
    
    # Initial state: mask_y = 0, mask_z = 0
    # We'll use a dict: dp[mask_y] = dict of mask_z -> (y, z, prev_mask_y, prev_mask_z)
    # Actually we can just store dp as dict of (mask_y, mask_z) -> (y, z, prev_mask_y, prev_mask_z)
    # But that's a lot of tuples. Let's use a dict mapping (mask_y, mask_z) to parent info.
    
    # To optimize, we can use a list of dicts: for each x, a dict mapping (mask_y, mask_z) to (y, z, prev_mask_y, prev_mask_z)
    # But we only need the previous state to reconstruct.
    
    # Let's use a single dict for current states.
    # current: dict mapping (mask_y, mask_z) -> (y, z, prev_mask_y, prev_mask_z)
    
    current = {(0, 0): None}
    
    for x in range(1, k + 1):
        next_states = {}
        for (mask_y, mask_z), parent in current.items():
            for (y, z) in triples_by_x[x]:
                bit_y = 1 << (y - 1)
                bit_z = 1 << (z - 1)
                if (mask_y & bit_y) == 0 and (mask_z & bit_z) == 0:
                    new_mask_y = mask_y | bit_y
                    new_mask_z = mask_z | bit_z
                    key = (new_mask_y, new_mask_z)
                    if key not in next_states:
                        next_states[key] = (y, z, mask_y, mask_z)
        current = next_states
        if not current:
            print("NO")
            return
    
    # If we have any state with mask_y == (1<<k)-1 and mask_z == (1<<k)-1, we found a solution.
    full_mask = (1 << k) - 1
    final_key = (full_mask, full_mask)
    if final_key not in current:
        print("NO")
        return
    
    # Reconstruct
    assignments = []
    # We need to reconstruct from the final state back to initial.
    # But we only stored parent info in the last `current` dict. We need to store all layers.
    # Oops, we overwrote current. We need to keep all layers.
    
    # Let's redo with storing layers.
    # Actually, we can store all layers in a list.
    
    # Re-run DP with layer storage
    current = {(0, 0): None}
    layers = [current]
    for x in range(1, k + 1):
        next_states = {}
        for (mask_y, mask_z), parent in current.items():
            for (y, z) in triples_by_x[x]:
                bit_y = 1 << (y - 1)
                bit_z = 1 << (z - 1)
                if (mask_y & bit_y) == 0 and (mask_z & bit_z) == 0:
                    new_mask_y = mask_y | bit_y
                    new_mask_z = mask_z | bit_z
                    key = (new_mask_y, new_mask_z)
                    if key not in next_states:
                        next_states[key] = (y, z, mask_y, mask_z)
        current = next_states
        layers.append(current)
        if not current:
            print("NO")
            return
    
    if (full_mask, full_mask) not in layers[k]:
        print("NO")
        return
    
    # Reconstruct
    assignments = []
    cur_key = (full_mask, full_mask)
    for x in range(k, 0, -1):
        y, z, prev_mask_y, prev_mask_z = layers[x][cur_key]
        assignments.append((x, y, z))
        cur_key = (prev_mask_y, prev_mask_z)
    
    assignments.reverse()
    print("YES")
    for x, y, z in assignments:
        print(x, y, z)

solve()