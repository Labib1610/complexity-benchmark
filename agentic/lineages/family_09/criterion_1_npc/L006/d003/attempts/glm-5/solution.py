import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
    
    # Check if there exists an independent set of size k
    # Using meet-in-the-middle approach
    
    half_n = n // 2
    left_size = half_n
    right_size = n - half_n
    
    # Left part: vertices 1..left_size
    # Right part: vertices left_size+1..n
    
    # Precompute compatibility masks
    # mask_left[i] = set of vertices in left part compatible with vertex i
    # mask_right[i] = set of vertices in right part compatible with vertex i
    
    mask_left = [0] * (n + 1)
    mask_right = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # Vertices in left part compatible with i
        for j in range(1, left_size + 1):
            if (adj[i] >> (j - 1)) & 1 == 0:
                mask_left[i] |= 1 << (j - 1)
        # Vertices in right part compatible with i
        for j in range(left_size + 1, n + 1):
            if (adj[i] >> (j - 1)) & 1 == 0:
                mask_right[i] |= 1 << (j - half_n - 1)
    
    # Enumerate all independent sets in left part
    # left_sets[s] = list of independent sets with size s (as bitmask)
    left_sets = [[] for _ in range(left_size + 1)]
    left_sets[0].append(0)
    
    for v in range(1, left_size + 1):
        v_bit = 1 << (v - 1)
        # Compatible set within left part
        compat = mask_left[v] & ((1 << left_size) - 1)
        for sz in range(left_size, 0, -1):
            for S in left_sets[sz - 1]:
                if S & compat == S:  # S is compatible with v
                    left_sets[sz].append(S | v_bit)
    
    # For each size s, store the first independent set found
    left_found = [None] * (left_size + 1)
    for sz in range(left_size + 1):
        if left_sets[sz]:
            left_found[sz] = left_sets[sz][0]
    
    # Enumerate all independent sets in right part
    right_sets = [[] for _ in range(right_size + 1)]
    right_sets[0].append(0)
    
    for v in range(left_size + 1, n + 1):
        v_bit = 1 << (v - half_n - 1)
        compat = mask_right[v] & ((1 << right_size) - 1)
        for sz in range(right_size, 0, -1):
            for S in right_sets[sz - 1]:
                if S & compat == S:
                    right_sets[sz].append(S | v_bit)
    
    # For each size s, store the first independent set found
    right_found = [None] * (right_size + 1)
    for sz in range(right_size + 1):
        if right_sets[sz]:
            right_found[sz] = right_sets[sz][0]
    
    # Try to combine left and right parts
    # For each valid combination, check compatibility
    
    # Precompute for each left set, which right vertices are compatible
    # We need: for left set L, right set R must satisfy:
    # For all v in R, v is compatible with all vertices in L
    
    # For efficiency, precompute for each left set mask, the compatible right mask
    # left_compat_right[L] = bitmask of right vertices compatible with all vertices in L
    
    # But this might be expensive. Instead, iterate and check.
    
    # For each left_size l and right_size r where l + r == k
    for l in range(max(0, k - right_size), min(left_size, k) + 1):
        r = k - l
        if r < 0 or r > right_size:
            continue
        if left_found[l] is None or right_found[r] is None:
            continue
        
        # Check all combinations
        for L in left_sets[l]:
            # Compute compatible right mask for L
            compat_right = (1 << right_size) - 1
            for v in range(1, left_size + 1):
                if (L >> (v - 1)) & 1:
                    compat_right &= mask_right[v]
            
            for R in right_sets[r]:
                if R & compat_right == R:
                    # Found valid combination
                    result = []
                    for i in range(left_size):
                        if (L >> i) & 1:
                            result.append(i + 1)
                    for i in range(right_size):
                        if (R >> i) & 1:
                            result.append(left_size + i + 1)
                    print("YES")
                    print(' '.join(map(str, result)))
                    return
    
    print("NO")

solve()