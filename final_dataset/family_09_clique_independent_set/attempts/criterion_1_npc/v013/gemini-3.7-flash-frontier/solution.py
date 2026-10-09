import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    # 0-indexed vertices for bit operations
    adj = [0] * n
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        idx += 2
        
    all_mask = (1 << n) - 1
    # indep_adj[u] is the bitmask of non-neighbors of u (excluding u itself)
    indep_adj = [all_mask ^ adj[u] ^ (1 << u) for u in range(n)]
    
    ans = None
    
    def bron_kerbosch(R, P, X):
        nonlocal ans
        if ans is not None:
            return
        if len(R) == k:
            ans = list(R)
            return
        if len(R) + P.bit_count() < k:
            return
        
        # Choose pivot u in P | X that maximizes |P & indep_adj[u]|
        # (which minimizes the branching factor |P \ indep_adj[u]|)
        p_or_x = P | X
        best_u = -1
        max_count = -1
        
        temp = p_or_x
        while temp:
            lsb = temp & -temp
            u = lsb.bit_length() - 1
            cnt = (P & indep_adj[u]).bit_count()
            if cnt > max_count:
                max_count = cnt
                best_u = u
            temp ^= lsb
            
        # Candidates to branch on: P \ indep_adj[best_u]
        branch_candidates = P & ~indep_adj[best_u]
        
        while branch_candidates:
            if ans is not None:
                return
            lsb = branch_candidates & -branch_candidates
            v = lsb.bit_length() - 1
            
            R.append(v + 1)
            bron_kerbosch(R, P & indep_adj[v], X & indep_adj[v])
            R.pop()
            
            P ^= (1 << v)
            X |= (1 << v)
            branch_candidates ^= lsb

    bron_kerbosch([], (1 << n) - 1, 0)
    
    if ans is not None:
        print("YES")
        print(*(ans[:k]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()