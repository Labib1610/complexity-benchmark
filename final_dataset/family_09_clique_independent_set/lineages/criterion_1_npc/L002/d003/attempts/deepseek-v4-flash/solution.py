import sys
from sys import stdin

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # Split into two halves
    n1 = n // 2
    n2 = n - n1

    # Enumerate independent sets for first half
    size1 = 1 << n1
    ind1 = []
    for mask in range(size1):
        ok = True
        for i in range(n1):
            if mask & (1 << i):
                # check if any neighbor in same half is also in mask
                if adj[i] & mask & ((1 << n1) - 1):
                    ok = False
                    break
        if ok:
            ind1.append(mask)
    # For each mask in first half, store max size for each possible size? Actually we need all sizes.
    # We'll store list of masks per size for first half
    by_size1 = [[] for _ in range(n1 + 1)]
    for mask in ind1:
        cnt = bin(mask).count("1")
        by_size1[cnt].append(mask)

    # Enumerate independent sets for second half
    size2 = 1 << n2
    ind2 = []
    for mask in range(size2):
        ok = True
        for i in range(n2):
            if mask & (1 << i):
                # actual vertex index = n1 + i
                if adj[n1 + i] & (mask << n1) & (((1 << n) - 1) ^ ((1 << n1) - 1)):
                    ok = False
                    break
        if ok:
            ind2.append(mask)
    by_size2 = [[] for _ in range(n2 + 1)]
    for mask in ind2:
        cnt = bin(mask).count("1")
        by_size2[cnt].append(mask)

    # For each mask in first half, compute forbidden mask in second half
    # forbidden = union of neighbors of selected vertices in first half that are in second half
    forbidden = [0] * (1 << n1)
    for mask in range(1 << n1):
        f = 0
        mm = mask
        while mm:
            lsb = mm & -mm
            i = (lsb.bit_length() - 1)
            f |= (adj[i] >> n1)
            mm -= lsb
        forbidden[mask] = f

    # Now combine: for each size s1 in first half, for each mask1, we need size s2 = k - s1
    # and mask2 in second half with (mask2 & forbidden[mask1]) == 0
    # We'll precompute for each forbidden mask the possible sizes and a representative mask
    # Since n2 <= 23, we can store for each mask2 its size, and for each forbidden value we can
    # iterate over all mask2 to find compatible ones. But that's 2^23 * 2^23 too big.
    # Instead, we can do: for each mask1, we need any mask2 with size k - s1 and mask2 & forbidden == 0.
    # We can precompute for each possible forbidden mask (0..2^n2-1) the list of sizes available
    # among masks2 that are subsets of complement of forbidden.
    # But forbidden can be many. Better: for each mask2, we can compute its "compatible" masks1?
    # Actually we can do: for each mask1, we need to know if there exists mask2 of size s2 with
    # mask2 & forbidden == 0. That is equivalent to: among all masks2 of size s2, is there one
    # that is subset of (~forbidden) & ((1<<n2)-1)?
    # We can precompute for each possible "allowed" mask (subset of second half) the maximum size
    # of independent set contained in it. But we need exact size, not max.
    # Since n2 <= 23, we can precompute for each mask2 its size, and for each possible allowed mask
    # we can store the set of sizes achievable by subsets of allowed that are independent.
    # That's 2^23 * 23 maybe okay? 8 million * 23 ~ 184M, might be heavy but okay in Python? Maybe not.
    # Better: use meet-in-the-middle with subset DP: For each mask2, we can compute its size.
    # For each mask1, we need to know if there is mask2 with size s2 and mask2 & forbidden == 0.
    # We can precompute for each possible "forbidden" value the list of sizes available among masks2
    # that are disjoint from forbidden. But forbidden can be any subset of second half.
    # We can do: for each mask2, we can mark for all subsets of its complement? That's too many.
    # Alternative: Since n2 <= 23, we can iterate over all mask2 for each mask1? That's 2^23 * 2^23 worst.
    # But n1 <= 23 too, so 2^23 * 2^23 = 2^46 too big.
    # We need smarter: For each mask1, we need to know if there exists mask2 of size s2 with mask2 & forbidden == 0.
    # We can precompute for each possible "allowed" mask (i.e., complement of forbidden) the maximum size
    # of independent set within it. But we need exact size, not max.
    # However, we can precompute for each mask2 its size, and then for each possible allowed mask,
    # we can compute the set of sizes achievable by independent subsets of allowed.
    # This can be done with SOS DP: For each mask, we can store a bitset of achievable sizes.
    # Since n2 <= 23, sizes up to 23, we can store a 24-bit integer where bit s is set if there exists
    # an independent set of size s that is a subset of mask.
    # Then for each mask1, allowed = (~forbidden[mask1]) & ((1<<n2)-1), we check if bit (k - s1) is set.
    # This is efficient: O(2^n2 * n2) for DP.

    # Build achievable sizes bitset for each mask in second half
    max_mask2 = 1 << n2
    size_bitset = [0] * max_mask2
    for mask in range(max_mask2):
        cnt = bin(mask).count("1")
        size_bitset[mask] = 1 << cnt

    # Now SOS DP: for each mask, we want to OR the bitsets of all submasks.
    # Standard subset sum DP:
    for i in range(n2):
        for mask in range(max_mask2):
            if mask & (1 << i):
                size_bitset[mask] |= size_bitset[mask ^ (1 << i)]

    # Now combine
    for s1 in range(n1 + 1):
        s2_needed = k - s1
        if s2_needed < 0 or s2_needed > n2:
            continue
        for mask1 in by_size1[s1]:
            allowed = (~forbidden[mask1]) & (max_mask2 - 1)
            if (size_bitset[allowed] >> s2_needed) & 1:
                # find a mask2
                for mask2 in by_size2[s2_needed]:
                    if mask2 & forbidden[mask1] == 0:
                        # construct answer
                        ans = []
                        for i in range(n1):
                            if mask1 & (1 << i):
                                ans.append(i + 1)
                        for i in range(n2):
                            if mask2 & (1 << i):
                                ans.append(n1 + i + 1)
                        print("YES")
                        print(" ".join(map(str, ans)))
                        return

    print("NO")

if __name__ == "__main__":
    solve()