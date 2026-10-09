import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj = [0]*n
    for _ in range(m):
        u = int(next(it))-1
        v = int(next(it))-1
        adj[u] |= 1<<v
        adj[v] |= 1<<u

    if k==0:
        print("YES")
        print()
        return

    half = n//2
    left_n = half
    right_n = n - half
    left_adj = [0]*left_n
    right_adj = [0]*right_n
    cross_adj_left = [0]*left_n   # neighbors in right side
    cross_adj_right = [0]*right_n  # neighbors in left side

    for i in range(left_n):
        left_adj[i] = adj[i] & ((1<<left_n)-1)
        cross_adj_left[i] = (adj[i] >> left_n) & ((1<<right_n)-1)
    for i in range(right_n):
        idx = i+left_n
        right_adj[i] = (adj[idx] >> left_n) & ((1<<right_n)-1)
        cross_adj_right[i] = adj[idx] & ((1<<left_n)-1)

    # enumerate independent subsets in right side
    right_by_size = [[] for _ in range(right_n+1)]
    for mask in range(1<<right_n):
        # check independence
        ok = True
        # fast check using adjacency
        # iterate bits
        sub = mask
        while sub:
            v = (sub & -sub).bit_length()-1
            if (right_adj[v] & mask):
                ok = False
                break
            sub &= sub-1
        if ok:
            sz = mask.bit_count()
            right_by_size[sz].append(mask)

    # for quick lookup, store masks as set per size
    right_sets = [set(lst) for lst in right_by_size]

    # enumerate left subsets and try to match
    for mask in range(1<<left_n):
        szL = mask.bit_count()
        if szL > k:
            continue
        # independence check left
        ok = True
        sub = mask
        while sub:
            v = (sub & -sub).bit_length()-1
            if (left_adj[v] & mask):
                ok = False
                break
            sub &= sub-1
        if not ok:
            continue
        need = k - szL
        # compute forbidden vertices in right due to edges crossing
        forbid = 0
        sub = mask
        while sub:
            v = (sub & -sub).bit_length()-1
            forbid |= cross_adj_left[v]
            sub &= sub-1
        allowed = ((1<<right_n)-1) ^ forbid
        # need an independent right subset of size need within allowed
        for rmask in right_by_size[need]:
            if rmask & ~allowed == 0:
                # construct answer
                ans = []
                # left vertices
                sub = mask
                while sub:
                    v = (sub & -sub).bit_length()-1
                    ans.append(v+1)
                    sub &= sub-1
                # right vertices
                sub = rmask
                while sub:
                    v = (sub & -sub).bit_length()-1
                    ans.append(v+1+left_n)
                    sub &= sub-1
                print("YES")
                print(' '.join(map(str, ans)))
                return
    print("NO")

if __name__ == "__main__":
    solve()