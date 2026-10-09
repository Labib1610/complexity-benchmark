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
    
    # Precompute adjacency for 0-indexed nodes
    adj0 = [0] * n
    for i in range(1, n + 1):
        adj0[i-1] = adj[i]
    
    # Tomita algorithm for maximum clique
    best_size = 0
    best_clique_mask = 0
    
    def expand(R, P, depth):
        nonlocal best_size, best_clique_mask
        if R.bit_count() > best_size:
            best_size = R.bit_count()
            best_clique_mask = R
        
        # Upper bound: |R| + |P|
        if R.bit_count() + P.bit_count() <= best_size:
            return
        
        # Pivot selection
        # Choose u in P U X that maximizes |P intersect N(u)|
        # Here X is empty, so choose u in P
        # We want to maximize branching efficiency
        if P == 0:
            return
        
        # Find pivot
        pivot = -1
        max_neighbors = -1
        p_temp = P
        while p_temp:
            u = (p_temp & -p_temp).bit_length() - 1
            cnt = (P & adj0[u]).bit_count()
            if cnt > max_neighbors:
                max_neighbors = cnt
                pivot = u
            p_temp &= p_temp - 1
        
        # Candidates: P \ N(pivot)
        candidates = P & ~adj0[pivot]
        
        while candidates:
            # Select vertex with smallest degree in the subgraph (heuristic)
            v_bit = candidates & -candidates
            v = (v_bit.bit_length() - 1)
            
            new_R = R | v_bit
            new_P = P & adj0[v]
            
            expand(new_R, new_P, depth + 1)
            
            P &= ~v_bit
            candidates &= ~v_bit
    
    all_vertices_mask = (1 << n) - 1
    expand(0, all_vertices_mask, 0)
    
    if best_size >= k:
        result = []
        for i in range(n):
            if best_clique_mask & (1 << i):
                result.append(i + 1)
        print("YES")
        print(" ".join(map(str, result[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()