import sys
from itertools import combinations

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))
    
    # Precompute popcount for n-bit integers
    popcount = [0] * (1 << n)
    for i in range(1, 1 << n):
        popcount[i] = popcount[i >> 1] + (i & 1)
    
    # Function to calculate the equilibrium value for a mask
    # Equilibrium value = Kinetic - Potential = sum(3^(Su+Sv) - 1 - 2*(Su+Sv))
    # For Su+Sv = 0: 3^0 - 1 - 0 = 0
    # For Su+Sv = 1: 3^1 - 1 - 2 = 0
    # For Su+Sv = 2: 3^2 - 1 - 4 = 4
    # So we just need to count edges with both ends activated
    def get_val(mask):
        cnt = 0
        # Iterate over nodes in mask
        m_temp = mask
        while m_temp:
            lsb = m_temp & -m_temp
            u = (lsb.bit_length() - 1)  # 0-based index
            # neighbors in mask
            cnt += popcount[adj[u + 1] & mask]
            m_temp -= lsb
        return cnt // 2
    
    # Split and meet-in-the-middle
    n1 = n // 2
    n2 = n - n1
    
    # Precompute values for first half
    # Map: (popcount, value) -> list of masks
    map1 = {}
    for mask in range(1 << n1):
        c = popcount[mask]
        if c > k:
            continue
        # Calculate value contribution from edges within first half
        val = 0
        m_temp = mask
        while m_temp:
            lsb = m_temp & -m_temp
            u = (lsb.bit_length() - 1)  # 0-based index in first half
            val += popcount[adj[u + 1] & mask]
            m_temp -= lsb
        val //= 2
        key = (c, val)
        if key not in map1:
            map1[key] = []
        map1[key].append(mask)
    
    # For second half
    # We need: c1 + c2 = k, and val1 + val2 + cross_edges = 0
    # cross_edges = edges between mask1 and mask2
    
    # Precompute for each mask2: its popcount, internal value, and cross-edge counts with first half nodes
    # cross_edges[mask2][u] = 1 if node u (in first half) is connected to any node in mask2
    
    # Actually, let's iterate over mask2 and check
    for mask2 in range(1 << n2):
        c2 = popcount[mask2]
        c1_needed = k - c2
        if c1_needed < 0 or c1_needed > n1:
            continue
        
        # Calculate internal value for mask2
        val2 = 0
        m_temp = mask2
        while m_temp:
            lsb = m_temp & -m_temp
            u2 = (lsb.bit_length() - 1)  # 0-based index in second half
            # actual node index is n1 + u2 + 1
            actual_u = n1 + u2 + 1
            # neighbors in mask2 (shifted)
            val2 += popcount[(adj[actual_u] >> n1) & mask2]
            m_temp -= lsb
        val2 //= 2
        
        # Calculate cross edges: for each node in mask2, count edges to nodes in first half
        # We need: val1 + val2 + cross_edges = 0
        # So val1 = -val2 - cross_edges
        
        # Compute cross_edges for this mask2
        cross_edges = 0
        m_temp = mask2
        while m_temp:
            lsb = m_temp & -m_temp
            u2 = (lsb.bit_length() - 1)
            actual_u = n1 + u2 + 1
            # neighbors in first half
            cross_edges += popcount[adj[actual_u] & ((1 << n1) - 1)]
            m_temp -= lsb
        
        # But wait, cross_edges should be edges between mask1 and mask2
        # We need to know which specific nodes in first half are connected to mask2
        # Let's compute a bitmask of first-half nodes connected to mask2
        connected_mask = 0
        m_temp = mask2
        while m_temp:
            lsb = m_temp & -m_temp
            u2 = (lsb.bit_length() - 1)
            actual_u = n1 + u2 + 1
            connected_mask |= (adj[actual_u] & ((1 << n1) - 1))
            m_temp -= lsb
        
        # Now for a given mask1, cross_edges = popcount[mask1 & connected_mask]
        # We need: val1 + val2 + popcount[mask1 & connected_mask] = 0
        
        # For each possible mask1 with c1_needed nodes, we need to find one where
        # val1 + popcount[mask1 & connected_mask] = -val2
        
        # Let's iterate over mask1 candidates
        key = (c1_needed, None)  # We'll filter by value
        # Actually, let's just iterate through map1 entries
        for (c1, v1), masks1 in map1.items():
            if c1 != c1_needed:
                continue
            for mask1 in masks1:
                cross = popcount[mask1 & connected_mask]
                if v1 + val2 + cross == 0:
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

if __name__ == "__main__":
    solve()