import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    pts = []
    idx = 2
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        pts.append((x, y, z))

    if k == 0:
        print("YES")
        return

    if t < k:
        print("NO")
        return

    # Check feasibility: each axis must have all values 1..k present
    xs = set(p[0] for p in pts)
    ys = set(p[1] for p in pts)
    zs = set(p[2] for p in pts)
    if len(xs) < k or len(ys) < k or len(zs) < k:
        print("NO")
        return

    # Build bipartite graph: x-value -> list of (y, z) pairs available
    from collections import defaultdict
    g = defaultdict(list)
    for (x, y, z) in pts:
        g[x].append((y, z))

    # We need a perfect matching of x-values to y-values, and simultaneously
    # the z-values must be a permutation of 1..k.
    # This is a 3-dimensional matching problem. With k <= 22, we use DP over
    # subsets of y-values, tracking for each subset of y the set of z-values
    # achievable. But that's too large (2^22 * 2^22).
    #
    # Instead, we use a randomized/heuristic backtracking with the structure:
    # Match x=1..k to distinct y's, and track used z's. Use Hall's theorem
    # style pruning.

    # Precompute for each subset of x, the union of available y's (Hall check)
    # and union of available z's. But 2^22 is 4M, feasible.
    # Actually we can do DP: dp[mask_y] = set of z-masks achievable.
    # But set of z-masks could be large. Let's try a different approach:
    # Since we just need ANY valid assignment, use backtracking with
    # bitmask for y and z, processing x in order of fewest options.

    # Order x by number of available (y,z) pairs (most constrained first)
    x_order = sorted(range(1, k+1), key=lambda x: len(g[x]))

    used_y = 0
    used_z = 0
    assignment = [0] * (k + 1)  # assignment[x] = (y, z)

    # Precompute Hall's condition check: for any subset S of remaining x's,
    # the number of available y's (not yet used) must be >= |S|.
    # We'll do a simpler greedy check during backtracking.

    import random
    # Shuffle options for diversity
    rng = random.Random(42)
    for x in g:
        rng.shuffle(g[x])

    def backtrack(i):
        nonlocal used_y, used_z
        if i == k:
            return True
        x = x_order[i]
        remaining = k - i
        # Quick Hall check: count available y's for remaining x's
        avail_y = 0
        for j in range(i, k):
            xj = x_order[j]
            for (y, z) in g[xj]:
                if not (used_y & (1 << (y-1))):
                    avail_y |= (1 << (y-1))
                    break
        if bin(avail_y).count('1') < remaining:
            return False
        # Same for z
        avail_z = 0
        for j in range(i, k):
            xj = x_order[j]
            for (y, z) in g[xj]:
                if not (used_z & (1 << (z-1))):
                    avail_z |= (1 << (z-1))
                    break
        if bin(avail_z).count('1') < remaining:
            return False

        for (y, z) in g[x]:
            yb = 1 << (y-1)
            zb = 1 << (z-1)
            if (used_y & yb) or (used_z & zb):
                continue
            used_y |= yb
            used_z |= zb
            assignment[x] = (y, z)
            if backtrack(i + 1):
                return True
            used_y &= ~yb
            used_z &= ~zb
        return False

    if backtrack(0):
        print("YES")
        out = []
        for x in range(1, k+1):
            y, z = assignment[x]
            out.append(f"{x} {y} {z}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        print("NO")

solve()