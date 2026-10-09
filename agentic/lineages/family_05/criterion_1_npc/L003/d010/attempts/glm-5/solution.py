import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    idx = 2
    modules = []
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        modules.append((x, y, z))
    
    # Group modules by frequency
    freq_groups = [[] for _ in range(k+1)]
    for i, (x, y, z) in enumerate(modules):
        freq_groups[x].append((y, z, i))
    
    # Filter frequencies that have at least one module
    freqs = [f for f in range(1, k+1) if freq_groups[f]]
    if len(freqs) < k:
        print("NO")
        return
    
    # We need to select exactly k modules, one per frequency, with distinct y and z.
    # This is a 3D matching problem. k <= 22, so we use DP over subsets of y (or z).
    # Let's use DP over subsets of y, tracking which z values are used.
    # Actually, we need both y and z to be distinct. So we need a matching in a bipartite graph
    # where left side is frequencies, right side is (y,z) pairs, but y and z must be distinct across selected.
    # This is a 3-dimensional matching. We can use DP over subsets of frequencies and subsets of y (or z).
    # Since k <= 22, 2^22 is about 4 million, which is manageable.
    # Let's do DP over subsets of frequencies, and for each, track which y values are used.
    # But we also need z to be distinct. So we need to track both y and z subsets.
    # That's 2^22 * 2^22 which is too large.
    # Alternative: DP over subsets of frequencies, and for each subset, store the set of possible z-subsets.
    # But that could be large too.
    # Better approach: Since we need a perfect matching in a 3-partite hypergraph, and k <= 22,
    # we can use the standard DP for 3D matching: dp[mask_y] = set of possible z masks.
    # But the number of possible z masks could be large.
    # However, we can iterate over frequencies in order, and for each frequency, try all modules,
    # updating dp. The dp maps y_mask -> z_mask. We only keep reachable (y_mask, z_mask) pairs.
    # The number of reachable pairs is at most 2^k * (number of z masks per y mask).
    # In the worst case, this could be large, but with k=22 and t <= k^3 = 10648, it might be okay.
    # Actually, the number of reachable states is bounded by the number of subsets, which is 2^k.
    # Wait, no. For each y_mask, there could be multiple z_masks. But the total number of states
    # is bounded by the number of ways to choose a set of modules, which is large.
    # Let's think differently: we can use inclusion-exclusion or a SAT solver, but that's complex.
    # Given k <= 22, we can use the standard DP for exact cover: dp[mask] where mask represents
    # which frequencies are covered, and we also need to track y and z. But that's 3D.
    # Alternative: Since k is small, we can use a recursive backtracking with pruning.
    # Let's try backtracking with heuristics.
    
    # Let's assign frequencies in order, and for each, try modules, checking y and z uniqueness.
    # We'll use bitmasks for used y and z.
    # To speed up, we can order frequencies by the number of available modules (most constrained first).
    
    freq_list = sorted(freqs, key=lambda f: len(freq_groups[f]))
    
    # Precompute for each frequency the list of (y, z, index)
    # freq_list contains the frequencies in order of increasing available modules.
    
    used_y = 0
    used_z = 0
    selected = [None] * (k+1)  # selected[f] = (y, z, index) or None
    
    # We'll do a DFS with pruning.
    # To make it faster, we can use bitmasks and precompute valid modules for each frequency.
    
    # Let's implement iterative DFS with stack.
    # But Python recursion might be okay with depth 22.
    
    # Let's try a recursive approach with memoization on (freq_index, used_y, used_z).
    # But used_y and used_z are 22-bit integers, so memoization might not help much.
    # Instead, we'll just do backtracking with pruning.
    
    # Order frequencies by increasing number of modules (already done).
    # For each frequency, try modules in some order.
    
    # Let's implement it.
    
    n_freqs = len(freq_list)
    if n_freqs < k:
        print("NO")
        return
    
    # We only need the first k frequencies in freq_list? No, we need exactly k frequencies,
    # and there are exactly k frequencies if len(freqs) == k. But if len(freqs) > k, we need to choose k.
    # Wait, the problem says we need exactly k modules with distinct frequencies. Since frequencies are 1..k,
    # and we need k distinct frequencies, we must use all frequencies 1..k. So if any frequency is missing,
    # it's impossible. So len(freqs) must be exactly k.
    # So we can assume freq_list contains all frequencies 1..k.
    
    # Now, we need to select one module per frequency such that y's are distinct and z's are distinct.
    
    # Let's do backtracking.
    
    # To optimize, we can use bitmasks for used_y and used_z.
    # We'll process frequencies in order of increasing number of modules.
    
    # Let's precompute for each frequency the list of (y, z, index) sorted by some heuristic.
    
    # Heuristic: sort modules by the number of conflicts they might cause? Not sure.
    # Let's just sort by y and z.
    
    for f in freq_list:
        freq_groups[f].sort()
    
    # Now, backtracking.
    
    # We'll use a stack for iterative DFS to avoid recursion limit issues.
    # Stack elements: (freq_index, used_y, used_z, selected_indices)
    # But selected_indices can be large, so we'll store it as a list and backtrack.
    
    # Actually, let's use recursion with sys.setrecursionlimit.
    sys.setrecursionlimit(10000)
    
    # We'll map frequencies to their position in freq_list.
    # freq_list is sorted by increasing number of modules.
    
    # Let's create a list of lists: for each position i, the modules for freq_list[i].
    freq_modules = [freq_groups[f] for f in freq_list]
    
    # Now, we need to select one module from each freq_modules[i] with distinct y and z.
    
    # Let's do backtracking.
    
    # We'll use a list 'chosen' of length k, where chosen[i] is the index in freq_modules[i] of the selected module.
    # Initially all -1.
    
    chosen = [-1] * k
    used_y = 0
    used_z = 0
    
    # We'll use a recursive function.
    def backtrack(i, used_y, used_z):
        if i == k:
            return True
        for (y, z, idx) in freq_modules[i]:
            if not (used_y & (1 << (y-1))) and not (used_z & (1 << (z-1))):
                chosen[i] = idx
                if backtrack(i+1, used_y | (1 << (y-1)), used_z | (1 << (z-1))):
                    return True
        chosen[i] = -1
        return False
    
    if backtrack(0, 0, 0):
        print("YES")
        # Reconstruct the selected modules.
        # chosen[i] is the index in modules list.
        for i in range(k):
            idx = chosen[i]
            x, y, z = modules[idx]
            print(x, y, z)
    else:
        print("NO")

solve()