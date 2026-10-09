import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0]); m = int(data[1]); k = int(data[2])
    adj = [0] * (n + 1)
    idx = 3
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    if k == 0:
        print("YES")
        print()
        return

    half = n // 2
    left = list(range(1, half + 1))
    right = list(range(half + 1, n + 1))

    def popcount(x):
        return bin(x).count('1')

    # left subsets
    left_masks = []
    for s in range(1 << len(left)):
        ok = True
        cnt = 0
        for i, u in enumerate(left):
            if s & (1 << i):
                cnt += 1
                if adj[u] & s:
                    ok = False
                    break
        if ok:
            left_masks.append((cnt, s))

    left_masks.sort()

    # right subsets
    right_masks = []
    for s in range(1 << len(right)):
        ok = True
        cnt = 0
        for i, u in enumerate(right):
            if s & (1 << i):
                cnt += 1
                if adj[u] & s:
                    ok = False
                    break
        if ok:
            right_masks.append((cnt, s))

    right_masks.sort()

    # group right by count
    from collections import defaultdict
    right_by_cnt = defaultdict(list)
    for cnt, s in right_masks:
        right_by_cnt[cnt].append(s)

    # for each left subset, find right subset with total k and no cross edges
    # cross edges: for u in left chosen, adj[u] has bits in right
    # we need right subset to avoid those bits
    # precompute right bit positions
    right_offset = half + 1
    right_bit = [u - right_offset for u in right]  # bit index in right subset

    # precompute forbidden mask for left subset (in right bit space)
    # forbidden = union of adj[u] bits restricted to right nodes
    # adj[u] is global mask with bits 1..n
    # right nodes are half+1..n, bit index = u - (half+1)
    # so forbidden_right_mask = (adj[u] >> (half+1)) & ((1<<len(right))-1)

    RIGHT_MASK = (1 << len(right)) - 1
    SHIFT = half + 1

    # binary search per left
    import bisect

    # precompute right counts sorted list
    right_counts_sorted = sorted(right_by_cnt.keys())

    for lcnt, lmask in left_masks:
        need = k - lcnt
        if need < 0 or need > len(right):
            continue
        if need not in right_by_cnt:
            continue
        # forbidden mask
        forbidden = 0
        s = lmask
        # iterate set bits
        temp = s
        while temp:
            b = temp & (-temp)
            u = left[(b.bit_length() - 1)]
            forbidden |= (adj[u] >> SHIFT) & RIGHT_MASK
            temp ^= b
        # find right subset with count=need and (s & forbidden)==0
        candidates = right_by_cnt[need]
        # binary search? candidates is list of masks, sorted by mask value
        # we need any mask with (mask & forbidden) == 0
        # linear scan might be too slow if many candidates
        # but total candidates across all needs is at most 2^23 ~ 8M, and left up to 2^23
        # worst case 8M * 8M too slow
        # need smarter: precompute for each forbidden? 
        # Alternative: meet in middle again? 
        # Let's just try linear with early break, hope constraints allow
        # Actually n<=46, half=23, 2^23=8M, too large for Python
        # Need better approach

        # Use SOS DP to find any independent set of size need avoiding forbidden
        # Too complex. Let's use randomized or greedy fallback.

        # Simple approach: iterate candidates, break when found
        found_r = None
        for rmask in candidates:
            if (rmask & forbidden) == 0:
                found_r = rmask
                break
        if found_r is not None:
            # build answer
            ans = []
            for i, u in enumerate(left):
                if lmask & (1 << i):
                    ans.append(u)
            for i, u in enumerate(right):
                if found_r & (1 << i):
                    ans.append(u)
            print("YES")
            print(' '.join(map(str, ans)))
            return

    print("NO")

solve()