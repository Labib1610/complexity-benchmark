import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    triplets = []
    idx = 2
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2])
        idx += 3
        triplets.append((a, b, c))
    
    target = 3 * k * (k + 1) // 2
    
    by_a = [[] for _ in range(k+1)]
    for i, (a, b, c) in enumerate(triplets):
        by_a[a].append(i)
    
    full_mask = (1 << k) - 1
    
    # Precompute masks for each triplet
    masks = []
    for (a, b, c) in triplets:
        masks.append((1 << (b-1)) | (1 << (c-1)))
    
    # Precompute popcount
    popcount = [0] * (1 << k)
    for i in range(1, 1 << k):
        popcount[i] = popcount[i >> 1] + (i & 1)
    
    # DP: dp[mask_b][mask_c] = (prev_a, triplet_index) or None
    # We use dictionary for sparse representation
    # But k <= 22, so 2^22 is too large for array. Use dict.
    
    # Actually, we can use the fact that we process a from 1 to k
    # and at step a, mask_b and mask_c have exactly a-1 bits set.
    
    # Use dict: key = (mask_b, mask_c), value = (triplet_index, parent_key)
    # But this might be too slow. Let's try.
    
    # Optimization: since at step a, mask_b and mask_c have a-1 bits,
    # we can use a dict keyed by (mask_b << k) | mask_c
    
    # Initialize
    dp = {0: (None, None, 0)}  # key -> (triplet_idx, parent_key, sum)
    
    for a in range(1, k+1):
        new_dp = {}
        candidates = by_a[a]
        for key, (prev_idx, parent_key, cur_sum) in dp.items():
            mask_b = key >> k
            mask_c = key & ((1 << k) - 1)
            for ti in candidates:
                m = masks[ti]
                mb = m >> (k) if k > 0 else 0  # wrong, masks is (1<<(b-1))|(1<<(c-1))
                # Actually masks[ti] = (1<<(b-1)) | (1<<(c-1)), need to separate
                # But b and c can be same, so we can't separate from mask alone
                # We need to store b and c separately
                pass
        # The above approach has issue: we can't separate b and c from combined mask
        # Let's redo with separate masks
    
    # Redo: store mask_b and mask_c separately in key
    # key = (mask_b << k) | mask_c, but we need to know b and c separately for each triplet
    
    # Precompute b_mask and c_mask for each triplet
    b_masks = []
    c_masks = []
    for (a, b, c) in triplets:
        b_masks.append(1 << (b-1))
        c_masks.append(1 << (c-1))
    
    dp = {0: (None, None, 0)}
    
    for a in range(1, k+1):
        new_dp = {}
        candidates = by_a[a]
        for key, (prev_idx, parent_key, cur_sum) in dp.items():
            mask_b = key >> k
            mask_c = key & ((1 << k) - 1)
            for ti in candidates:
                bm = b_masks[ti]
                cm = c_masks[ti]
                if (mask_b & bm) or (mask_c & cm):
                    continue
                new_mask_b = mask_b | bm
                new_mask_c = mask_c | cm
                new_key = (new_mask_b << k) | new_mask_c
                new_sum = cur_sum + triplets[ti][0] + triplets[ti][1] + triplets[ti][2]
                if new_key not in new_dp:
                    new_dp[new_key] = (ti, key, new_sum)
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    # Find valid end state
    final_key = (full_mask << k) | full_mask
    if final_key not in dp:
        print("NO")
        return
    
    # Check sum
    cur = dp[final_key]
    if cur[2] != target:
        print("NO")
        return
    
    # Reconstruct
    result = []
    key = final_key
    while key != 0:
        ti, parent_key, _ = dp[key]
        result.append(triplets[ti])
        key = parent_key
    
    print("YES")
    for (a, b, c) in result:
        print(f"{a} {b} {c}")

solve()