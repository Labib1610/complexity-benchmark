import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    adj = [0] * (n + 1)
    idx = 3
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1])
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    if k == 1:
        print("YES")
        print(1)
        return
    
    if k > n:
        print("NO")
        return
    
    # complement adjacency: non-friends (excluding self)
    non_adj = [0] * (n + 1)
    full = (1 << (n + 1)) - 1
    for i in range(1, n + 1):
        non_adj[i] = full & ~adj[i] & ~1
    
    # DP over subsets: dp[mask] = True if mask is a clique in complement graph
    # We only need masks of size up to k
    # Use meet-in-the-middle or iterative approach
    
    # Since n <= 46, we use a different approach
    # Split into two halves
    
    half = n // 2
    left = list(range(1, half + 1))
    right = list(range(half + 1, n + 1))
    
    # For left half, enumerate all cliques
    left_cliques = []  # list of (mask, size)
    # We use recursive enumeration with pruning
    
    # Precompute non_adj restricted to left half
    left_mask = 0
    for v in left:
        left_mask |= 1 << v
    
    # Enumerate cliques in left half
    left_clique_list = []
    
    def enum_left(start_idx, current_mask, current_size, available):
        if current_size > 0:
            left_clique_list.append((current_mask, current_size))
        if current_size == k:
            return
        for i in range(start_idx, len(left)):
            v = left[i]
            new_avail = available & non_adj[v]
            if new_avail & (1 << v):
                enum_left(i + 1, current_mask | (1 << v), current_size + 1, new_avail)
    
    avail_left = 0
    for v in left:
        avail_left |= 1 << v
    enum_left(0, 0, 0, avail_left)
    
    # Check if any left clique has size k
    for mask, size in left_clique_list:
        if size == k:
            print("YES")
            result = []
            for i in range(1, n + 1):
                if mask & (1 << i):
                    result.append(i)
            print(' '.join(map(str, result)))
            return
    
    # For right half, enumerate all cliques
    right_clique_list = []
    
    right_mask = 0
    for v in right:
        right_mask |= 1 << v
    
    def enum_right(start_idx, current_mask, current_size, available):
        if current_size > 0:
            right_clique_list.append((current_mask, current_size))
        if current_size == k:
            return
        for i in range(start_idx, len(right)):
            v = right[i]
            new_avail = available & non_adj[v]
            if new_avail & (1 << v):
                enum_right(i + 1, current_mask | (1 << v), current_size + 1, new_avail)
    
    avail_right = 0
    for v in right:
        avail_right |= 1 << v
    enum_right(0, 0, 0, avail_right)
    
    # Check if any right clique has size k
    for mask, size in right_clique_list:
        if size == k:
            print("YES")
            result = []
            for i in range(1, n + 1):
                if mask & (1 << i):
                    result.append(i)
            print(' '.join(map(str, result)))
            return
    
    # Now combine: left clique of size s + right clique of size (k-s)
    # They must be fully connected in complement graph
    
    # Group right cliques by size
    right_by_size = {}
    for mask, size in right_clique_list:
        if size not in right_by_size:
            right_by_size[size] = []
        right_by_size[size].append(mask)
    
    # For each left clique, compute which right vertices are all non-adjacent to all left vertices
    for lmask, lsize in left_clique_list:
        if lsize >= k:
            continue
        need = k - lsize
        if need not in right_by_size:
            continue
        
        # Compute available right vertices: those non-adjacent to all in lmask
        avail = right_mask
        temp = lmask
        while temp:
            v = (temp & -temp).bit_length() - 1
            avail &= non_adj[v]
            temp &= temp - 1
        
        avail &= right_mask
        if bin(avail).count('1') < need:
            continue
        
        # Check if there's a right clique of size 'need' within avail
        for rmask in right_by_size[need]:
            if (rmask & avail) == rmask:
                print("YES")
                result = []
                for i in range(1, n + 1):
                    if (lmask | rmask) & (1 << i):
                        result.append(i)
                print(' '.join(map(str, result)))
                return
    
    print("NO")

solve()