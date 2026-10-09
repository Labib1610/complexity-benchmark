import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # Split vertices into two halves
    left_n = n // 2
    right_n = n - left_n

    left_vertices = list(range(left_n))
    right_vertices = list(range(left_n, n))

    # Precompute for left half: for each subset, check if independent and store size
    left_size = 1 << left_n
    left_independent = [False] * left_size
    left_independent[0] = True
    for mask in range(1, left_size):
        # pick lowest set bit
        lsb = mask & -mask
        v = (lsb.bit_length() - 1)
        prev = mask ^ lsb
        if left_independent[prev] and (adj[v] & prev) == 0:
            left_independent[mask] = True

    # For right half, we need to know for each subset its size and the set of left vertices it conflicts with
    right_size = 1 << right_n
    right_info = []  # list of (size, conflict_mask_left)
    for mask in range(right_size):
        # check independence within right half
        ok = True
        conflict = 0
        # check each bit
        mm = mask
        while mm:
            lsb = mm & -mm
            v = (lsb.bit_length() - 1) + left_n
            # conflict with left
            conflict |= (adj[v] & ((1 << left_n) - 1))
            # check with other right bits already in mask
            if adj[v] & (mask ^ lsb):
                ok = False
                break
            mm ^= lsb
        if ok:
            right_info.append((mask.bit_count(), conflict))

    # Group right subsets by size, and for each size keep minimal conflict mask? Actually we need to find a left subset
    # that is independent and has no conflict with right subset.
    # We'll store for each right subset its size and conflict mask.
    # Then for each left independent subset, we need a right subset of size k - left_size_count
    # with conflict mask disjoint from left subset.

    # Precompute best right subset for each size and conflict mask? n<=46, right_n<=23, so right subsets <= 8 million? Actually 2^23 = 8.3M, too big to store all.
    # But we can do meet-in-the-middle: enumerate left independent subsets, and for each, search right subsets of needed size with no conflict.
    # Since right_n <= 23, we can enumerate all right subsets and store by size and conflict mask? That's too many.
    # Instead, we can do a recursive search on right half with pruning.

    # But n <= 46, so left_n <= 23, right_n <= 23. 2^23 = 8.3M, feasible to enumerate all right subsets and store by size.
    # For each size, we can store a list of conflict masks. Then for a given left mask, we need a right conflict mask that is disjoint.
    # We can precompute for each size a "minimum conflict mask" in terms of subset? Actually we need disjointness, so we can store for each size
    # a list of conflict masks, and for a query left mask, check if any conflict mask has zero intersection.

    # To speed up, for each size, we can store a boolean array of possible conflict masks? That's 2^23 per size, too much.
    # But we can use a trick: for each size, store a list of conflict masks, and for query, iterate over them. Worst case 8M per query, too slow.

    # Better: Use meet-in-the-middle with splitting into two halves of ~23 each, and for each half enumerate all independent subsets.
    # For left half, store by size a list of masks (the subset itself).
    # For right half, store by size a list of masks.
    # Then for each left subset of size a, we need right subset of size k-a that is independent and has no edges between halves.
    # We can precompute for each right subset its conflict mask with left half.
    # Then for each left subset, we need a right subset of size k-a with conflict mask disjoint from left subset.

    # Since right_n <= 23, we can enumerate all right subsets (2^23 = 8.3M) and store for each size a list of (mask, conflict).
    # That's 8.3M entries, each storing two ints, memory ~ 8.3M * 8 bytes = 66 MB, okay.

    right_by_size = [[] for _ in range(right_n + 1)]
    for mask in range(right_size):
        # check independence
        ok = True
        conflict = 0
        mm = mask
        while mm:
            lsb = mm & -mm
            v = (lsb.bit_length() - 1) + left_n
            conflict |= (adj[v] & ((1 << left_n) - 1))
            if adj[v] & (mask ^ lsb):
                ok = False
                break
            mm ^= lsb
        if ok:
            right_by_size[mask.bit_count()].append((mask, conflict))

    # Now enumerate left independent subsets
    left_by_size = [[] for _ in range(left_n + 1)]
    for mask in range(left_size):
        if left_independent[mask]:
            left_by_size[mask.bit_count()].append(mask)

    # For each left size a, we need right size b = k - a
    for a in range(min(k, left_n) + 1):
        b = k - a
        if b < 0 or b > right_n:
            continue
        for left_mask in left_by_size[a]:
            # need right subset with conflict disjoint from left_mask
            for right_mask, conflict in right_by_size[b]:
                if (conflict & left_mask) == 0:
                    # found
                    ans = []
                    for i in range(left_n):
                        if left_mask >> i & 1:
                            ans.append(i + 1)
                    for i in range(right_n):
                        if right_mask >> i & 1:
                            ans.append(i + 1 + left_n)
                    print("YES")
                    print(" ".join(map(str, ans)))
                    return

    print("NO")

if __name__ == "__main__":
    solve()