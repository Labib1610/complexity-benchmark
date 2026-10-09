import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * n for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u][v] = True
        adj[v][u] = True
    
    # We need to find a valid 3-coloring.
    # Since n <= 40, we can use a meet-in-the-middle approach.
    # Split vertices into two halves A and B.
    # For each half, iterate all 3^n possible colorings.
    # For each coloring, check if it is valid within the half.
    # For valid colorings of A, store the set of colors used by vertices in B
    # that are adjacent to vertices in A.
    # Actually, for each vertex b in B, we need to know which colors are forbidden
    # based on the coloring of A.
    # Let's denote the coloring of A as c_A.
    # For each vertex b in B, the set of forbidden colors is {c_A[a] for a in A where (a, b) is an edge}.
    # We need to find c_A and c_B such that for all b in B, c_B[b] is not in forbidden(b, c_A).
    # And c_B is valid within B.
    
    # Let's split n into n1 and n2.
    n1 = n // 2
    n2 = n - n1
    
    # Map indices: 0..n1-1 are in A, n1..n-1 are in B.
    # We relabel B's vertices to 0..n2-1 for convenience.
    
    # Precompute adjacency for B
    # adj_b[i][j] indicates if original vertex n1+i and n1+j are connected.
    adj_b = [[False] * n2 for _ in range(n2)]
    for i in range(n2):
        for j in range(i + 1, n2):
            if adj[n1 + i][n1 + j]:
                adj_b[i][j] = True
                adj_b[j][i] = True
    
    # Precompute for each vertex in B, which vertices in A are connected.
    # conn_to_A[b] = list of indices a in A such that (a, n1+b) is an edge.
    conn_to_A = [[] for _ in range(n2)]
    for b in range(n2):
        for a in range(n1):
            if adj[a][n1 + b]:
                conn_to_A[b].append(a)
    
    # Iterate all colorings for A
    # For each valid c_A, compute a mask for B.
    # The mask for B is a tuple of integers, where mask[b] is a bitmask of forbidden colors for vertex b.
    # Colors are 1, 2, 3. We use bits 0, 1, 2 for colors 1, 2, 3.
    
    # Store valid colorings of A grouped by their mask on B.
    # mask is a tuple of n2 integers.
    # We can use a dictionary to map mask to list of valid c_A.
    # But mask is a tuple of n2 integers, which can be large.
    # Instead, we can use a hash map.
    
    # To optimize, we can encode the mask as a base-8 number or similar.
    # Since each mask[b] is in {0, 1, 2, 3, 4, 5, 6, 7} (subset of {1, 2, 3}), we can encode it in 3 bits.
    # Total bits for mask: 3 * n2 <= 3 * 20 = 60 bits, which fits in an integer.
    
    def encode_mask(mask_list):
        val = 0
        for x in mask_list:
            val = (val << 3) | x
        return val
    
    def decode_mask(val, length):
        mask_list = [0] * length
        for i in range(length - 1, -1, -1):
            mask_list[i] = val & 7
            val >>= 3
        return mask_list
    
    # Precompute powers of 3 for iterating colorings
    pow3 = [1] * (max(n1, n2) + 1)
    for i in range(1, len(pow3)):
        pow3[i] = pow3[i-1] * 3
    
    # Dictionary to store mask -> valid c_A
    # We only need to store one valid c_A for each mask.
    left_solutions = {}
    
    # Iterate all colorings of A
    for k in range(pow3[n1]):
        # Decode coloring
        c_A = [0] * n1
        temp = k
        valid_A = True
        for i in range(n1):
            c_A[i] = temp % 3
            temp //= 3
        
        # Check validity within A
        for i in range(n1):
            for j in range(i + 1, n1):
                if adj[i][j] and c_A[i] == c_A[j]:
                    valid_A = False
                    break
            if not valid_A:
                break
        
        if not valid_A:
            continue
        
        # Compute mask for B
        mask_list = [0] * n2
        for b in range(n2):
            forbidden = 0
            for a in conn_to_A[b]:
                forbidden |= (1 << c_A[a])
            mask_list[b] = forbidden
        
        encoded = encode_mask(mask_list)
        if encoded not in left_solutions:
            left_solutions[encoded] = k
    
    # Iterate all colorings of B
    for k in range(pow3[n2]):
        c_B = [0] * n2
        temp = k
        valid_B = True
        for i in range(n2):
            c_B[i] = temp % 3
            temp //= 3
        
        # Check validity within B
        for i in range(n2):
            for j in range(i + 1, n2):
                if adj_b[i][j] and c_B[i] == c_B[j]:
                    valid_B = False
                    break
            if not valid_B:
                break
        
        if not valid_B:
            continue
        
        # Compute required mask from A
        # For each b in B, c_B[b] must not be in forbidden colors.
        # So forbidden colors must be a subset of {0, 1, 2} \ {c_B[b]}.
        # We need to find a mask from left_solutions such that for all b, (mask[b] >> c_B[b]) & 1 == 0.
        
        # We can compute the required mask pattern.
        # Actually, we need to check if there exists a mask in left_solutions that is compatible.
        # Compatible means for all b, mask[b] does not contain c_B[b].
        
        # We can iterate all keys in left_solutions and check.
        # But the number of keys can be large.
        # However, the number of valid colorings of A is at most 3^20 ~ 3.4e9, but in practice much smaller.
        # But n1 <= 20, so 3^20 is too large to iterate all.
        # Wait, the problem says n <= 40. 3^20 is indeed too large.
        # We need a better approach.
        
        # Alternative: For each valid c_B, compute the required mask and check if it exists.
        # The required mask is: for each b, the forbidden colors must not include c_B[b].
        # So we need mask[b] such that (mask[b] & (1 << c_B[b])) == 0.
        # This is a constraint on mask.
        # We can iterate all masks in left_solutions and check.
        # But the number of masks can be large.
        
        # Optimization: We can use a trie or a hash set for masks.
        # But checking all masks is still slow.
        
        # Let's reconsider. The mask is determined by c_A.
        # For each b, mask[b] is the set of colors used by neighbors of b in A.
        # We need mask[b] to not contain c_B[b].
        # This is equivalent to: for all a in conn_to_A[b], c_A[a] != c_B[b].
        
        # So we can iterate all valid c_A and check if it is compatible with c_B.
        # But iterating all valid c_A is slow.
        
        # Let's use the meet-in-the-middle approach properly.
        # We store all valid c_A in a list.
        # For each valid c_B, we need to find a c_A such that for all b, for all a in conn_to_A[b], c_A[a] != c_B[b].
        # This is equivalent to: for all edges (a, b) with a in A and b in B, c_A[a] != c_B[b].
        
        # We can use a hash map to store valid c_A.
        # Key: for each b in B, the set of colors used by neighbors of b in A.
        # But this is exactly the mask.
        
        # So we need to find a mask such that for all b, mask[b] does not contain c_B[b].
        # We can iterate all masks in left_solutions and check.
        # Since the number of valid colorings of A is at most 3^20, but in practice much smaller due to constraints.
        # But in the worst case (no edges), it is 3^20.
        # We need to handle this.
        
        # Let's try to iterate all masks in left_solutions.
        # Since we only store one c_A for each mask, the number of masks is at most 3^n1.
        # But 3^20 is too large.
        
        # We need a different approach.
        # Let's use the fact that the graph is small (n <= 40).
        # We can use a recursive backtracking with pruning.
        # Or use a heuristic.
        
        # Actually, the meet-in-the-middle approach should work if we handle the matching efficiently.
        # Let's try to iterate all valid c_B and for each, iterate all valid c_A.
        # But we need to store valid c_A efficiently.
        
        # Let's store valid c_A in a list.
        # valid_A_list = []
        # for k in range(pow3[n1]):
        #     ... check validity ...
        #     if valid: valid_A_list.append(k)
        
        # Then for each valid c_B, iterate valid_A_list and check compatibility.
        # This is O(3^n1 * 3^n2) in the worst case, which is too slow.
        
        # We need to use the mask to prune.
        # Let's compute the mask for each valid c_A and store in a dictionary.
        # Then for each valid c_B, we compute the required mask and check if it exists.
        # But the required mask is not unique. We need to check if there exists a mask that is compatible.
        
        # Let's define compatibility:
        # mask_A is compatible with c_B if for all b, (mask_A[b] & (1 << c_B[b])) == 0.
        # We can iterate all masks in left_solutions and check.
        # But the number of masks can be large.
        
        # Let's try to use a different encoding.
        # For each b in B, we have a constraint on c_A: for all a in conn_to_A[b], c_A[a] != c_B[b].
        # This is a constraint on c_A.
        # We can use a SAT solver or a CSP solver.
        # But we need to implement it ourselves.
        
        # Let's use a recursive search with pruning.
        # We assign colors to vertices in A one by one.
        # For each assignment, we check if it is compatible with c_B.
        # If yes, we continue.
        # This is O(3^n1) in the worst case.
        
        # Let's implement this.
        
        # We need to find c_A such that:
        # 1. c_A is valid within A.
        # 2. For all edges (a, b) with a in A and b in B, c_A[a] != c_B[b].
        
        # We can use backtracking.
        # Let's define a recursive function.
        
        # But first, let's check if we can find a compatible mask in left_solutions.
        # We can iterate all masks in left_solutions and check.
        # Since the number of masks is at most 3^n1, and n1 <= 20, this is feasible.
        # Wait, 3^20 is 3.4e9, which is too large.
        
        # We need to reduce the number of masks.
        # We can use the fact that the graph is sparse.
        # But in the worst case, the graph is empty, and we have 3^20 masks.
        
        # Let's use a different approach.
        # We can use the fact that the number of edges is at most n(n-1)/2.
        # We can use a heuristic to find a valid coloring.
        
        # Let's use a greedy algorithm.
        # Assign colors to vertices one by one.
        # For each vertex, choose a color that is not used by its neighbors.
        # If no color is available, backtrack.
        
        # This is a standard graph coloring algorithm.
        # Let's implement it.
        
        # We need to handle the case where the graph is not 3-colorable.
        
        # Let's use a recursive function with pruning.
        
        # We'll use a global variable to store the coloring.
        coloring = [-1] * n
        
        def is_safe(v, c):
            for u in range(n):
                if adj[v][u] and coloring[u] == c:
                    return False
            return True
        
        def graph_coloring_util(v):
            if v == n:
                return True
            for c in range(3):
                if is_safe(v, c):
                    coloring[v] = c
                    if graph_coloring_util(v + 1):
                        return True
                    coloring[v] = -1
            return False
        
        if graph_coloring_util(0):
            print("YES")
            print(" ".join(str(x + 1) for x in coloring))
            return
        else:
            print("NO")
            return
    
    # If we reach here, no solution found
    print("NO")

solve()