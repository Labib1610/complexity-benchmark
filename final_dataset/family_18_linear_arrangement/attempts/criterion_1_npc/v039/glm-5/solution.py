import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    B = int(input_data[idx]); idx += 1
    
    adj = [0] * n
    edges = []
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        edges.append((u, v))
    
    full = (1 << n) - 1
    
    # Precompute cut sizes: cut[mask] = number of edges between mask and complement
    # cut[mask] = popcount(adj[v] & ~mask) for v in mask, but that double counts? No.
    # Each edge (u,v) with u in mask, v not in mask is counted once if we sum over u in mask.
    # But edges are stored in adj as bits, so adj[u] has v set. Sum over u in mask of popcount(adj[u] & ~mask).
    # This counts each crossing edge once (from the mask side).
    
    INF = float('inf')
    dp = [INF] * (1 << n)
    parent = [-1] * (1 << n)  # which server was added last
    
    dp[0] = 0
    
    for mask in range(1 << n):
        if dp[mask] == INF:
            continue
        # Try adding each server not in mask
        for u in range(n):
            if mask & (1 << u):
                continue
            new_mask = mask | (1 << u)
            # cut size of new_mask
            # edges from new_mask to complement
            comp = full ^ new_mask
            cut = 0
            # count edges from u to comp, plus edges from mask to comp
            # Actually cut(new_mask) = edges between new_mask and complement
            # = edges from mask to comp (excluding u) + edges from u to comp
            # But edges from mask to comp: for v in mask, adj[v] & comp
            # This is expensive to recompute each time.
            # Let's just compute cut(new_mask) directly.
            
            # Optimization: cut(new_mask) = cut(mask) - edges(u, mask) + edges(u, comp)
            # Because moving u from comp to mask: removes edges from u to mask (no longer crossing),
            # adds edges from u to comp (now crossing).
            # But we don't store cut(mask) in dp...
            
            # Let's precompute or compute on the fly
            # For small n this is fine
            cut = bin(adj[u] & comp).count('1')
            # Plus edges from mask to comp
            # This is the expensive part
            mm = mask
            c2 = 0
            while mm:
                v = (mm & -mm).bit_length() - 1
                c2 += bin(adj[v] & comp).count('1')
                mm &= mm - 1
            cut += c2
            
            new_cost = dp[mask] + cut
            if new_cost < dp[new_mask]:
                dp[new_mask] = new_cost
                parent[new_mask] = u
    
    if dp[full] <= B:
        # Reconstruct
        pos = [0] * n
        mask = full
        p = n
        while mask:
            u = parent[mask]
            pos[u] = p
            mask ^= (1 << u)
            p -= 1
        print("YES")
        print(' '.join(str(x) for x in pos))
    else:
        print("NO")

solve()