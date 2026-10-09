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
    
    # Precompute popcount for integers up to 2^n
    popcount = [0] * (1 << n)
    for i in range(1, 1 << n):
        popcount[i] = popcount[i >> 1] + (i & 1)
    
    # Check if a set represented by bitmask is independent
    def is_independent(mask):
        bits = mask
        while bits:
            v_bit = bits & -bits
            v = (v_bit.bit_length() - 1)
            if adj[v + 1] & mask:
                return False
            bits ^= v_bit
        return True
    
    # Check if mask is a clique in complement graph (i.e., independent in original)
    # Using Bron-Kerbosch style pivot algorithm for maximum clique
    # All nodes are 0-indexed internally
    
    # Complement adjacency: two nodes are connected in complement if not connected in original
    # For efficiency, we use the original graph and check non-edges
    
    best_mask = 0
    
    def bronk(R, P, X):
        nonlocal best_mask
        if popcount[R] >= k:
            best_mask = R
            return True
        if P == 0 and X == 0:
            if popcount[R] > popcount[best_mask]:
                best_mask = R
            return
        
        # Pruning: if current R + all P cannot reach k, stop
        if popcount[R] + popcount[P] < k:
            return
        
        # Pivot selection: choose u in P|X with max degree in P
        # For pivot, we want to minimize branching
        # Choose u with maximum number of neighbors in P (in complement graph)
        # In complement graph, neighbors of u are nodes NOT connected to u in original
        # So we want u with max (P & ~adj[u+1])
        
        # Simple pivot: choose first node in P|X
        union = P | X
        if union:
            u_bit = union & -union
            u = u_bit.bit_length() - 1
            # Nodes to consider: P without neighbors of u in complement
            # Neighbors of u in complement = P & ~adj[u+1] (nodes in P not connected to u)
            # But we want P \ N_comp(u), which is P & adj[u+1]
            # Actually, in standard BK: we iterate over P \ N(u)
            # Here N_comp(u) = nodes in P that are NOT connected to u in original
            # So P \ N_comp(u) = P & adj[u+1] (nodes in P connected to u in original)
            candidates = P & adj[u + 1]
        else:
            candidates = P
        
        while candidates:
            v_bit = candidates & -candidates
            v = v_bit.bit_length() - 1
            candidates ^= v_bit
            
            # Neighbors of v in complement graph (within all nodes)
            # = nodes NOT connected to v in original graph
            # all_nodes = (1 << n) - 1
            # N_comp(v) = all_nodes ^ adj[v+1] ^ (1 << v)  (excluding v itself)
            # But we only care about intersection with P and X
            # N_comp_P = P & ~adj[v+1]  (nodes in P not connected to v)
            # N_comp_X = X & ~adj[v+1]  (nodes in X not connected to v)
            
            # Actually, for BK: R' = R | {v}, P' = P ∩ N(v), X' = X ∩ N(v)
            # Here N(v) is neighbors in complement graph
            N_comp_v = ((1 << n) - 1) ^ adj[v + 1] ^ (1 << v)
            
            if bronk(R | (1 << v), P & N_comp_v, X & N_comp_v):
                return True
            
            P ^= v_bit
            X |= v_bit
        
        return False
    
    all_nodes = (1 << n) - 1
    bronk(0, all_nodes, 0)
    
    if popcount[best_mask] >= k:
        print("YES")
        result = []
        mask = best_mask
        while mask:
            v_bit = mask & -mask
            v = v_bit.bit_length() - 1
            result.append(v + 1)
            mask ^= v_bit
        # Print first k nodes
        print(' '.join(map(str, result[:k])))
    else:
        print("NO")

solve()