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

    nL = n // 2
    nR = n - nL
    left_ids = list(range(nL))
    right_ids = list(range(nL, n))

    # masks relative to halves
    left_adj = [0] * nL
    right_adj = [0] * nR
    # neighbours inside the same half
    for i in range(nL):
        mask = 0
        for j in range(nL):
            if adj[i] >> j & 1:
                mask |= 1 << j
        left_adj[i] = mask
    for i in range(nR):
        v = nL + i
        mask = 0
        for j in range(nR):
            if adj[v] >> (nL + j) & 1:
                mask |= 1 << j
        right_adj[i] = mask

    # enumerate independent subsets of left half
    left_subs = []
    for mask in range(1 << nL):
        ok = True
        # check internal edges
        # fast: for each vertex present, ensure no neighbour also present
        mm = mask
        while mm:
            v = (mm & -mm).bit_length() - 1
            if left_adj[v] & mask:
                ok = False
                break
            mm &= mm - 1
        if ok:
            left_subs.append((mask, mask.bit_count()))
    # enumerate independent subsets of right half
    sizeR = 1 << nR
    best = [-1] * sizeR
    rep = [0] * sizeR
    for mask in range(1 << nR):
        ok = True
        mm = mask
        while mm:
            v = (mm & -mm).bit_length() - 1
            if right_adj[v] & mask:
                ok = False
                break
            mm &= mm - 1
        if ok:
            sz = mask.bit_count()
            best[mask] = sz
            rep[mask] = mask

    # SOS DP to propagate best to supersets
    for i in range(nR):
        bit = 1 << i
        for mask in range(sizeR):
            if mask & bit:
                prev = mask ^ bit
                if best[prev] > best[mask]:
                    best[mask] = best[prev]
                    rep[mask] = rep[prev]

    allRMask = (1 << nR) - 1

    # precompute neighbour mask from left vertex to right half
    left_to_right = [0] * nL
    for i in range(nL):
        nb = 0
        for j in range(nR):
            if adj[i] >> (nL + j) & 1:
                nb |= 1 << j
        left_to_right[i] = nb

    for maskL, szL in left_subs:
        need = k - szL
        if need < 0:
            continue
        # compute forbidden vertices in right half
        forbid = 0
        mm = maskL
        while mm:
            v = (mm & -mm).bit_length() - 1
            forbid |= left_to_right[v]
            mm &= mm - 1
        allowed = allRMask ^ forbid
        if best[allowed] >= need:
            # we have a solution
            # take left vertices
            ans = []
            mm = maskL
            while mm:
                v = (mm & -mm).bit_length() - 1
                ans.append(v + 1)          # back to 1‑based
                mm &= mm - 1
            # take right vertices from rep[allowed], possibly trim
            maskR = rep[allowed]
            taken = 0
            while taken < need:
                v = (maskR & -maskR).bit_length() - 1
                ans.append(nL + v + 1)
                maskR &= maskR - 1
                taken += 1
            # output
            print("YES")
            print(' '.join(map(str, ans)))
            return

    print("NO")

if __name__ == "__main__":
    solve()