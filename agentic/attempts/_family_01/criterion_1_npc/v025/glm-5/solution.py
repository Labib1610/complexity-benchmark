import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1])
        idx += 2
        u -= 1; v -= 1
        if u > v:
            u, v = v, u
        edges.append((u, v))
    
    # Precompute adjacency as bitmasks
    adj = [0] * n
    for u, v in edges:
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    full = (1 << n) - 1
    
    # Enumerate all independent sets
    ind_sets = []
    for mask in range(1 << n):
        ok = True
        mm = mask
        while mm:
            b = mm & (-mm)
            i = b.bit_length() - 1
            if adj[i] & mask:
                ok = False
                break
            mm ^= b
        if ok:
            ind_sets.append(mask)
    
    # For each independent set, compute filtration cost (number of edges crossing)
    cost_of = {}
    for mask in ind_sets:
        c = 0
        mm = mask
        while mm:
            b = mm & (-mm)
            i = b.bit_length() - 1
            c += bin(adj[i] & (full ^ mask)).count('1')
            mm ^= b
        cost_of[mask] = c
    
    # Group independent sets by size
    by_size = [[] for _ in range(n+1)]
    for mask in ind_sets:
        by_size[bin(mask).count('1')].append(mask)
    
    # For each size, build dict: cost -> list of masks
    by_size_cost = []
    for s in range(n+1):
        d = {}
        for mask in by_size[s]:
            c = cost_of[mask]
            if c not in d:
                d[c] = []
            d[c].append(mask)
        by_size_cost.append(d)
    
    # DP: dp[cost] = set of achievable masks (bitmask of assigned species)
    # We try to pick 3 independent sets (greenhouses) that partition all species
    # and total filtration cost <= 800.
    
    # Start with empty
    dp = {0: {0}}
    
    for step in range(3):
        new_dp = {}
        for total_cost, masks in dp.items():
            if total_cost > 800:
                continue
            for mask in masks:
                remaining = full ^ mask
                # We need independent sets that are subsets of remaining
                # Iterate over all independent sets and check subset
                # To optimize, iterate by size and check
                for s in range(n+1):
                    for c, lst in by_size_cost[s].items():
                        if total_cost + c > 800:
                            continue
                        for iset in lst:
                            if (iset & remaining) == iset:
                                new_mask = mask | iset
                                new_cost = total_cost + c
                                if new_cost not in new_dp:
                                    new_dp[new_cost] = set()
                                new_dp[new_cost].add(new_mask)
        dp = new_dp
    
    # Check if full mask is achievable with cost <= 800
    found = None
    for total_cost, masks in dp.items():
        if total_cost <= 800 and full in masks:
            found = total_cost
            break
    
    if found is None:
        print("NO")
        return
    
    # Reconstruct the assignment
    # We need to find 3 independent sets that partition all species with total cost <= 800
    # Backtrack through the DP
    
    # Redo DP with parent tracking
    # dp[cost] = dict: mask -> (prev_mask, iset)
    dp2 = [{} for _ in range(4)]
    dp2[0][0] = None
    
    for step in range(1, 4):
        for total_cost, masks in dp2[step-1].items():
            if total_cost > 800:
                continue
            for mask in masks:
                remaining = full ^ mask
                for s in range(n+1):
                    for c, lst in by_size_cost[s].items():
                        if total_cost + c > 800:
                            continue
                        for iset in lst:
                            if (iset & remaining) == iset:
                                new_mask = mask | iset
                                new_cost = total_cost + c
                                if new_mask not in dp2[step]:
                                    dp2[step][new_mask] = (mask, iset, total_cost)
        # We can break early if full is found at step 3 with cost <= 800
        if step == 3:
            if full in dp2[3] and any(k <= 800 for k in [full] if full in dp2[3]):
                pass
    
    # Find full in dp2[3] with cost <= 800
    # dp2[3] maps mask -> (prev_mask, iset, prev_cost)
    # But we stored only one parent per mask. We need to track cost too.
    # Let's redo with cost as key.
    
    dp3 = [dict() for _ in range(4)]
    dp3[0][0] = (None, None)  # (prev_mask, iset)
    cost_at = [dict() for _ in range(4)]
    cost_at[0][0] = 0
    
    for step in range(1, 4):
        for prev_mask, prev_cost in cost_at[step-1].items():
            if prev_cost > 800:
                continue
            remaining = full ^ prev_mask
            for s in range(n+1):
                for c, lst in by_size_cost[s].items():
                    if prev_cost + c > 800:
                        continue
                    for iset in lst:
                        if (iset & remaining) == iset:
                            new_mask = prev_mask | iset
                            new_cost = prev_cost + c
                            if new_mask not in cost_at[step] or new_cost < cost_at[step][new_mask]:
                                cost_at[step][new_mask] = new_cost
                                dp3[step][new_mask] = (prev_mask, iset)
    
    # Check if full is achievable
    if full not in cost_at[3] or cost_at[3][full] > 800:
        print("NO")
        return
    
    # Reconstruct
    assignment = [0] * n
    mask = full
    for step in range(3, 0, -1):
        prev_mask, iset = dp3[step][mask]
        for i in range(n):
            if iset & (1 << i):
                assignment[i] = step
        mask = prev_mask
    
    print("YES")
    print(' '.join(str(x) for x in assignment))

solve()