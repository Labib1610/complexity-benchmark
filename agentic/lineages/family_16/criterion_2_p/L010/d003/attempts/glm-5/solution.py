import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    lenses = []
    for _ in range(j):
        d1 = int(next(it))
        d2 = int(next(it))
        lenses.append((d1, d2))
    
    # Sort by d1 in descending order
    lenses.sort(key=lambda x: -x[0])
    
    # Compute prefix sums of d1
    prefix_d1 = [0] * (j + 1)
    for i in range(j):
        prefix_d1[i + 1] = prefix_d1[i] + lenses[i][0]
    
    # Compute suffix max of (d1 + d2)
    suffix_max_d1d2 = [0] * (j + 1)
    for i in range(j - 1, -1, -1):
        suffix_max_d1d2[i] = max(lenses[i][0] + lenses[i][1], suffix_max_d1d2[i + 1])
    
    # Compute suffix max of d2
    suffix_max_d2 = [0] * (j + 1)
    for i in range(j - 1, -1, -1):
        suffix_max_d2[i] = max(lenses[i][1], suffix_max_d2[i + 1])
    
    ans = float('inf')
    for k in range(1, j + 1):
        # First k lenses have d1 >= d1_k, remaining j-k have d1 < d1_k
        # For first k: Y_i = X_i + d1_i, X_{i+1} = X_i + d1_i
        # So X_k = sum of first k d1's, Y_k = X_k + d1_k
        # Y_k + d2_k = X_k + d1_k + d2_k = prefix_d1[k] + d1_k + d2_k
        # Max over first k: prefix_d1[k] + max(d1 + d2)
        val1 = prefix_d1[k] + suffix_max_d1d2[0] if k == j else prefix_d1[k] + suffix_max_d1d2[0]
        # Actually for first k lenses, we need max of (d1 + d2) among them
        # suffix_max_d1d2[0] is max over all, but we need max over first k
        # Let's compute differently
        max_d1d2_first_k = suffix_max_d1d2[0]  # This is wrong, need to recompute
        
    # Recompute properly
    # For first k lenses (indices 0 to k-1), max of (d1 + d2)
    # We can compute prefix max
    prefix_max_d1d2 = [0] * (j + 1)
    for i in range(j):
        prefix_max_d1d2[i + 1] = max(prefix_max_d1d2[i], lenses[i][0] + lenses[i][1])
    
    ans = float('inf')
    for k in range(1, j + 1):
        # Option 1: max Y_i + d2_i comes from first k lenses
        # For lens i in first k: Y_i + d2_i = prefix_d1[i] + d1_i + d2_i
        # We need max over i in [1, k] of (prefix_d1[i] + d1_i + d2_i)
        # Since prefix_d1 is increasing and we want max, we need to track this
        
        # Option 2: max Y_i + d2_i comes from remaining j-k lenses
        # For these, Y_i = Y_k + sum_{t=k+1}^{i} d2_t = Y_k + (prefix_d2[i] - prefix_d2[k])
        # Y_k = prefix_d1[k] + d1_k (for lens k)
        # So Y_i + d2_i = prefix_d1[k] + d1_k + prefix_d2[i] - prefix_d2[k] + d2_i
        #               = prefix_d1[k] + d1_k - prefix_d2[k] + (prefix_d2[i] + d2_i)
        # We need max over i in [k+1, j] of (prefix_d2[i] + d2_i)
        
        # Let's compute prefix_d2 and prefix_max_pd2_d2
        pass
    
    # Let me restart with cleaner approach
    # Compute necessary arrays
    prefix_d1 = [0] * (j + 1)
    for i in range(j):
        prefix_d1[i + 1] = prefix_d1[i] + lenses[i][0]
    
    # For first k lenses, compute max of (prefix_d1[i] + d1_i + d2_i) for i in [1, k]
    # prefix_d1[i] + d1_i + d2_i = prefix_d1[i-1] + d1_i + d1_i + d2_i = prefix_d1[i-1] + 2*d1_i + d2_i
    # Hmm, let's just compute directly
    prefix_max_option1 = [0] * (j + 1)
    for i in range(1, j + 1):
        val = prefix_d1[i] + lenses[i-1][0] + lenses[i-1][1]  # Y_i + d2_i for lens i
        prefix_max_option1[i] = max(prefix_max_option1[i-1], val)
    
    # For remaining lenses (indices k+1 to j), we need prefix sums of d2
    prefix_d2 = [0] * (j + 1)
    for i in range(j):
        prefix_d2[i + 1] = prefix_d2[i] + lenses[i][1]
    
    # For remaining lenses, Y_i + d2_i = Y_k + (prefix_d2[i] - prefix_d2[k]) + d2_i
    # Y_k = prefix_d1[k] + d1_k (for lens k)
    # So Y_i + d2_i = prefix_d1[k] + d1_k + prefix_d2[i] - prefix_d2[k] + d2_i
    #               = prefix_d1[k] + d1_k - prefix_d2[k] + prefix_d2[i] + d2_i
    # We need max over i in [k+1, j] of (prefix_d2[i] + d2_i)
    
    # Compute suffix max of (prefix_d2[i] + d2_i)
    suffix_max_pd2_d2 = [0] * (j + 2)
    for i in range(j, 0, -1):
        val = prefix_d2[i] + lenses[i-1][1]
        suffix_max_pd2_d2[i] = max(val, suffix_max_pd2_d2[i + 1])
    
    ans = float('inf')
    for k in range(1, j + 1):
        # Option 1: max from first k lenses
        opt1 = prefix_max_option1[k]
        
        # Option 2: max from remaining j-k lenses
        if k < j:
            Y_k = prefix_d1[k] + lenses[k-1][0]
            # Y_i + d2_i = Y_k + prefix_d2[i] - prefix_d2[k] + d2_i
            #            = Y_k - prefix_d2[k] + prefix_d2[i] + d2_i
            # Max over i in [k+1, j] of (prefix_d2[i] + d2_i)
            max_pd2_d2 = suffix_max_pd2_d2[k + 1]
            opt2 = Y_k - prefix_d2[k] + max_pd2_d2
            ans = min(ans, max(opt1, opt2))
        else:
            ans = min(ans, opt1)
    
    print(ans)

solve()