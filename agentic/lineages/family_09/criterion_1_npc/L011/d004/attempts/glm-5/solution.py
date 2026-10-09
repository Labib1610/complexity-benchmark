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
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))
    
    # Precompute popcount for numbers up to 2^n - 1
    # We'll use built-in bit_count() in Python 3.8+
    
    # Split into two halves
    n1 = n // 2
    n2 = n - n1
    
    # Enumerate all subsets of first half
    # For each subset, compute:
    # - size (number of elements)
    # - internal edges (edges within the subset)
    # - boundary edges (edges from subset to second half)
    
    # For each subset of first half, store (size, internal_edges, boundary_edges)
    # boundary_edges[u] = edges from subset to vertex u in second half
    
    # We'll use dictionaries to store valid configurations
    # Key: (size, internal_edges), Value: list of (boundary_mask, subset_mask)
    
    # Actually, let's think differently
    # x^T L x = sum(D[i] * x[i]) - sum(A[i][j] * x[i] * x[j])
    #         = sum(d[i] * x[i]) - 2 * (edges within selected)
    # where d[i] = degree of vertex i
    
    # Valid if: sum(d[i] * x[i]) - 2 * E_in = sum(d[i] * x[i])
    # So: E_in = 0
    # The selected vertices must form an independent set!
    
    # So we need to find an independent set of size k
    
    # Use meet-in-the-middle for finding independent set
    # Split vertices into two halves
    # For each subset of first half, check if it's independent
    # For each subset of second half, check if it's independent
    # Then combine: no edges between the two subsets
    
    # Map for first half: size -> list of (mask, forbidden_mask_in_second_half)
    # forbidden_mask_in_second_half = vertices in second half that are adjacent to any vertex in the subset
    
    half1_size = n1
    half2_size = n2
    
    # Vertices 1..n1 are in first half, vertices n1+1..n are in second half
    # For a vertex v in first half, adj_to_half2[v] = mask of neighbors in second half
    
    adj_to_half2 = [0] * (n1 + 1)  # 1-indexed for first half
    adj_in_half1 = [0] * (n1 + 1)  # neighbors within first half
    
    for v in range(1, n1 + 1):
        neighbors = adj[v]
        # Neighbors in first half (vertices 1..n1)
        adj_in_half1[v] = neighbors & ((1 << n1) - 1)
        # Neighbors in second half (vertices n1+1..n)
        adj_to_half2[v] = neighbors >> n1
    
    adj_in_half2 = [0] * (n2 + 1)  # 0-indexed for second half
    adj_to_half1 = [0] * (n2 + 1)  # neighbors in first half
    
    for v in range(n2):
        actual_v = n1 + 1 + v  # vertex number
        neighbors = adj[actual_v]
        # Neighbors in first half
        adj_to_half1[v] = neighbors & ((1 << n1) - 1)
        # Neighbors in second half (shifted to 0-indexed)
        adj_in_half2[v] = (neighbors >> n1) & ((1 << n2) - 1)
    
    # Enumerate all subsets of first half
    # half1_subsets[size] = list of (mask, forbidden_mask)
    half1_subsets = [[] for _ in range(n1 + 1)]
    
    for mask in range(1 << n1):
        # Check if independent set
        is_independent = True
        for v in range(n1):
            if mask & (1 << v):
                # Check if any neighbor in first half is also in mask
                if mask & adj_in_half1[v + 1]:
                    is_independent = False
                    break
        
        if is_independent:
            size = mask.bit_count()
            # Compute forbidden mask in second half
            forbidden = 0
            for v in range(n1):
                if mask & (1 << v):
                    forbidden |= adj_to_half2[v + 1]
            half1_subsets[size].append((mask, forbidden))
    
    # Enumerate all subsets of second half
    # half2_subsets[size] = list of (mask, forbidden_mask)
    half2_subsets = [[] for _ in range(n2 + 1)]
    
    for mask in range(1 << n2):
        # Check if independent set
        is_independent = True
        for v in range(n2):
            if mask & (1 << v):
                # Check if any neighbor in second half is also in mask
                if mask & adj_in_half2[v]:
                    is_independent = False
                    break
        
        if is_independent:
            size = mask.bit_count()
            # Compute forbidden mask in first half
            forbidden = 0
            for v in range(n2):
                if mask & (1 << v):
                    forbidden |= adj_to_half1[v]
            half2_subsets[size].append((mask, forbidden))
    
    # Now find combination: size1 + size2 = k, and no conflicts
    for size1 in range(min(k, n1) + 1):
        size2 = k - size1
        if size2 < 0 or size2 > n2:
            continue
        
        # For each subset of first half with size1
        for mask1, forbidden1 in half1_subsets[size1]:
            # For each subset of second half with size2
            for mask2, forbidden2 in half2_subsets[size2]:
                # Check if no conflicts
                # mask1 should not intersect with forbidden2
                # mask2 should not intersect with forbidden1
                if (mask1 & forbidden2) == 0 and (mask2 & forbidden1) == 0:
                    # Found valid independent set
                    result = []
                    for v in range(n1):
                        if mask1 & (1 << v):
                            result.append(v + 1)
                    for v in range(n2):
                        if mask2 & (1 << v):
                            result.append(n1 + 1 + v)
                    print("YES")
                    print(" ".join(map(str, result)))
                    return
    
    print("NO")

solve()