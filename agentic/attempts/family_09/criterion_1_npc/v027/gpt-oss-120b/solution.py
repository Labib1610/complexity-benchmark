import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    edges = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges[u].append(v)
        edges[v].append(u)

    n1 = n // 2
    n2 = n - n1
    # masks for left part (0..n1-1) and right part (n1..n-1)
    left_adj = [0] * n1          # adjacency within left
    left_cross = [0] * n1        # adjacency to right (bits 0..n2-1)
    for i in range(n1):
        mask = 0
        cross = 0
        for v in edges[i]:
            if v < n1:
                mask |= 1 << v
            else:
                cross |= 1 << (v - n1)
        left_adj[i] = mask
        left_cross[i] = cross

    right_adj = [0] * n2
    for i in range(n2):
        v_global = n1 + i
        mask = 0
        for v in edges[v_global]:
            if v >= n1:
                mask |= 1 << (v - n1)
        right_adj[i] = mask

    # enumerate independent subsets of left
    size_left = 1 << n1
    indep_left = [False] * size_left
    left_sz = [0] * size_left
    left_cross_mask = [0] * size_left
    indep_left[0] = True
    for mask in range(1, size_left):
        lsb = mask & -mask
        v = (lsb.bit_length() - 1)
        prev = mask ^ lsb
        if indep_left[prev] and (left_adj[v] & prev) == 0:
            indep_left[mask] = True
            left_sz[mask] = left_sz[prev] + 1
            left_cross_mask[mask] = left_cross_mask[prev] | left_cross[v]
        else:
            indep_left[mask] = False

    # enumerate independent subsets of right, store f[mask]=size or -1
    size_right = 1 << n2
    f = [-1] * size_right
    f[0] = 0
    for mask in range(1, size_right):
        lsb = mask & -mask
        v = (lsb.bit_length() - 1)
        prev = mask ^ lsb
        if f[prev] != -1 and (right_adj[v] & prev) == 0:
            f[mask] = f[prev] + 1
        else:
            f[mask] = -1

    # SOS DP for max independent subset size in submasks
    g = f[:]                     # max size
    best_sub = [-1] * size_right # submask achieving g
    for mask in range(size_right):
        if f[mask] != -1:
            best_sub[mask] = mask
    for i in range(n2):
        for mask in range(size_right):
            if mask & (1 << i):
                sub = mask ^ (1 << i)
                if g[sub] > g[mask]:
                    g[mask] = g[sub]
                    best_sub[mask] = best_sub[sub]

    full_right_mask = (1 << n2) - 1
    # search
    for mask in range(size_left):
        if not indep_left[mask]:
            continue
        szL = left_sz[mask]
        need = k - szL
        if need < 0:
            continue
        allowed = full_right_mask ^ left_cross_mask[mask]
        if g[allowed] < need:
            continue
        # find a right submask with exact needed size
        sub = allowed
        found_sub = -1
        while True:
            if f[sub] == need:
                found_sub = sub
                break
            if sub == 0:
                break
            sub = (sub - 1) & allowed
        if found_sub == -1:
            # fallback: take best_sub (may be larger) and trim arbitrarily
            sub = best_sub[allowed]
            # trim to needed size
            cur = sub
            # remove vertices until size matches need
            while f[cur] > need:
                lsb = cur & -cur
                cur ^= lsb
                # recompute size quickly
                # we can just decrement count
                # but easier: recompute via f (since cur is independent)
                # ensure f[cur] != -1
                if f[cur] == -1:
                    # shouldn't happen
                    pass
            found_sub = cur
        # construct answer
        ans = []
        for i in range(n1):
            if mask & (1 << i):
                ans.append(i + 1)
        for i in range(n2):
            if found_sub & (1 << i):
                ans.append(n1 + i + 1)
        print("YES")
        print(' '.join(map(str, ans[:k])))
        return

    print("NO")

if __name__ == "__main__":
    solve()