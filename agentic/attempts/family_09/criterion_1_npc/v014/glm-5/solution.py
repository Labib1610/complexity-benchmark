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
    for i in range(1, n + 1):
        adj[i] = (1 << i)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Pick k vertices, no two share an edge
    # Traditional meet-in-the-middle selection problem
    # n <= 46, so n1 + n2 <= 46
    
    # Greedy upper bound filter using Maximum Independent Set approximation
    # Use degeneracy ordering (smallest degree first) to find a greedy independent set
    cnt_nei = [0] * (n + 1)
    for i in range(1, n + 1):
        # count neighbors in original graph
        # we can use popcount on adj[i] mask, but adj[i] includes self bit
        # bit i is set in adj[i], so neighbor count = popcount - 1
        cnt_nei[i] = (adj[i].bit_count() - 1)
    
    # Repeatedly pick vertex with smallest degree, add to set, remove it and neighbors
    used = [False] * (n + 1)
    greedy_count = 0
    
    import heapq
    # Heap of (degree, vertex), but degree changes as we remove vertices
    # We'll just use a simple loop since n is small and we don't update heap
    # Instead: in each iteration, find unused vertex with minimum current degree
    
    # Copy of degree that we update
    deg = list(cnt_nei)
    
    for _ in range(n):
        # find unused vertex with minimum deg
        min_d = n + 1
        min_v = -1
        for v in range(1, n + 1):
            if not used[v] and deg[v] < min_d:
                min_d = deg[v]
                min_v = v
        
        # Add to independent set
        greedy_count += 1
        # Remove this vertex and its neighbors: mark used, decrease neighbors' degrees
        used[min_v] = True
        # Decrease neighbor degrees
        vmask = adj[min_v]
        # For each neighbor u of min_v that is not used yet, decrease deg[u]
        # Since we're just using this for upper bound, we do it simply
        for u in range(1, n + 1):
            if u != min_v and not used[u] and (vmask & (1 << u)):
                deg[u] -= 1
    
    # If greedy_count < k, impossible
    if greedy_count < k:
        print("NO")
        return
    
    # Split vertices
    n1 = n // 2
    n2 = n - n1
    
    # left vertices: 1..n1, right: n1+1..n
    left_vertices = list(range(1, n1 + 1))
    right_vertices = list(range(n1 + 1, n + 1))
    
    # Precompute masks for right vertices
    # right_masks[j] = bitmask of neighbors in right side (including self), for j in 0..n2-1
    right_masks = []
    for v in right_vertices:
        mask = (1 << v)  # self
        # neighbors in right side
        v_adj = adj[v]
        for u in right_vertices:
            if (v_adj & (1 << u)):
                mask |= (1 << u)
        right_masks.append(mask)
    
    # DP for right side: best[mask] = size of independent set
    # We use dictionary, but array is faster due to small n2
    # n2 <= 23, so array of size 2^n2
    right_size = 1 << n2
    best = [0] * right_size
    # best is already initialized to 0, meaning mask 0 has size 0
    
    # We need to fill best[mask] = max size independent set for mask
    # Standard DP: for each mask, try removing one vertex
    
    # But we actually want: given a mask (selected right vertices), what's max size?
    # best[mask] = max size independent set that is subset of selected vertices
    
    # Classic DP: iterate masks in increasing order
    # best[0] = 0
    for mask in range(1, right_size):
        # Find one bit
        # LSB
        lsb = mask & -mask
        idx = (lsb.bit_length() - 1)
        # Without idx
        prev = mask ^ lsb
        cand = best[prev]
        # With idx, check if valid
        # idx corresponds to vertex right_vertices[idx]
        # The vertex can be added if it has no conflicts with other vertices in prev
        # Conflict: if any other vertex u in prev is neighbor of right_vertices[idx]
        # We use precomputed conflict mask
        # right_conflict[idx] = bitmask of neighbors of right_vertices[idx] in right side
        # We can allow adding idx if (prev & right_conflict[idx]) == 0
        # But right_masks[idx] already includes self and neighbors
        # So: (prev & (right_masks[idx] ^ (1 << right_vertices[idx]))) == 0
        # Or simpler: check if (prev & right_masks[idx]) == 0? No, that's wrong because right_masks[idx] includes self
        
        # Let's compute conflict mask: neighbors only
        # But we can also compute it as: right_masks[idx] includes self and neighbors
        # The vertex at idx conflicts with vertices that are its neighbors
        # So: if we want to add vertex idx, we need that none of its neighbors are in prev
        # Neighbor mask of vertex idx (without self):
        v = right_vertices[idx]
        nei_mask = right_masks[idx] ^ (1 << v)  # neighbors only, in right side
        nei_mask_shifted = 0
        for j in range(n2):
            if (nei_mask & (1 << right_vertices[j])):
                nei_mask_shifted |= (1 << j)
        
        # But simpler: we can just AND prev with nei_mask_shifted
        # However, we need to convert nei_mask to local indexing
        
        # Alternative: precompute for each j, conflict_mask[j] = bitmask (in local indexing) of neighbors
        pass  # We'll precompute below
    
    # Precompute conflict masks for right side in local indexing
    conflict_right = [0] * n2
    for j in range(n2):
        v = right_vertices[j]
        # neighbors in right side
        c = 0
        for jj in range(n2):
            if jj != j and (adj[v] & (1 << right_vertices[jj])):
                c |= (1 << jj)
        conflict_right[j] = c
    
    # Now DP
    best = [0] * right_size
    for mask in range(1, right_size):
        lsb = mask & -mask
        j = (lsb.bit_length() - 1)
        prev = mask ^ lsb
        # Option 1: don't take j
        cand = best[prev]
        # Option 2: take j
        # Valid if no neighbor of j is in prev
        if (prev & conflict_right[j]) == 0:
            cand = max(cand, 1 + best[prev])
        best[mask] = cand
    
    # Also need to track which subsets achieve best[mask] for reconstruction
    # But since n is small, we can enumerate all subsets for left and right
    # Instead, let's just enumerate left subsets and check
    
    # Enumerate all subsets of left size k (independent sets)
    # Since n1 <= 23, enumerating all 2^n1 is fine
    
    left_size_enum = 1 << n1
    left_best = [0] * left_size_enum
    conflict_left = [0] * n1
    for j in range(n1):
        v = left_vertices[j]
        c = 0
        for jj in range(n1):
            if jj != j and (adj[v] & (1 << left_vertices[jj])):
                c |= (1 << jj)
        conflict_left[j] = c
    
    for mask in range(1, left_size_enum):
        lsb = mask & -mask
        j = (lsb.bit_length() - 1)
        prev = mask ^ lsb
        cand = left_best[prev]
        if (prev & conflict_left[j]) == 0:
            cand = max(cand, 1 + left_best[prev])
        left_best[mask] = cand
    
    # Now iterate over all subsets of left that are independent sets
    # For each with size s, we need a subset of right with size k-s that is independent
    # And also no edges between left and right
    
    # For each left independent set, compute the "forbidden mask" for right:
    # all right vertices that are neighbors of some left vertex in the set
    
    # We'll iterate over all masks, but only process those with left_best[mask] == popcount (i.e., independent)
    # Actually, left_best[mask] gives max independent within mask, we want mask itself to be independent
    
    # So condition: left_best[mask] == popcount(mask)
    # Or: mask & (for any j in mask, conflict_left[j]) == 0
    # Simpler: the mask is independent if for all j in mask, (mask ^ (1<<j)) & conflict_left[j] == 0
    # But checking left_best[mask] == popcount is easier after we compute
    
    # Precompute all right independent subsets grouped by size
    right_indep_by_size = [[] for _ in range(n2 + 1)]
    for mask in range(right_size):
        # Check if mask is independent
        # Check: for all j in mask, (mask ^ (1<<j)) & conflict_right[j] == 0
        m_temp = mask
        independent = True
        while m_temp:
            lsb = m_temp & -m_temp
            j = (lsb.bit_length() - 1)
            if ((mask ^ lsb) & conflict_right[j]) != 0:
                independent = False
                break
            m_temp ^= lsb
        if independent:
            sz = mask.bit_count()
            right_indep_by_size[sz].append(mask)
    
    # Iterate over left subsets
    for mask_left in range(left_size_enum):
        # Check if mask_left is independent
        m_temp = mask_left
        indep = True
        while m_temp:
            lsb = m_temp & -m_temp
            j = (lsb.bit_length() - 1)
            if ((mask_left ^ lsb) & conflict_left[j]) != 0:
                indep = False
                break
            m_temp ^= lsb
        if not indep:
            continue
        
        sz_left = mask_left.bit_count()
        if sz_left > k:
            continue
        
        need = k - sz_left
        if need > n2:
            continue
        
        # Compute forbidden mask for right
        forbidden_right_mask = 0  # global indexing
        ml = mask_left
        while ml:
            lsb = ml & -ml
            j = (lsb.bit_length() - 1)
            v = left_vertices[j]
            # neighbors in right side
            for jj in range(n2):
                if (adj[v] & (1 << right_vertices[jj])):
                    forbidden_right_mask |= (1 << jj)  # local indexing for right
            ml ^= lsb
        
        # Among right independent subsets of size "need", find one disjoint from forbidden
        for mask_right in right_indep_by_size[need]:
            if (mask_right & forbidden_right_mask) == 0:
                # Found solution
                result = []
                ml = mask_left
                while ml:
                    lsb = ml & -ml
                    j = (lsb.bit_length() - 1)
                    result.append(left_vertices[j])
                    ml ^= lsb
                mr = mask_right
                while mr:
                    lsb = mr & -mr
                    j = (lsb.bit_length() - 1)
                    result.append(right_vertices[j])
                    mr ^= lsb
                result.sort()
                print("YES")
                print(' '.join(map(str, result)))
                return
    
    print("NO")

solve()