from itertools import combinations

def solve():
    n, m, t = map(int, input().split())
    T = list(map(int, input().split()))
    
    pairs = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        pairs.append((u, v, w))
    
    # If t <= 1, no subset can split T, so condition is vacuously true
    if t <= 1:
        print(0)
        return
    
    # Generate all possible subsets of T that split T
    # A subset Y splits T if 0 < |Y ∩ T| < |T|
    splitting_subsets = []
    T_set = set(T)
    
    # Check all possible subsets of E (universe) that intersect T properly
    # We only care about how these subsets intersect with T
    # So we can represent each relevant subset by its intersection with T
    for r in range(1, t):  # We want proper subsets of T that are non-empty
        for subset_T in combinations(T, r):
            splitting_subsets.append(set(subset_T))
    
    # For each splitting subset of T, we create a constraint
    # A subset Y splits a pair {u,v} iff (u in Y) != (v in Y)
    # We want that for every splitting Y of T, there exists a selected pair that Y splits
    
    # We'll use a bitmask approach over the elements of T
    # Each subset of T can be represented as a bitmask of t bits
    # But we only consider those that are proper non-empty subsets
    
    # Map each splitting subset to a unique identifier
    constraints = []
    for s in splitting_subsets:
        # For this constraint (splitting subset s of T),
        # we need at least one selected pair {u,v} such that
        # (u in s) != (v in s), i.e., the pair is split by s
        
        # Create a constraint: at least one of the pairs that are split by s must be chosen
        # Find all pairs that are split by s
        split_pairs = []
        for i, (u, v, w) in enumerate(pairs):
            u_in_s = u in s
            v_in_s = v in s
            if u_in_s != v_in_s:  # Pair is split by subset s
                split_pairs.append(i)
        
        if split_pairs:  # Only add constraint if there are pairs that can satisfy it
            constraints.append(split_pairs)
    
    # Now we have a set cover problem:
    # We need to select a set of pairs with minimum cost such that
    # for each constraint (a list of pair indices), at least one of them is selected
    
    # Since t <= 10, number of constraints is at most 2^10 - 2 = 1022
    # But actually it's less because we only take proper non-empty subsets
    # Which is 2^t - 2 (excluding empty set and full set)
    
    # Use dynamic programming with bitmasks
    # dp[mask] = minimum cost to satisfy all constraints represented by mask
    # where mask represents which constraints are satisfied
    
    num_constraints = len(constraints)
    if num_constraints == 0:
        print(0)
        return
        
    # Precompute for each pair, which constraints it satisfies
    pair_satisfies = [[] for _ in range(m)]
    for i, constraint in enumerate(constraints):
        for pair_idx in constraint:
            pair_satisfies[pair_idx].append(i)
    
    # DP over subsets of constraints
    INF = float('inf')
    dp = [INF] * (1 << num_constraints)
    dp[0] = 0
    
    # For each pair, see what constraints it can help satisfy
    for pair_idx in range(m):
        u, v, w = pairs[pair_idx]
        # Determine which existing constraints this pair helps satisfy
        satisfying = 0
        for i in range(num_constraints):
            if pair_idx in constraints[i]:
                satisfying |= (1 << i)
        
        # Update DP
        for mask in range(1 << num_constraints):
            if dp[mask] != INF:
                new_mask = mask | satisfying
                dp[new_mask] = min(dp[new_mask], dp[mask] + w)
    
    print(dp[(1 << num_constraints) - 1])

solve()