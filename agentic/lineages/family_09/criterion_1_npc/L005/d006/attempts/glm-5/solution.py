import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    deg = [0] * (n + 1)
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        deg[u] += 1
        deg[v] += 1
    
    # Precompute adjacency bitmasks
    adj = [0] * (n + 1)
    for u, v in edges:
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))
    
    # Precompute popcount for 16-bit integers
    popcount16 = [0] * 65536
    for i in range(1, 65536):
        popcount16[i] = popcount16[i >> 1] + (i & 1)
    
    def popcount(x):
        return popcount16[x & 0xFFFF] + popcount16[(x >> 16) & 0xFFFF]
    
    # Split into two halves
    n1 = n // 2
    n2 = n - n1
    
    # Generate all subsets of first half
    subsets1 = []
    for mask in range(1 << n1):
        cnt = popcount(mask)
        if cnt > k:
            continue
        T = 0
        for i in range(n1):
            if mask & (1 << i):
                T += deg[i + 1]
        # Count edges within first half
        e_in = 0
        for i in range(n1):
            if mask & (1 << i):
                e_in += popcount(mask & adj[i + 1])
        e_in //= 2
        subsets1.append((mask, cnt, T, e_in))
    
    # Group by (cnt, T, e_in)
    from collections import defaultdict
    groups1 = defaultdict(list)
    for mask, cnt, T, e_in in subsets1:
        groups1[(cnt, T, e_in)].append(mask)
    
    # Generate all subsets of second half
    subsets2 = []
    for mask in range(1 << n2):
        cnt = popcount(mask)
        if cnt > k:
            continue
        T = 0
        for i in range(n2):
            if mask & (1 << i):
                T += deg[n1 + i + 1]
        # Count edges within second half
        e_in = 0
        for i in range(n2):
            if mask & (1 << i):
                e_in += popcount(mask & adj[n1 + i + 1])
        e_in //= 2
        subsets2.append((mask, cnt, T, e_in))
    
    # For each subset of second half, compute cross edges
    for mask2, cnt2, T2, e_in2 in subsets2:
        # Compute cross edges
        cross = 0
        for i in range(n2):
            if mask2 & (1 << i):
                v = n1 + i + 1
                cross += popcount(adj[v] & ((1 << n1) - 1))
        
        # For each subset of first half
        for mask1, cnt1, T1, e_in1 in subsets1:
            if cnt1 + cnt2 != k:
                continue
            
            T = T1 + T2
            target = m + 4 * T
            
            # Total edges with c=2: e_in1 + e_in2 + cross_edges
            # cross_edges = edges between selected in first half and selected in second half
            cross_edges = 0
            for i in range(n1):
                if mask1 & (1 << i):
                    u = i + 1
                    # Count selected vertices in second half adjacent to u
                    cross_edges += popcount((adj[u] >> n1) & mask2)
            
            total_c2 = e_in1 + e_in2 + cross_edges
            total_c1 = T - 2 * total_c2
            total_c0 = m - total_c1 - total_c2
            
            score = total_c0 * 1 + total_c1 * 5 + total_c2 * 25
            
            if score == target:
                # Found solution
                result = []
                for i in range(n1):
                    if mask1 & (1 << i):
                        result.append(i + 1)
                for i in range(n2):
                    if mask2 & (1 << i):
                        result.append(n1 + i + 1)
                result.sort()
                print("YES")
                print(" ".join(map(str, result)))
                return
    
    print("NO")

solve()