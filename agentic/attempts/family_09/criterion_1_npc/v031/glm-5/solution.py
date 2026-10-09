from collections import defaultdict

def solve():
    import sys
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1
    
    adj = [0] * n
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    half = n // 2
    left_size = half
    right_size = n - half
    
    # Left vertices: 0..left_size-1
    # Right vertices: left_size..n-1, remapped to 0..right_size-1
    
    # For left: enumerate independent sets
    left_sets_by_size = defaultdict(list)
    
    def enum_left(pos, mask, size):
        if pos == left_size:
            left_sets_by_size[size].append(mask)
            return
        enum_left(pos + 1, mask, size)
        if (mask & adj[pos]) == 0:
            enum_left(pos + 1, mask | (1 << pos), size + 1)
    
    enum_left(0, 0, 0)
    
    # For right: enumerate independent sets
    # For each, compute forbidden_left_mask (left vertices adjacent to this set)
    # Group by forbidden_left_mask, keep max size and one example
    
    right_best = {}  # forbidden_left_mask -> (max_size, right_mask)
    
    def remap_right(v):
        return v - left_size
    
    def enum_right(pos, rmask, size, forbidden_left):
        if pos == n:
            key = forbidden_left
            if key not in right_best or size > right_best[key][0]:
                right_best[key] = (size, rmask)
            return
        enum_right(pos + 1, rmask, size, forbidden_left)
        rv = remap_right(pos)
        if (rmask & (1 << rv)) == 0:
            new_forbidden = forbidden_left | adj[pos] & ((1 << left_size) - 1)
            enum_right(pos + 1, rmask | (1 << rv), size + 1, new_forbidden)
    
    enum_right(half, 0, 0, 0)
    
    # For each left set, find compatible right set
    for lsize, left_sets in left_sets_by_size.items():
        if lsize > k:
            continue
        need = k - lsize
        for lmask in left_sets:
            # Need right set with forbidden_left_mask & lmask == 0 and size >= need
            # But we need exactly 'need'... we stored max size, but we need exactly need
            # Actually we need at least need, but we need exactly k total
            # Hmm, we need exactly need from right
            pass
    
    # Problem: we need exactly k, but stored max. Need to store all sizes.
    # Let me redo: group by (forbidden_left_mask, size) -> right_mask
    
    right_by_key = {}  # (forbidden_left, size) -> right_mask
    
    def enum_right2(pos, rmask, size, forbidden_left):
        if pos == n:
            key = (forbidden_left, size)
            if key not in right_by_key:
                right_by_key[key] = rmask
            return
        enum_right2(pos + 1, rmask, size, forbidden_left)
        rv = remap_right(pos)
        if (rmask & (1 << rv)) == 0:
            new_forbidden = forbidden_left | (adj[pos] & ((1 << left_size) - 1))
            enum_right2(pos + 1, rmask | (1 << rv), size + 1, new_forbidden)
    
    enum_right2(half, 0, 0, 0)
    
    # Index by forbidden_left for faster lookup
    right_index = defaultdict(dict)  # forbidden_left -> {size: rmask}
    for (fl, sz), rmask in right_by_key.items():
        right_index[fl][sz] = rmask
    
    for lsize in range(k + 1):
        if lsize not in left_sets_by_size:
            continue
        need = k - lsize
        for lmask in left_sets_by_size[lsize]:
            # Find right set with forbidden_left & lmask == 0 and size == need
            for fl, sizes in right_index.items():
                if (fl & lmask) == 0 and need in sizes:
                    rmask = sizes[need]
                    result = []
                    for i in range(left_size):
                        if lmask & (1 << i):
                            result.append(i + 1)
                    for i in range(right_size):
                        if rmask & (1 << i):
                            result.append(left_size + i + 1)
                    print("YES")
                    print(' '.join(map(str, result)))
                    return
    
    print("NO")

solve()