import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    words = []
    idx = 2
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        words.append((x, y, z))
    
    if k == 1:
        if t >= 1:
            print("YES")
            print(f"{words[0][0]} {words[0][1]} {words[0][2]}")
        else:
            print("NO")
        return
    
    # For k >= 2, we need k codewords pairwise at Hamming distance exactly 3.
    # This means for any two codewords (a,b,c) and (a',b',c'), we must have
    # a != a', b != b', c != c'.
    # So the first coordinates form a permutation of 1..k,
    # the second coordinates form a permutation of 1..k,
    # and the third coordinates form a permutation of 1..k.
    # Thus the codebook corresponds to three permutations P, Q, R of 1..k
    # such that for each i in 1..k, (P[i], Q[i], R[i]) is in the pool.
    
    # Build lookup: for each (x, y), which z values are available
    from collections import defaultdict
    z_for_xy = defaultdict(set)
    for (x, y, z) in words:
        z_for_xy[(x, y)].add(z)
    
    # We will search for permutations P, Q, R.
    # P is fixed as identity: P[i] = i for i in 1..k (by symmetry, we can relabel).
    # Actually we can't relabel because the pool is fixed. But we can try all
    # possible P? That's k! which is too large for k=22.
    # However, note that the graph structure: we need a perfect matching in a
    # 3-partite 3-uniform hypergraph. This is NP-hard in general, but k <= 22
    # and the constraints suggest a smarter approach.
    
    # Key insight: Consider the bipartite graph between first and second coordinates.
    # For each pair (x, y) that has at least one z, we have an edge.
    # We need a perfect matching in this bipartite graph (x matched to y),
    # and then for the matched pairs, we need to assign z's such that z's are
    # all distinct and form a permutation.
    
    # But even with a perfect matching, assigning z's is another matching problem.
    # Let's think differently.
    
    # Since k <= 22, we can use bitmask DP or backtracking with pruning.
    # Let's try backtracking: assign codewords one by one.
    # State: which x's used, which y's used, which z's used (as bitmasks).
    # At each step, pick the smallest unused x, and try all valid y (unused)
    # such that there exists a valid z (unused) with (x,y,z) in pool.
    
    # To make this efficient, precompute for each x, the list of (y, z) pairs.
    x_to_yz = defaultdict(list)
    for (x, y, z) in words:
        x_to_yz[x].append((y, z))
    
    # Sort x's to process in order
    all_x = sorted(x_to_yz.keys())
    
    # If some x in 1..k has no codewords, impossible
    for x in range(1, k+1):
        if x not in x_to_yz:
            print("NO")
            return
    
    # Backtracking with bitmasks
    # used_y, used_z are bitmasks (bit i-1 set means value i is used)
    # assignment[i] = (y, z) for x = i
    
    assignment = [None] * (k + 1)
    
    def backtrack(x, used_y, used_z):
        if x > k:
            return True
        for (y, z) in x_to_yz[x]:
            ybit = 1 << (y - 1)
            zbit = 1 << (z - 1)
            if (used_y & ybit) == 0 and (used_z & zbit) == 0:
                assignment[x] = (y, z)
                if backtrack(x + 1, used_y | ybit, used_z | zbit):
                    return True
                assignment[x] = None
        return False
    
    if backtrack(1, 0, 0):
        print("YES")
        for x in range(1, k + 1):
            y, z = assignment[x]
            print(f"{x} {y} {z}")
    else:
        print("NO")

solve()