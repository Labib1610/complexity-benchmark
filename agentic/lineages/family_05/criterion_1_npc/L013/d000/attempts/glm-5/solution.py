import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    idx = 2
    # adj[d] = list of (f, m)
    adj = [[] for _ in range(k + 1)]
    for _ in range(t):
        d = int(data[idx]); f = int(data[idx+1]); m = int(data[idx+2])
        idx += 3
        adj[d].append((f, m))

    # We need a perfect matching in a 3-partite 3-uniform hypergraph.
    # Use DP over subsets of formulations and facilities.
    # State: (mask_f, mask_m) -> chosen (f, m) for demographics processed so far.
    # Since k <= 22, 2^22 is too large for full mask, but we can use meet-in-the-middle
    # or observe that mask_f and mask_m have the same popcount = number of demographics processed.
    # We split demographics into two halves and do meet-in-the-middle.

    half = k // 2
    rest = k - half

    # Process first half of demographics (1..half)
    # Map (mask_f, mask_m) -> list of (f, m) assignments for demographics 1..half
    # To save memory, store only one solution path.
    from collections import defaultdict
    left_states = {}
    # initial state: no demographics processed
    left_states[(0, 0)] = []

    for d in range(1, half + 1):
        new_states = {}
        for (mf, mm), path in left_states.items():
            for (f, m) in adj[d]:
                bf = 1 << (f - 1)
                bm = 1 << (m - 1)
                if (mf & bf) == 0 and (mm & bm) == 0:
                    nkey = (mf | bf, mm | bm)
                    if nkey not in new_states:
                        new_states[nkey] = path + [(d, f, m)]
        left_states = new_states
        if not left_states:
            print("NO")
            return

    # Process second half of demographics (half+1..k)
    # We want to find a right state such that (left_mask | right_mask_f) == full and (left_mask | right_mask_m) == full
    full_mask = (1 << k) - 1

    # For meet-in-the-middle: we process right half and for each right state, check if there's a left state with complementary masks.
    # left needed: (full_mask ^ right_f, full_mask ^ right_m)
    # But left states only have demographics 1..half, so their masks have popcount = half.
    # Right states have popcount = rest.
    # So we need left_f = full_mask ^ right_f and left_m = full_mask ^ right_m.

    # Store left states in a dict for quick lookup
    left_lookup = left_states  # key: (mf, mm) -> path

    right_states = {}
    right_states[(0, 0)] = []

    for d in range(half + 1, k + 1):
        new_states = {}
        for (mf, mm), path in right_states.items():
            for (f, m) in adj[d]:
                bf = 1 << (f - 1)
                bm = 1 << (m - 1)
                if (mf & bf) == 0 and (mm & bm) == 0:
                    nkey = (mf | bf, mm | bm)
                    if nkey not in new_states:
                        new_states[nkey] = path + [(d, f, m)]
        right_states = new_states
        if not right_states:
            print("NO")
            return

    # Now combine
    for (rf, rm), rpath in right_states.items():
        lf = full_mask ^ rf
        lm = full_mask ^ rm
        key = (lf, lm)
        if key in left_lookup:
            lpath = left_lookup[key]
            print("YES")
            for d, f, m in lpath:
                print(f"{d} {f} {m}")
            for d, f, m in rpath:
                print(f"{d} {f} {m}")
            return

    print("NO")

solve()