import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    full = (1 << (n + 1)) - 1
    # complement adjacency (within vertices 1..n)
    comp = [0] * (n + 1)
    for i in range(1, n + 1):
        comp[i] = full ^ adj[i] ^ (1 << i)
    
    # Precompute popcount for masks up to 2^(n+1)
    size = 1 << (n + 1)
    popcnt = [0] * size
    for i in range(1, size):
        popcnt[i] = popcnt[i >> 1] + (i & 1)
    
    # Find first maximal independent set (greedy by min degree)
    def find_mis(start_mask):
        mask = start_mask
        result = 0
        while mask:
            best = -1
            best_deg = 10**9
            m2 = mask
            while m2:
                v = (m2 & -m2).bit_length() - 1
                m2 &= m2 - 1
                deg = popcnt[adj[v] & mask]
                if deg < best_deg:
                    best_deg = deg
                    best = v
            if best == -1:
                break
            result |= 1 << best
            mask &= comp[best]
        return result
    
    mask_all = (1 << (n + 1)) - 2  # vertices 1..n
    S1 = find_mis(mask_all)
    rem1 = mask_all ^ S1
    S2 = find_mis(rem1)
    rem2 = rem1 ^ S2
    S3 = rem2
    
    if S1 | S2 | S3 != mask_all:
        print("NO")
        return
    
    color = [0] * (n + 1)
    for v in range(1, n + 1):
        if S1 & (1 << v):
            color[v] = 1
        elif S2 & (1 << v):
            color[v] = 2
        else:
            color[v] = 3
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()