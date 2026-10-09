import sys
sys.setrecursionlimit(10000)

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
    
    # Greedy heuristic to find a large independent set
    def greedy_is():
        deg = [(bin(adj[i]).count('1'), i) for i in range(1, n + 1)]
        deg.sort()
        order = [x[1] for x in deg]
        iset = []
        used = [False] * (n + 1)
        for u in order:
            if not used[u]:
                iset.append(u)
                used[u] = True
                for v in range(1, n + 1):
                    if (adj[u] >> (v - 1)) & 1:
                        used[v] = True
        return iset
    
    iset = greedy_is()
    if len(iset) >= k:
        print("YES")
        print(" ".join(map(str, iset[:k])))
        return
    
    # Meet-in-the-middle
    half = n // 2
    L_size = half
    R_size = n - half
    
    # Precompute masks for left and right halves
    # L_mask[i] = conflicts of node i with nodes in L (1-indexed)
    # R_mask[i] = conflicts of node i with nodes in R (1-indexed)
    L_mask = [0] * (n + 1)
    R_mask = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (adj[i] >> (j - 1)) & 1:
                if j <= half:
                    L_mask[i] |= 1 << (j - 1)
                else:
                    R_mask[i] |= 1 << (j - half - 1)
    
    # Generate all independent sets in L
    # dp[mask] = size of largest independent set with this mask
    # We iterate through masks in increasing order
    dp = [0] * (1 << L_size)
    dp[0] = 0
    
    for mask in range(1, 1 << L_size):
        lsb = mask & -mask
        i = (lsb.bit_length() - 1) + 1  # node number (1-indexed in L)
        prev = mask ^ lsb
        # Check if i conflicts with any node in prev
        if (L_mask[i] & prev) == 0:
            dp[mask] = dp[prev] + 1
        else:
            dp[mask] = dp[prev]
    
    # Generate all independent sets in R
    # For each independent set in R, we need to find compatible set in L
    # best_L[mask] = mask with maximum dp[mask] that is compatible
    # We use DP to compute best_L for all masks
    
    best_L = [0] * (1 << L_size)
    best_L[0] = 0
    for mask in range(1, 1 << L_size):
        lsb = mask & -mask
        prev = mask ^ lsb
        if dp[mask] > dp[best_L[prev]]:
            best_L[mask] = mask
        else:
            best_L[mask] = best_L[prev]
    
    # Now iterate through all subsets of R
    # For each subset, check if it's independent and find compatible L
    for r_mask in range(1 << R_size):
        if r_mask == 0:
            # Only L
            if dp[best_L[(1 << L_size) - 1]] >= k:
                # Find the actual set
                full_mask = (1 << L_size) - 1
                best_mask = best_L[full_mask]
                # Reconstruct
                result = []
                for i in range(1, half + 1):
                    if (best_mask >> (i - 1)) & 1:
                        result.append(i)
                # We need exactly k, but dp gives max
                # Actually we need to find if any set of size k exists
                # Let's just output first k from the greedy or search
                # Actually we should search properly
                # Let me redo this part
                pass
            continue
        
        # Check if r_mask is independent
        ok = True
        temp = r_mask
        while temp:
            lsb = temp & -temp
            i = (lsb.bit_length() - 1) + 1  # node in R (1-indexed in R)
            actual_i = half + i
            # Check conflicts with other nodes in r_mask
            if (R_mask[actual_i] & (r_mask ^ lsb)) != 0:
                ok = False
                break
            temp ^= lsb
        
        if not ok:
            continue
        
        # r_mask is independent, find compatible L
        # L nodes that conflict with r_mask
        forbidden_L = 0
        temp = r_mask
        while temp:
            lsb = temp & -temp
            i = (lsb.bit_length() - 1) + 1
            actual_i = half + i
            forbidden_L |= L_mask[actual_i]
            temp ^= lsb
        
        allowed_L = ((1 << L_size) - 1) ^ forbidden_L
        best_L_mask = best_L[allowed_L]
        
        r_count = bin(r_mask).count('1')
        l_count = dp[best_L_mask]
        
        if l_count + r_count >= k:
            # Found! Reconstruct
            result = []
            for i in range(1, half + 1):
                if (best_L_mask >> (i - 1)) & 1:
                    result.append(i)
            for i in range(1, R_size + 1):
                if (r_mask >> (i - 1)) & 1:
                    result.append(half + i)
            print("YES")
            print(" ".join(map(str, result[:k])))
            return
    
    # Also check r_mask = 0 case
    best_L_mask = best_L[(1 << L_size) - 1]
    if dp[best_L_mask] >= k:
        result = []
        for i in range(1, half + 1):
            if (best_L_mask >> (i - 1)) & 1:
                result.append(i)
        print("YES")
        print(" ".join(map(str, result[:k])))
        return
    
    print("NO")

solve()