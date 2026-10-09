import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # split vertices
    l = n // 2
    r = n - l
    left_ids = list(range(l))
    right_ids = list(range(l, n))

    # precompute adjacency masks within each side and cross
    left_adj = [0] * l
    right_adj = [0] * r
    cross_adj_left = [0] * l   # bits of right side adjacent to left vertex
    cross_adj_right = [0] * r  # bits of left side adjacent to right vertex

    for i in range(l):
        mask = 0
        for j in range(l):
            if adj[i] >> j & 1:
                mask |= 1 << j
        left_adj[i] = mask
        # cross
        cross = 0
        for idx, v in enumerate(right_ids):
            if adj[i] >> v & 1:
                cross |= 1 << idx
        cross_adj_left[i] = cross

    for idx, v in enumerate(right_ids):
        mask = 0
        for jdx, w in enumerate(right_ids):
            if adj[v] >> w & 1:
                mask |= 1 << jdx
        right_adj[idx] = mask
        # cross back
        cross = 0
        for i in range(l):
            if adj[v] >> i & 1:
                cross |= 1 << i
        cross_adj_right[idx] = cross

    # enumerate independent subsets in left
    left_indep = []
    for mask in range(1 << l):
        ok = True
        # check internal edges
        # fast: for each set bit i, ensure no neighbor also set
        sub = mask
        while sub:
            i = (sub & -sub).bit_length() - 1
            if left_adj[i] & mask:
                ok = False
                break
            sub &= sub - 1
        if ok:
            left_indep.append((mask, mask.bit_count()))
    # enumerate independent subsets in right
    right_indep = []
    for mask in range(1 << r):
        ok = True
        sub = mask
        while sub:
            i = (sub & -sub).bit_length() - 1
            if right_adj[i] & mask:
                ok = False
                break
            sub &= sub - 1
        if ok:
            right_indep.append((mask, mask.bit_count()))
    # For quick lookup, group right independent masks by size
    right_by_size = {}
    for mask, sz in right_indep:
        right_by_size.setdefault(sz, []).append(mask)

    # try combinations
    for lmask, lsz in left_indep:
        need = k - lsz
        if need < 0:
            continue
        # compute allowed vertices in right (those not adjacent to any left vertex in lmask)
        forbid = 0
        sub = lmask
        while sub:
            i = (sub & -sub).bit_length() - 1
            forbid |= cross_adj_left[i]
            sub &= sub - 1
        allowed = ((1 << r) - 1) ^ forbid
        if need == 0:
            # left alone sufficient
            res = [i+1 for i in range(l) if (lmask >> i) & 1]
            print("YES")
            print(*res)
            return
        # need independent subset of size need within allowed
        if need > r:
            continue
        # iterate over right independent subsets of required size
        for rmask in right_by_size.get(need, []):
            if rmask & ~allowed == 0:
                # found
                res = [i+1 for i in range(l) if (lmask >> i) & 1]
                for idx in range(r):
                    if (rmask >> idx) & 1:
                        res.append(right_ids[idx] + 1)
                print("YES")
                print(*res)
                return
    print("NO")

if __name__ == "__main__":
    solve()