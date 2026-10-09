import sys
from itertools import product

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # Precompute for each vertex, the set of vertices that are NOT adjacent (excluding self)
    non_adj = [0] * n
    full = (1 << n) - 1
    for i in range(n):
        non_adj[i] = full ^ adj[i] ^ (1 << i)
    
    # Precompute for each vertex, the set of vertices adjacent to it (including self for convenience)
    adj_self = [0] * n
    for i in range(n):
        adj_self[i] = adj[i] | (1 << i)
    
    # Precompute for each vertex, the set of vertices NOT adjacent to it (including self)
    non_adj_self = [0] * n
    for i in range(n):
        non_adj_self[i] = full ^ adj[i]
    
    # Enumerate all maximal independent sets using Bron-Kerbosch with pivoting
    # We need all maximal independent sets
    maximal_independent_sets = []
    
    # Using iterative approach to avoid recursion depth issues (though n<=40, recursion is fine)
    # But let's use recursion with pivoting
    def bron_kerbosch(R, P, X):
        if P == 0 and X == 0:
            maximal_independent_sets.append(R)
            return
        # Choose pivot u from P | X that maximizes |P & non_adj_self[u]|
        PuX = P | X
        # Find vertex with max intersection
        pivot = -1
        max_count = -1
        temp = PuX
        while temp:
            v_bit = temp & (-temp)
            v = v_bit.bit_length() - 1
            count = bin(P & non_adj_self[v]).count('1')
            if count > max_count:
                max_count = count
                pivot = v
            temp ^= v_bit
        # Iterate over P & adj_self[pivot] (vertices NOT in non_adj of pivot, i.e., adjacent or self)
        # These are the vertices to branch on
        candidates = P & adj_self[pivot]
        temp = candidates
        while temp:
            v_bit = temp & (-temp)
            v = v_bit.bit_length() - 1
            newP = P & non_adj_self[v]
            newX = X & non_adj_self[v]
            bron_kerbosch(R | v_bit, newP, newX)
            P ^= v_bit
            X |= v_bit
            temp ^= v_bit
    
    bron_kerbosch(0, full, 0)
    
    # Now try all pairs of maximal independent sets for chambers 1 and 2
    # Chamber 3 is the complement
    best = None
    num_mis = len(maximal_independent_sets)
    
    for i in range(num_mis):
        S1 = maximal_independent_sets[i]
        for j in range(num_mis):
            S2 = maximal_independent_sets[j]
            if S1 & S2:
                continue
            S3 = full ^ S1 ^ S2
            # Check S3 is independent
            temp = S3
            valid = True
            while temp:
                v_bit = temp & (-temp)
                v = v_bit.bit_length() - 1
                if adj[v] & S3:
                    valid = False
                    break
                temp ^= v_bit
            if not valid:
                continue
            # Build assignment
            assign = [0] * n
            temp = S1
            while temp:
                v_bit = temp & (-temp)
                v = v_bit.bit_length() - 1
                assign[v] = 1
                temp ^= v_bit
            temp = S2
            while temp:
                v_bit = temp & (-temp)
                v = v_bit.bit_length() - 1
                assign[v] = 2
                temp ^= v_bit
            temp = S3
            while temp:
                v_bit = temp & (-temp)
                v = v_bit.bit_length() - 1
                assign[v] = 3
                temp ^= v_bit
            if best is None or assign < best:
                best = assign
    
    if best is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, best)))

solve()