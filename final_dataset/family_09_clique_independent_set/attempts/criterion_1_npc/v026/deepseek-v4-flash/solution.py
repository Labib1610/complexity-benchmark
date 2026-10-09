import sys
sys.setrecursionlimit(1000000)

def solve():
    n, m, k = map(int, sys.stdin.readline().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # If k is large, we can use complement: find clique of size n-k in complement graph
    # But here we'll do meet-in-the-middle for independent set.

    # Split vertices into two halves
    left_n = n // 2
    right_n = n - left_n
    left_mask = (1 << left_n) - 1
    right_mask = ((1 << right_n) - 1) << left_n

    # Precompute for each subset of left half whether it's independent
    left_size = 1 << left_n
    left_independent = [True] * left_size
    for mask in range(left_size):
        # check if any edge inside mask
        mm = mask
        while mm:
            v = (mm & -mm).bit_length() - 1
            mm ^= (1 << v)
            if (adj[v] & mask) != 0:
                left_independent[mask] = False
                break

    # For each subset of left half, store max independent subset size and its mask
    left_best = [0] * left_size
    left_best_mask = [0] * left_size
    for mask in range(left_size):
        if left_independent[mask]:
            left_best[mask] = bin(mask).count("1")
            left_best_mask[mask] = mask
        else:
            # remove one bit
            sub = mask
            best = 0
            best_m = 0
            while sub:
                lsb = sub & -sub
                prev = mask ^ lsb
                if left_best[prev] > best:
                    best = left_best[prev]
                    best_m = left_best_mask[prev]
                sub ^= lsb
            left_best[mask] = best
            left_best_mask[mask] = best_m

    # For right half, we need to consider all subsets and combine with left
    right_size = 1 << right_n
    right_independent = [True] * right_size
    for mask in range(right_size):
        # shift to actual bits
        actual = mask << left_n
        mm = mask
        while mm:
            v = (mm & -mm).bit_length() - 1
            mm ^= (1 << v)
            if (adj[left_n + v] & actual) != 0:
                right_independent[mask] = False
                break

    # For each right subset, compute its size and the set of left vertices that are not adjacent to any in it
    right_best = [0] * right_size
    right_best_mask = [0] * right_size
    for mask in range(right_size):
        if right_independent[mask]:
            sz = bin(mask).count("1")
            right_best[mask] = sz
            right_best_mask[mask] = mask
        else:
            sub = mask
            best = 0
            best_m = 0
            while sub:
                lsb = sub & -sub
                prev = mask ^ lsb
                if right_best[prev] > best:
                    best = right_best[prev]
                    best_m = right_best_mask[prev]
                sub ^= lsb
            right_best[mask] = best
            right_best_mask[mask] = best_m

    # Now combine: for each right subset that is independent, find allowed left mask
    # allowed left mask = all left vertices not adjacent to any vertex in right subset
    for rmask in range(right_size):
        if not right_independent[rmask]:
            continue
        # compute forbidden left bits
        forbidden = 0
        mm = rmask
        while mm:
            v = (mm & -mm).bit_length() - 1
            mm ^= (1 << v)
            forbidden |= adj[left_n + v] & left_mask
        allowed = left_mask & ~forbidden
        # We need total size = k
        need = k - bin(rmask).count("1")
        if need < 0 or need > left_n:
            continue
        # find if there is an independent subset of allowed of size exactly need
        # We can iterate over submasks of allowed, but that's too big.
        # Instead, we can precompute for each mask the max independent size and also check if any subset of allowed has size need.
        # We'll do DP over subsets: for each mask, store if there is an independent set of each size? That's too heavy.
        # But n<=46, left_n<=23, so we can enumerate all independent subsets of left half and store by size.
        # Let's do that: enumerate all independent subsets of left half, store by size.
        pass

    # Better approach: enumerate all independent sets in left half, store by size.
    left_sets_by_size = [[] for _ in range(left_n + 1)]
    for mask in range(left_size):
        if left_independent[mask]:
            left_sets_by_size[bin(mask).count("1")].append(mask)

    # Enumerate all independent sets in right half
    right_sets_by_size = [[] for _ in range(right_n + 1)]
    for mask in range(right_size):
        if right_independent[mask]:
            right_sets_by_size[bin(mask).count("1")].append(mask)

    # For each right set, compute forbidden left mask
    # We'll try all right sets and see if we can find left set of needed size
    for rsize in range(min(k, right_n) + 1):
        need = k - rsize
        if need < 0 or need > left_n:
            continue
        for rmask in right_sets_by_size[rsize]:
            # compute forbidden left
            forbidden = 0
            mm = rmask
            while mm:
                v = (mm & -mm).bit_length() - 1
                mm ^= (1 << v)
                forbidden |= adj[left_n + v] & left_mask
            allowed = left_mask & ~forbidden
            # check if any left independent set of size need is subset of allowed
            for lmask in left_sets_by_size[need]:
                if (lmask & ~allowed) == 0:
                    # found
                    ans = []
                    for i in range(left_n):
                        if lmask >> i & 1:
                            ans.append(i + 1)
                    for i in range(right_n):
                        if rmask >> i & 1:
                            ans.append(left_n + i + 1)
                    print("YES")
                    print(" ".join(map(str, ans)))
                    return
    print("NO")

if __name__ == "__main__":
    solve()