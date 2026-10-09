import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    idx = 2
    triplets = []
    for _ in range(t):
        x = int(data[idx]) - 1
        y = int(data[idx+1]) - 1
        z = int(data[idx+2]) - 1
        idx += 3
        triplets.append((x, y, z))

    # For each left pillar x, list of (y, z) pairs.
    left_options = [[] for _ in range(k)]
    for x, y, z in triplets:
        left_options[x].append((y, z))

    # If any left pillar has no options, impossible.
    for x in range(k):
        if not left_options[x]:
            print("NO")
            return

    # We need to assign each left pillar x a (y, z) pair such that
    # all y's are distinct and all z's are distinct.
    # This is a bipartite matching problem:
    #   left side: left pillars 0..k-1
    #   right side: pairs (y, z) with y, z in 0..k-1
    # But the right side can be huge (k^2). We use a smarter approach.
    #
    # We model it as: for each left pillar x, choose a pair (y, z).
    # Constraint: y's form a permutation, z's form a permutation.
    # We can think of it as a 3D matching, but with k <= 22, we can use
    # a meet-in-the-middle or DP approach.
    #
    # Alternative: since k <= 22, we can use DP over subsets of y (or z).
    # For each subset of y assigned to the first m left pillars, track
    # the set of z's used. But that's 2^22 * 2^22 which is too large.
    #
    # Better: use bipartite matching where left pillars are matched to
    # y-values, and for each (x, y) edge, the z is determined... but z
    # is not unique per (x, y).
    #
    # Let's use a different approach: model as a flow/matching problem
    # and use the fact that k is small (<=22) to do a search with pruning.
    #
    # We'll use a recursive backtracking with bitmask for y and z.
    # To make it efficient, we order left pillars by number of options
    # (fewest first) and use bitmasks.

    # Order left pillars by number of options (ascending) for better pruning.
    order = sorted(range(k), key=lambda x: len(left_options[x]))

    # Convert options to lists for faster access.
    options = [left_options[x] for x in order]

    # Bitmasks for used y and z.
    used_y = 0
    used_z = 0
    assignment = [None] * k  # assignment[i] = (y, z) for options[i]

    # Precompute for each position, the list of (y_bit, z_bit, y, z)
    opt_bits = []
    for i in range(k):
        bits = []
        for (y, z) in options[i]:
            bits.append((1 << y, 1 << z, y, z))
        opt_bits.append(bits)

    # Recursive backtracking.
    def backtrack(pos, used_y, used_z):
        if pos == k:
            return True
        for (yb, zb, y, z) in opt_bits[pos]:
            if not (used_y & yb) and not (used_z & zb):
                assignment[pos] = (y, z)
                if backtrack(pos + 1, used_y | yb, used_z | zb):
                    return True
        return False

    if backtrack(0, 0, 0):
        print("YES")
        # Reconstruct: assignment[i] corresponds to left pillar order[i]
        result = [None] * k
        for i in range(k):
            x = order[i]
            y, z = assignment[i]
            result[x] = (x, y, z)
        for x in range(k):
            r = result[x]
            print(r[0] + 1, r[1] + 1, r[2] + 1)
    else:
        print("NO")

solve()