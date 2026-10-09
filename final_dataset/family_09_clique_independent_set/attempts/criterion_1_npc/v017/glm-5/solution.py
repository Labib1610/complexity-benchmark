import sys

def solve():
    data = sys.stdin.read().split()
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
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    if k == 1:
        print("YES")
        print(1)
        return
    
    full = (1 << (n + 1)) - 1
    
    # Find a clique of size k in the complement graph
    # using Bron-Kerbosch with pivoting and early termination.
    
    best = [0]
    
    def bron_kerbosch(R, P, X):
        if len(R) == k:
            best[0] = R
            return True
        if len(R) + bin(P).count('1') < k:
            return False
        if P == 0 and X == 0:
            return False
        
        # Pivot selection
        union = P | X
        pivot = (union & -union).bit_length() - 1
        pivot_neighbors = adj[pivot]
        
        # Candidates = P \ N(pivot)
        candidates = P & ~pivot_neighbors
        
        while candidates:
            v = (candidates & -candidates).bit_length() - 1
            v_bit = 1 << v
            candidates ^= v_bit
            P ^= v_bit
            
            v_neighbors = adj[v]
            if bron_kerbosch(R | v_bit, P & ~v_neighbors, X & ~v_neighbors):
                return True
            
            X |= v_bit
        
        return False
    
    all_vertices = 0
    for i in range(1, n + 1):
        all_vertices |= 1 << i
    
    if bron_kerbosch(0, all_vertices, 0):
        print("YES")
        result = []
        for i in range(1, n + 1):
            if best[0] & (1 << i):
                result.append(str(i))
        print(' '.join(result))
    else:
        print("NO")

solve()