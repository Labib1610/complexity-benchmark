import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    triplets = []
    idx = 2
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        triplets.append((x, y, z))
        idx += 3

    # Build adjacency: for each (x, y), list of z values
    adj = {}
    for (x, y, z) in triplets:
        adj.setdefault((x, y), []).append(z)

    # We need a perfect matching in the 3-partite 3-uniform hypergraph.
    # Since k <= 22, we can use DP over subsets of z for each (x,y) pair.
    # But number of (x,y) pairs can be up to k^2 = 484, and 2^22 = 4M, too large for product.
    # 
    # Alternative: treat as bipartite matching between (x,y) pairs and z values,
    # but we also need each x used once and each y used once.
    # 
    # Better: DP over subsets of x, y, z simultaneously is 3^k * something, too large.
    # 
    # Given constraints: each resource appears in at most k^2 configurations,
    # and x*y*z <= 10648. Since k <= 22, 22^3 = 10648, so this is just saying
    # the product doesn't exceed k^3, which is always true. Not helpful.
    # 
    # Let's use backtracking with pruning. k <= 22, but with good pruning it might work.
    # 
    # Actually, let's think of it as: assign each x a y and z. 
    # For each x, we have a set of (y, z) pairs. We need to pick one (y,z) per x
    # such that all y's are distinct and all z's are distinct.
    # 
    # This is like a bipartite matching problem but with an extra constraint.
    # We can do DP: dp[mask_y][mask_z] = True/False, but that's 2^22 * 2^22, too large.
    # 
    # However, we can process x one by one and use DP over (mask_y, mask_z).
    # But 2^22 * 2^22 is way too large.
    # 
    # Let's try: dp[mask_y] = set of achievable mask_z. Since each x contributes
    # at most k^2 pairs, and we process x from 1 to k, the set of mask_z for each
    # mask_y could be large but maybe manageable with bitset operations.
    # 
    # Actually 2^22 = 4M, and for each we'd store a set of z-masks. Too large.
    # 
    # Let's try backtracking with good ordering and pruning.

    # Group by x
    by_x = {}
    for (x, y, z) in triplets:
        by_x.setdefault(x, []).append((y, z))

    # Check feasibility: each x must have at least one option
    for x in range(1, k+1):
        if x not in by_x:
            print("NO")
            return

    # Order x by number of options (fewest first) for better pruning
    xs = sorted(range(1, k+1), key=lambda x: len(by_x[x]))

    used_y = 0
    used_z = 0
    assignment = [None] * (k + 1)  # assignment[x] = (y, z)

    def backtrack(i):
        nonlocal used_y, used_z
        if i == k:
            return True
        x = xs[i]
        for (y, z) in by_x[x]:
            yb = 1 << (y - 1)
            zb = 1 << (z - 1)
            if (used_y & yb) == 0 and (used_z & zb) == 0:
                used_y |= yb
                used_z |= zb
                assignment[x] = (y, z)
                if backtrack(i + 1):
                    return True
                used_y &= ~yb
                used_z &= ~zb
                assignment[x] = None
        return False

    if backtrack(0):
        print("YES")
        for x in range(1, k+1):
            y, z = assignment[x]
            print(f"{x} {y} {z}")
    else:
        print("NO")

solve()