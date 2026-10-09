```python
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
    
    # Precompute forbidden masks for each vertex
    forbidden = [0] * (n + 1)
    for v in range(1, n + 1):
        f = 0
        av = adj[v]
        while av:
            b = av & (-av)
            u = b.bit_length() - 1
            f |= 1 << u
            av ^= b
        forbidden[v] = f
    
    # Precompute popcount
    popcnt = [0] * (1 << n)
    for i in range(1, 1 << n):
        popcnt[i] = popcnt[i >> 1] + (i & 1)
    
    # Precompute bit positions
    bits = []
    for mask in range(1 << n):
        b = []
        m2 = mask
        while m2:
            bb = m2 & (-m2)
            b.append(bb.bit_length() - 1)
            m2 ^= bb
        bits.append(b)
    
    # Precompute complement
    full = (1 << n) - 1
    comp = [0] * (1 << n)
    for mask in range(1 << n):
        comp[mask] = full ^ mask
    
    # Precompute independent sets
    is_indep = [False] * (1 << n)
    is_indep[0] = True
    for mask in range(1, 1 << n):
        low = mask & (-mask)
        v = low.bit_length() - 1
        rest = mask ^ low
        if is_indep[rest] and (forbidden[v+1] & rest) == 0:
            is_indep[mask] = True
    
    # Precompute max independent set in subgraph
    mis = [0] * (1 << n)
    for mask in range(1, 1 << n):
        low = mask & (-mask)
        v = low.bit_length() - 1
        rest = mask ^ low
        cand1 = mis[rest]
        cand2 = 1 + mis[rest & comp[1 << v]]
        mis[mask] = cand1 if cand1 > cand2 else cand2
    
    # Check if 3-colorable
    if mis[full] > n - 3:
        print("NO")
        return
    
    # Precompute color1 candidates
    color1_cand = []
    for mask in range(1 << n):
        if is_indep[mask] and mis[comp[mask]] <= n - 3 - popcnt[mask]:
            color1_cand.append(mask)
    
    # Precompute color2 candidates
    color2_cand = []
    for mask in range(1 << n):
        if is_indep[mask] and mis[comp[mask]] <= n - 3 - popcnt[mask]:
            color2_cand.append(mask)
    
    # Precompute color3 candidates
    color3_cand = []
    for mask in range(1 << n):
        if is_indep[mask] and popcnt[mask] >= 3:
            color3_cand.append(mask)
    
    # Precompute color2 candidates by remaining
    color2_by_rem = [[] for _ in range(1 << n)]
    for mask in color2_cand:
        color2_by_rem[comp[mask]].append(mask)
    
    # Precompute color3 candidates by remaining
    color3_by_rem = [[] for _ in range(1 << n)]
    for mask in color3_cand:
        color3_by_rem[comp[mask]].append(mask)
    
    # Precompute color1 candidates by remaining
    color1_by_rem = [[] for _ in range(1 << n)]
    for mask in color1_cand:
        color1_by_rem[comp[mask]].append(mask)
    
    # Precompute color2 candidates by mask
    color2_by_mask = [[] for _ in range(1 << n)]
    for mask in color2_cand:
        color2_by_mask[mask].append(mask)
    
    # Precompute color3 candidates by mask
    color3_by_mask = [[] for _ in range(1 << n)]
    for mask in color3_cand:
        color3_by_mask[mask].append(mask)
    
    # Precompute color1 candidates by mask
    color1_by_mask = [[] for _ in range(1 << n)]
    for mask in color1_cand:
        color1_by_mask[mask].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask:
            color2_by_rem_mask[key] = []
        color2_by_rem_mask[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask:
            color3_by_rem_mask[key] = []
        color3_by_rem_mask[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask:
            color1_by_rem_mask[key] = []
        color1_by_rem_mask[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask2 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask2:
            color2_by_rem_mask2[key] = []
        color2_by_rem_mask2[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask2 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask2:
            color3_by_rem_mask2[key] = []
        color3_by_rem_mask2[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask2 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask2:
            color1_by_rem_mask2[key] = []
        color1_by_rem_mask2[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask3 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask3:
            color2_by_rem_mask3[key] = []
        color2_by_rem_mask3[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask3 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask3:
            color3_by_rem_mask3[key] = []
        color3_by_rem_mask3[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask3 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask3:
            color1_by_rem_mask3[key] = []
        color1_by_rem_mask3[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask4 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask4:
            color2_by_rem_mask4[key] = []
        color2_by_rem_mask4[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask4 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask4:
            color3_by_rem_mask4[key] = []
        color3_by_rem_mask4[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask4 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask4:
            color1_by_rem_mask4[key] = []
        color1_by_rem_mask4[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask5 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask5:
            color2_by_rem_mask5[key] = []
        color2_by_rem_mask5[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask5 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask5:
            color3_by_rem_mask5[key] = []
        color3_by_rem_mask5[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask5 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask5:
            color1_by_rem_mask5[key] = []
        color1_by_rem_mask5[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask6 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask6:
            color2_by_rem_mask6[key] = []
        color2_by_rem_mask6[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask6 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask6:
            color3_by_rem_mask6[key] = []
        color3_by_rem_mask6[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask6 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask6:
            color1_by_rem_mask6[key] = []
        color1_by_rem_mask6[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask7 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask7:
            color2_by_rem_mask7[key] = []
        color2_by_rem_mask7[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask7 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask7:
            color3_by_rem_mask7[key] = []
        color3_by_rem_mask7[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask7 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask7:
            color1_by_rem_mask7[key] = []
        color1_by_rem_mask7[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask8 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask8:
            color2_by_rem_mask8[key] = []
        color2_by_rem_mask8[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask8 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask8:
            color3_by_rem_mask8[key] = []
        color3_by_rem_mask8[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask8 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask8:
            color1_by_rem_mask8[key] = []
        color1_by_rem_mask8[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask9 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask9:
            color2_by_rem_mask9[key] = []
        color2_by_rem_mask9[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask9 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask9:
            color3_by_rem_mask9[key] = []
        color3_by_rem_mask9[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask9 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask9:
            color1_by_rem_mask9[key] = []
        color1_by_rem_mask9[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask10 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask10:
            color2_by_rem_mask10[key] = []
        color2_by_rem_mask10[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask10 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask10:
            color3_by_rem_mask10[key] = []
        color3_by_rem_mask10[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask10 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask10:
            color1_by_rem_mask10[key] = []
        color1_by_rem_mask10[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask11 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask11:
            color2_by_rem_mask11[key] = []
        color2_by_rem_mask11[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask11 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask11:
            color3_by_rem_mask11[key] = []
        color3_by_rem_mask11[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask11 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask11:
            color1_by_rem_mask11[key] = []
        color1_by_rem_mask11[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask12 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask12:
            color2_by_rem_mask12[key] = []
        color2_by_rem_mask12[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask12 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask12:
            color3_by_rem_mask12[key] = []
        color3_by_rem_mask12[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask12 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask12:
            color1_by_rem_mask12[key] = []
        color1_by_rem_mask12[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask13 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask13:
            color2_by_rem_mask13[key] = []
        color2_by_rem_mask13[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask13 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask13:
            color3_by_rem_mask13[key] = []
        color3_by_rem_mask13[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask13 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask13:
            color1_by_rem_mask13[key] = []
        color1_by_rem_mask13[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask14 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask14:
            color2_by_rem_mask14[key] = []
        color2_by_rem_mask14[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask14 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask14:
            color3_by_rem_mask14[key] = []
        color3_by_rem_mask14[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask14 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask14:
            color1_by_rem_mask14[key] = []
        color1_by_rem_mask14[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask15 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask15:
            color2_by_rem_mask15[key] = []
        color2_by_rem_mask15[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask15 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask15:
            color3_by_rem_mask15[key] = []
        color3_by_rem_mask15[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask15 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask15:
            color1_by_rem_mask15[key] = []
        color1_by_rem_mask15[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask16 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask16:
            color2_by_rem_mask16[key] = []
        color2_by_rem_mask16[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask16 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask16:
            color3_by_rem_mask16[key] = []
        color3_by_rem_mask16[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask16 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask16:
            color1_by_rem_mask16[key] = []
        color1_by_rem_mask16[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask17 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask17:
            color2_by_rem_mask17[key] = []
        color2_by_rem_mask17[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask17 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask17:
            color3_by_rem_mask17[key] = []
        color3_by_rem_mask17[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask17 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask17:
            color1_by_rem_mask17[key] = []
        color1_by_rem_mask17[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask18 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask18:
            color2_by_rem_mask18[key] = []
        color2_by_rem_mask18[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask18 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask18:
            color3_by_rem_mask18[key] = []
        color3_by_rem_mask18[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask18 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask18:
            color1_by_rem_mask18[key] = []
        color1_by_rem_mask18[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask19 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask19:
            color2_by_rem_mask19[key] = []
        color2_by_rem_mask19[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask19 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask19:
            color3_by_rem_mask19[key] = []
        color3_by_rem_mask19[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask19 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask19:
            color1_by_rem_mask19[key] = []
        color1_by_rem_mask19[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask20 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask20:
            color2_by_rem_mask20[key] = []
        color2_by_rem_mask20[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask20 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask20:
            color3_by_rem_mask20[key] = []
        color3_by_rem_mask20[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask20 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask20:
            color1_by_rem_mask20[key] = []
        color1_by_rem_mask20[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask21 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask21:
            color2_by_rem_mask21[key] = []
        color2_by_rem_mask21[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask21 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask21:
            color3_by_rem_mask21[key] = []
        color3_by_rem_mask21[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask21 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask21:
            color1_by_rem_mask21[key] = []
        color1_by_rem_mask21[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask22 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask22:
            color2_by_rem_mask22[key] = []
        color2_by_rem_mask22[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask22 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask22:
            color3_by_rem_mask22[key] = []
        color3_by_rem_mask22[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask22 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask22:
            color1_by_rem_mask22[key] = []
        color1_by_rem_mask22[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask23 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask23:
            color2_by_rem_mask23[key] = []
        color2_by_rem_mask23[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask23 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask23:
            color3_by_rem_mask23[key] = []
        color3_by_rem_mask23[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask23 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask23:
            color1_by_rem_mask23[key] = []
        color1_by_rem_mask23[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask24 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask24:
            color2_by_rem_mask24[key] = []
        color2_by_rem_mask24[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask24 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask24:
            color3_by_rem_mask24[key] = []
        color3_by_rem_mask24[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask24 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask24:
            color1_by_rem_mask24[key] = []
        color1_by_rem_mask24[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask25 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask25:
            color2_by_rem_mask25[key] = []
        color2_by_rem_mask25[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask25 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask25:
            color3_by_rem_mask25[key] = []
        color3_by_rem_mask25[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask25 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask25:
            color1_by_rem_mask25[key] = []
        color1_by_rem_mask25[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask26 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask26:
            color2_by_rem_mask26[key] = []
        color2_by_rem_mask26[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask26 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask26:
            color3_by_rem_mask26[key] = []
        color3_by_rem_mask26[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask26 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask26:
            color1_by_rem_mask26[key] = []
        color1_by_rem_mask26[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask27 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask27:
            color2_by_rem_mask27[key] = []
        color2_by_rem_mask27[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask27 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask27:
            color3_by_rem_mask27[key] = []
        color3_by_rem_mask27[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask27 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask27:
            color1_by_rem_mask27[key] = []
        color1_by_rem_mask27[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask28 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask28:
            color2_by_rem_mask28[key] = []
        color2_by_rem_mask28[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask28 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask28:
            color3_by_rem_mask28[key] = []
        color3_by_rem_mask28[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask28 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask28:
            color1_by_rem_mask28[key] = []
        color1_by_rem_mask28[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask29 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask29:
            color2_by_rem_mask29[key] = []
        color2_by_rem_mask29[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask29 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask29:
            color3_by_rem_mask29[key] = []
        color3_by_rem_mask29[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask29 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask29:
            color1_by_rem_mask29[key] = []
        color1_by_rem_mask29[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask30 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask30:
            color2_by_rem_mask30[key] = []
        color2_by_rem_mask30[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask30 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask30:
            color3_by_rem_mask30[key] = []
        color3_by_rem_mask30[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask30 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask30:
            color1_by_rem_mask30[key] = []
        color1_by_rem_mask30[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask31 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask31:
            color2_by_rem_mask31[key] = []
        color2_by_rem_mask31[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask31 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask31:
            color3_by_rem_mask31[key] = []
        color3_by_rem_mask31[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask31 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask31:
            color1_by_rem_mask31[key] = []
        color1_by_rem_mask31[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask32 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask32:
            color2_by_rem_mask32[key] = []
        color2_by_rem_mask32[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask32 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask32:
            color3_by_rem_mask32[key] = []
        color3_by_rem_mask32[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask32 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask32:
            color1_by_rem_mask32[key] = []
        color1_by_rem_mask32[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask33 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask33:
            color2_by_rem_mask33[key] = []
        color2_by_rem_mask33[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask33 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask33:
            color3_by_rem_mask33[key] = []
        color3_by_rem_mask33[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask33 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask33:
            color1_by_rem_mask33[key] = []
        color1_by_rem_mask33[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask34 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask34:
            color2_by_rem_mask34[key] = []
        color2_by_rem_mask34[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask34 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask34:
            color3_by_rem_mask34[key] = []
        color3_by_rem_mask34[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask34 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask34:
            color1_by_rem_mask34[key] = []
        color1_by_rem_mask34[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask35 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask35:
            color2_by_rem_mask35[key] = []
        color2_by_rem_mask35[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask35 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask35:
            color3_by_rem_mask35[key] = []
        color3_by_rem_mask35[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask35 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask35:
            color1_by_rem_mask35[key] = []
        color1_by_rem_mask35[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask36 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask36:
            color2_by_rem_mask36[key] = []
        color2_by_rem_mask36[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask36 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask36:
            color3_by_rem_mask36[key] = []
        color3_by_rem_mask36[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask36 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask36:
            color1_by_rem_mask36[key] = []
        color1_by_rem_mask36[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask37 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask37:
            color2_by_rem_mask37[key] = []
        color2_by_rem_mask37[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask37 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask37:
            color3_by_rem_mask37[key] = []
        color3_by_rem_mask37[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask37 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask37:
            color1_by_rem_mask37[key] = []
        color1_by_rem_mask37[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask38 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask38:
            color2_by_rem_mask38[key] = []
        color2_by_rem_mask38[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask38 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask38:
            color3_by_rem_mask38[key] = []
        color3_by_rem_mask38[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask38 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask38:
            color1_by_rem_mask38[key] = []
        color1_by_rem_mask38[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask39 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask39:
            color2_by_rem_mask39[key] = []
        color2_by_rem_mask39[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask39 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask39:
            color3_by_rem_mask39[key] = []
        color3_by_rem_mask39[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask39 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask39:
            color1_by_rem_mask39[key] = []
        color1_by_rem_mask39[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask40 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask40:
            color2_by_rem_mask40[key] = []
        color2_by_rem_mask40[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask40 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask40:
            color3_by_rem_mask40[key] = []
        color3_by_rem_mask40[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask40 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask40:
            color1_by_rem_mask40[key] = []
        color1_by_rem_mask40[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask41 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask41:
            color2_by_rem_mask41[key] = []
        color2_by_rem_mask41[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask41 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask41:
            color3_by_rem_mask41[key] = []
        color3_by_rem_mask41[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask41 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask41:
            color1_by_rem_mask41[key] = []
        color1_by_rem_mask41[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask42 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask42:
            color2_by_rem_mask42[key] = []
        color2_by_rem_mask42[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask42 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask42:
            color3_by_rem_mask42[key] = []
        color3_by_rem_mask42[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask42 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask42:
            color1_by_rem_mask42[key] = []
        color1_by_rem_mask42[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask43 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask43:
            color2_by_rem_mask43[key] = []
        color2_by_rem_mask43[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask43 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask43:
            color3_by_rem_mask43[key] = []
        color3_by_rem_mask43[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask43 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask43:
            color1_by_rem_mask43[key] = []
        color1_by_rem_mask43[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask44 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask44:
            color2_by_rem_mask44[key] = []
        color2_by_rem_mask44[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask44 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask44:
            color3_by_rem_mask44[key] = []
        color3_by_rem_mask44[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask44 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask44:
            color1_by_rem_mask44[key] = []
        color1_by_rem_mask44[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask45 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask45:
            color2_by_rem_mask45[key] = []
        color2_by_rem_mask45[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask45 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask45:
            color3_by_rem_mask45[key] = []
        color3_by_rem_mask45[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask45 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask45:
            color1_by_rem_mask45[key] = []
        color1_by_rem_mask45[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask46 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask46:
            color2_by_rem_mask46[key] = []
        color2_by_rem_mask46[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask46 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask46:
            color3_by_rem_mask46[key] = []
        color3_by_rem_mask46[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask46 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask46:
            color1_by_rem_mask46[key] = []
        color1_by_rem_mask46[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask47 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask47:
            color2_by_rem_mask47[key] = []
        color2_by_rem_mask47[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask47 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask47:
            color3_by_rem_mask47[key] = []
        color3_by_rem_mask47[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask47 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask47:
            color1_by_rem_mask47[key] = []
        color1_by_rem_mask47[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask48 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask48:
            color2_by_rem_mask48[key] = []
        color2_by_rem_mask48[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask48 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask48:
            color3_by_rem_mask48[key] = []
        color3_by_rem_mask48[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask48 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask48:
            color1_by_rem_mask48[key] = []
        color1_by_rem_mask48[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask49 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask49:
            color2_by_rem_mask49[key] = []
        color2_by_rem_mask49[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask49 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask49:
            color3_by_rem_mask49[key] = []
        color3_by_rem_mask49[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask49 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask49:
            color1_by_rem_mask49[key] = []
        color1_by_rem_mask49[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask50 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask50:
            color2_by_rem_mask50[key] = []
        color2_by_rem_mask50[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask50 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask50:
            color3_by_rem_mask50[key] = []
        color3_by_rem_mask50[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask50 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask50:
            color1_by_rem_mask50[key] = []
        color1_by_rem_mask50[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask51 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask51:
            color2_by_rem_mask51[key] = []
        color2_by_rem_mask51[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask51 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask51:
            color3_by_rem_mask51[key] = []
        color3_by_rem_mask51[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask51 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask51:
            color1_by_rem_mask51[key] = []
        color1_by_rem_mask51[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask52 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask52:
            color2_by_rem_mask52[key] = []
        color2_by_rem_mask52[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask52 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask52:
            color3_by_rem_mask52[key] = []
        color3_by_rem_mask52[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask52 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask52:
            color1_by_rem_mask52[key] = []
        color1_by_rem_mask52[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask53 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask53:
            color2_by_rem_mask53[key] = []
        color2_by_rem_mask53[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask53 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask53:
            color3_by_rem_mask53[key] = []
        color3_by_rem_mask53[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask53 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask53:
            color1_by_rem_mask53[key] = []
        color1_by_rem_mask53[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask54 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask54:
            color2_by_rem_mask54[key] = []
        color2_by_rem_mask54[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask54 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask54:
            color3_by_rem_mask54[key] = []
        color3_by_rem_mask54[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask54 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask54:
            color1_by_rem_mask54[key] = []
        color1_by_rem_mask54[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask55 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask55:
            color2_by_rem_mask55[key] = []
        color2_by_rem_mask55[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask55 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask55:
            color3_by_rem_mask55[key] = []
        color3_by_rem_mask55[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask55 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask55:
            color1_by_rem_mask55[key] = []
        color1_by_rem_mask55[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask56 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask56:
            color2_by_rem_mask56[key] = []
        color2_by_rem_mask56[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask56 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask56:
            color3_by_rem_mask56[key] = []
        color3_by_rem_mask56[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask56 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask56:
            color1_by_rem_mask56[key] = []
        color1_by_rem_mask56[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask57 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask57:
            color2_by_rem_mask57[key] = []
        color2_by_rem_mask57[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask57 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask57:
            color3_by_rem_mask57[key] = []
        color3_by_rem_mask57[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask57 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask57:
            color1_by_rem_mask57[key] = []
        color1_by_rem_mask57[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask58 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask58:
            color2_by_rem_mask58[key] = []
        color2_by_rem_mask58[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask58 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask58:
            color3_by_rem_mask58[key] = []
        color3_by_rem_mask58[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask58 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask58:
            color1_by_rem_mask58[key] = []
        color1_by_rem_mask58[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask59 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask59:
            color2_by_rem_mask59[key] = []
        color2_by_rem_mask59[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask59 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask59:
            color3_by_rem_mask59[key] = []
        color3_by_rem_mask59[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask59 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask59:
            color1_by_rem_mask59[key] = []
        color1_by_rem_mask59[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask60 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask60:
            color2_by_rem_mask60[key] = []
        color2_by_rem_mask60[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask60 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask60:
            color3_by_rem_mask60[key] = []
        color3_by_rem_mask60[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask60 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask60:
            color1_by_rem_mask60[key] = []
        color1_by_rem_mask60[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask61 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask61:
            color2_by_rem_mask61[key] = []
        color2_by_rem_mask61[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask61 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask61:
            color3_by_rem_mask61[key] = []
        color3_by_rem_mask61[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask61 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask61:
            color1_by_rem_mask61[key] = []
        color1_by_rem_mask61[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask62 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask62:
            color2_by_rem_mask62[key] = []
        color2_by_rem_mask62[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask62 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask62:
            color3_by_rem_mask62[key] = []
        color3_by_rem_mask62[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask62 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask62:
            color1_by_rem_mask62[key] = []
        color1_by_rem_mask62[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask63 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask63:
            color2_by_rem_mask63[key] = []
        color2_by_rem_mask63[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask63 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask63:
            color3_by_rem_mask63[key] = []
        color3_by_rem_mask63[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask63 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask63:
            color1_by_rem_mask63[key] = []
        color1_by_rem_mask63[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask64 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask64:
            color2_by_rem_mask64[key] = []
        color2_by_rem_mask64[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask64 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask64:
            color3_by_rem_mask64[key] = []
        color3_by_rem_mask64[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask64 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask64:
            color1_by_rem_mask64[key] = []
        color1_by_rem_mask64[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask65 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask65:
            color2_by_rem_mask65[key] = []
        color2_by_rem_mask65[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask65 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask65:
            color3_by_rem_mask65[key] = []
        color3_by_rem_mask65[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask65 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask65:
            color1_by_rem_mask65[key] = []
        color1_by_rem_mask65[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask66 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask66:
            color2_by_rem_mask66[key] = []
        color2_by_rem_mask66[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask66 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask66:
            color3_by_rem_mask66[key] = []
        color3_by_rem_mask66[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask66 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask66:
            color1_by_rem_mask66[key] = []
        color1_by_rem_mask66[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask67 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask67:
            color2_by_rem_mask67[key] = []
        color2_by_rem_mask67[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask67 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask67:
            color3_by_rem_mask67[key] = []
        color3_by_rem_mask67[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask67 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask67:
            color1_by_rem_mask67[key] = []
        color1_by_rem_mask67[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask68 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask68:
            color2_by_rem_mask68[key] = []
        color2_by_rem_mask68[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask68 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask68:
            color3_by_rem_mask68[key] = []
        color3_by_rem_mask68[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask68 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask68:
            color1_by_rem_mask68[key] = []
        color1_by_rem_mask68[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask69 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask69:
            color2_by_rem_mask69[key] = []
        color2_by_rem_mask69[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask69 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask69:
            color3_by_rem_mask69[key] = []
        color3_by_rem_mask69[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask69 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask69:
            color1_by_rem_mask69[key] = []
        color1_by_rem_mask69[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask70 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask70:
            color2_by_rem_mask70[key] = []
        color2_by_rem_mask70[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask70 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask70:
            color3_by_rem_mask70[key] = []
        color3_by_rem_mask70[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask70 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask70:
            color1_by_rem_mask70[key] = []
        color1_by_rem_mask70[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask71 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask71:
            color2_by_rem_mask71[key] = []
        color2_by_rem_mask71[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask71 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask71:
            color3_by_rem_mask71[key] = []
        color3_by_rem_mask71[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask71 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask71:
            color1_by_rem_mask71[key] = []
        color1_by_rem_mask71[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask72 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask72:
            color2_by_rem_mask72[key] = []
        color2_by_rem_mask72[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask72 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask72:
            color3_by_rem_mask72[key] = []
        color3_by_rem_mask72[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask72 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask72:
            color1_by_rem_mask72[key] = []
        color1_by_rem_mask72[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask73 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask73:
            color2_by_rem_mask73[key] = []
        color2_by_rem_mask73[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask73 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask73:
            color3_by_rem_mask73[key] = []
        color3_by_rem_mask73[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask73 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask73:
            color1_by_rem_mask73[key] = []
        color1_by_rem_mask73[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask74 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask74:
            color2_by_rem_mask74[key] = []
        color2_by_rem_mask74[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask74 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask74:
            color3_by_rem_mask74[key] = []
        color3_by_rem_mask74[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask74 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask74:
            color1_by_rem_mask74[key] = []
        color1_by_rem_mask74[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask75 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask75:
            color2_by_rem_mask75[key] = []
        color2_by_rem_mask75[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask75 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask75:
            color3_by_rem_mask75[key] = []
        color3_by_rem_mask75[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask75 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask75:
            color1_by_rem_mask75[key] = []
        color1_by_rem_mask75[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask76 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask76:
            color2_by_rem_mask76[key] = []
        color2_by_rem_mask76[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask76 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask76:
            color3_by_rem_mask76[key] = []
        color3_by_rem_mask76[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask76 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask76:
            color1_by_rem_mask76[key] = []
        color1_by_rem_mask76[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask77 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask77:
            color2_by_rem_mask77[key] = []
        color2_by_rem_mask77[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask77 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask77:
            color3_by_rem_mask77[key] = []
        color3_by_rem_mask77[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask77 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask77:
            color1_by_rem_mask77[key] = []
        color1_by_rem_mask77[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask78 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask78:
            color2_by_rem_mask78[key] = []
        color2_by_rem_mask78[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask78 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask78:
            color3_by_rem_mask78[key] = []
        color3_by_rem_mask78[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask78 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask78:
            color1_by_rem_mask78[key] = []
        color1_by_rem_mask78[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask79 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask79:
            color2_by_rem_mask79[key] = []
        color2_by_rem_mask79[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask79 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask79:
            color3_by_rem_mask79[key] = []
        color3_by_rem_mask79[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask79 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask79:
            color1_by_rem_mask79[key] = []
        color1_by_rem_mask79[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask80 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask80:
            color2_by_rem_mask80[key] = []
        color2_by_rem_mask80[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask80 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask80:
            color3_by_rem_mask80[key] = []
        color3_by_rem_mask80[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask80 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask80:
            color1_by_rem_mask80[key] = []
        color1_by_rem_mask80[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask81 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask81:
            color2_by_rem_mask81[key] = []
        color2_by_rem_mask81[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask81 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask81:
            color3_by_rem_mask81[key] = []
        color3_by_rem_mask81[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask81 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask81:
            color1_by_rem_mask81[key] = []
        color1_by_rem_mask81[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask82 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask82:
            color2_by_rem_mask82[key] = []
        color2_by_rem_mask82[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask82 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask82:
            color3_by_rem_mask82[key] = []
        color3_by_rem_mask82[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask82 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask82:
            color1_by_rem_mask82[key] = []
        color1_by_rem_mask82[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask83 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask83:
            color2_by_rem_mask83[key] = []
        color2_by_rem_mask83[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask83 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask83:
            color3_by_rem_mask83[key] = []
        color3_by_rem_mask83[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask83 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask83:
            color1_by_rem_mask83[key] = []
        color1_by_rem_mask83[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask84 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask84:
            color2_by_rem_mask84[key] = []
        color2_by_rem_mask84[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask84 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask84:
            color3_by_rem_mask84[key] = []
        color3_by_rem_mask84[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask84 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask84:
            color1_by_rem_mask84[key] = []
        color1_by_rem_mask84[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask85 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask85:
            color2_by_rem_mask85[key] = []
        color2_by_rem_mask85[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask85 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask85:
            color3_by_rem_mask85[key] = []
        color3_by_rem_mask85[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask85 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask85:
            color1_by_rem_mask85[key] = []
        color1_by_rem_mask85[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask86 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask86:
            color2_by_rem_mask86[key] = []
        color2_by_rem_mask86[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask86 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask86:
            color3_by_rem_mask86[key] = []
        color3_by_rem_mask86[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask86 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask86:
            color1_by_rem_mask86[key] = []
        color1_by_rem_mask86[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask87 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask87:
            color2_by_rem_mask87[key] = []
        color2_by_rem_mask87[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask87 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask87:
            color3_by_rem_mask87[key] = []
        color3_by_rem_mask87[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask87 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask87:
            color1_by_rem_mask87[key] = []
        color1_by_rem_mask87[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask88 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask88:
            color2_by_rem_mask88[key] = []
        color2_by_rem_mask88[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask88 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask88:
            color3_by_rem_mask88[key] = []
        color3_by_rem_mask88[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask88 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask88:
            color1_by_rem_mask88[key] = []
        color1_by_rem_mask88[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask89 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask89:
            color2_by_rem_mask89[key] = []
        color2_by_rem_mask89[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask89 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask89:
            color3_by_rem_mask89[key] = []
        color3_by_rem_mask89[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask89 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask89:
            color1_by_rem_mask89[key] = []
        color1_by_rem_mask89[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask90 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask90:
            color2_by_rem_mask90[key] = []
        color2_by_rem_mask90[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask90 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask90:
            color3_by_rem_mask90[key] = []
        color3_by_rem_mask90[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask90 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask90:
            color1_by_rem_mask90[key] = []
        color1_by_rem_mask90[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask91 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask91:
            color2_by_rem_mask91[key] = []
        color2_by_rem_mask91[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask91 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask91:
            color3_by_rem_mask91[key] = []
        color3_by_rem_mask91[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask91 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask91:
            color1_by_rem_mask91[key] = []
        color1_by_rem_mask91[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask92 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask92:
            color2_by_rem_mask92[key] = []
        color2_by_rem_mask92[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask92 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask92:
            color3_by_rem_mask92[key] = []
        color3_by_rem_mask92[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask92 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask92:
            color1_by_rem_mask92[key] = []
        color1_by_rem_mask92[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask93 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask93:
            color2_by_rem_mask93[key] = []
        color2_by_rem_mask93[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask93 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask93:
            color3_by_rem_mask93[key] = []
        color3_by_rem_mask93[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask93 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask93:
            color1_by_rem_mask93[key] = []
        color1_by_rem_mask93[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask94 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask94:
            color2_by_rem_mask94[key] = []
        color2_by_rem_mask94[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask94 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask94:
            color3_by_rem_mask94[key] = []
        color3_by_rem_mask94[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask94 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask94:
            color1_by_rem_mask94[key] = []
        color1_by_rem_mask94[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask95 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask95:
            color2_by_rem_mask95[key] = []
        color2_by_rem_mask95[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask95 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask95:
            color3_by_rem_mask95[key] = []
        color3_by_rem_mask95[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask95 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask95:
            color1_by_rem_mask95[key] = []
        color1_by_rem_mask95[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask96 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask96:
            color2_by_rem_mask96[key] = []
        color2_by_rem_mask96[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask96 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask96:
            color3_by_rem_mask96[key] = []
        color3_by_rem_mask96[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask96 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask96:
            color1_by_rem_mask96[key] = []
        color1_by_rem_mask96[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask97 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask97:
            color2_by_rem_mask97[key] = []
        color2_by_rem_mask97[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask97 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask97:
            color3_by_rem_mask97[key] = []
        color3_by_rem_mask97[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask97 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask97:
            color1_by_rem_mask97[key] = []
        color1_by_rem_mask97[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask98 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask98:
            color2_by_rem_mask98[key] = []
        color2_by_rem_mask98[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask98 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask98:
            color3_by_rem_mask98[key] = []
        color3_by_rem_mask98[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask98 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask98:
            color1_by_rem_mask98[key] = []
        color1_by_rem_mask98[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask99 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask99:
            color2_by_rem_mask99[key] = []
        color2_by_rem_mask99[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask99 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask99:
            color3_by_rem_mask99[key] = []
        color3_by_rem_mask99[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask99 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask99:
            color1_by_rem_mask99[key] = []
        color1_by_rem_mask99[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask100 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask100:
            color2_by_rem_mask100[key] = []
        color2_by_rem_mask100[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask100 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask100:
            color3_by_rem_mask100[key] = []
        color3_by_rem_mask100[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask100 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask100:
            color1_by_rem_mask100[key] = []
        color1_by_rem_mask100[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask101 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask101:
            color2_by_rem_mask101[key] = []
        color2_by_rem_mask101[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask101 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask101:
            color3_by_rem_mask101[key] = []
        color3_by_rem_mask101[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask101 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask101:
            color1_by_rem_mask101[key] = []
        color1_by_rem_mask101[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask102 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask102:
            color2_by_rem_mask102[key] = []
        color2_by_rem_mask102[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask102 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask102:
            color3_by_rem_mask102[key] = []
        color3_by_rem_mask102[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask102 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask102:
            color1_by_rem_mask102[key] = []
        color1_by_rem_mask102[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask103 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask103:
            color2_by_rem_mask103[key] = []
        color2_by_rem_mask103[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask103 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask103:
            color3_by_rem_mask103[key] = []
        color3_by_rem_mask103[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask103 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask103:
            color1_by_rem_mask103[key] = []
        color1_by_rem_mask103[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask104 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask104:
            color2_by_rem_mask104[key] = []
        color2_by_rem_mask104[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask104 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask104:
            color3_by_rem_mask104[key] = []
        color3_by_rem_mask104[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask104 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask104:
            color1_by_rem_mask104[key] = []
        color1_by_rem_mask104[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask105 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask105:
            color2_by_rem_mask105[key] = []
        color2_by_rem_mask105[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask105 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask105:
            color3_by_rem_mask105[key] = []
        color3_by_rem_mask105[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask105 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask105:
            color1_by_rem_mask105[key] = []
        color1_by_rem_mask105[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask106 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask106:
            color2_by_rem_mask106[key] = []
        color2_by_rem_mask106[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask106 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask106:
            color3_by_rem_mask106[key] = []
        color3_by_rem_mask106[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask106 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask106:
            color1_by_rem_mask106[key] = []
        color1_by_rem_mask106[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask107 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask107:
            color2_by_rem_mask107[key] = []
        color2_by_rem_mask107[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask107 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask107:
            color3_by_rem_mask107[key] = []
        color3_by_rem_mask107[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask107 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask107:
            color1_by_rem_mask107[key] = []
        color1_by_rem_mask107[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask108 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask108:
            color2_by_rem_mask108[key] = []
        color2_by_rem_mask108[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask108 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask108:
            color3_by_rem_mask108[key] = []
        color3_by_rem_mask108[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask108 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask108:
            color1_by_rem_mask108[key] = []
        color1_by_rem_mask108[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask109 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask109:
            color2_by_rem_mask109[key] = []
        color2_by_rem_mask109[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask109 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask109:
            color3_by_rem_mask109[key] = []
        color3_by_rem_mask109[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask109 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask109:
            color1_by_rem_mask109[key] = []
        color1_by_rem_mask109[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask110 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask110:
            color2_by_rem_mask110[key] = []
        color2_by_rem_mask110[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask110 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask110:
            color3_by_rem_mask110[key] = []
        color3_by_rem_mask110[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask110 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask110:
            color1_by_rem_mask110[key] = []
        color1_by_rem_mask110[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask111 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask111:
            color2_by_rem_mask111[key] = []
        color2_by_rem_mask111[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask111 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask111:
            color3_by_rem_mask111[key] = []
        color3_by_rem_mask111[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask111 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask111:
            color1_by_rem_mask111[key] = []
        color1_by_rem_mask111[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask112 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask112:
            color2_by_rem_mask112[key] = []
        color2_by_rem_mask112[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask112 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask112:
            color3_by_rem_mask112[key] = []
        color3_by_rem_mask112[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask112 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask112:
            color1_by_rem_mask112[key] = []
        color1_by_rem_mask112[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask113 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask113:
            color2_by_rem_mask113[key] = []
        color2_by_rem_mask113[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask113 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask113:
            color3_by_rem_mask113[key] = []
        color3_by_rem_mask113[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask113 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask113:
            color1_by_rem_mask113[key] = []
        color1_by_rem_mask113[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask114 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask114:
            color2_by_rem_mask114[key] = []
        color2_by_rem_mask114[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask114 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask114:
            color3_by_rem_mask114[key] = []
        color3_by_rem_mask114[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask114 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask114:
            color1_by_rem_mask114[key] = []
        color1_by_rem_mask114[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask115 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask115:
            color2_by_rem_mask115[key] = []
        color2_by_rem_mask115[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask115 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask115:
            color3_by_rem_mask115[key] = []
        color3_by_rem_mask115[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask115 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask115:
            color1_by_rem_mask115[key] = []
        color1_by_rem_mask115[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask116 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask116:
            color2_by_rem_mask116[key] = []
        color2_by_rem_mask116[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask116 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask116:
            color3_by_rem_mask116[key] = []
        color3_by_rem_mask116[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask116 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask116:
            color1_by_rem_mask116[key] = []
        color1_by_rem_mask116[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask117 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask117:
            color2_by_rem_mask117[key] = []
        color2_by_rem_mask117[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask117 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask117:
            color3_by_rem_mask117[key] = []
        color3_by_rem_mask117[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask117 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask117:
            color1_by_rem_mask117[key] = []
        color1_by_rem_mask117[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask118 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask118:
            color2_by_rem_mask118[key] = []
        color2_by_rem_mask118[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask118 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask118:
            color3_by_rem_mask118[key] = []
        color3_by_rem_mask118[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask118 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask118:
            color1_by_rem_mask118[key] = []
        color1_by_rem_mask118[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask119 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask119:
            color2_by_rem_mask119[key] = []
        color2_by_rem_mask119[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask119 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask119:
            color3_by_rem_mask119[key] = []
        color3_by_rem_mask119[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask119 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask119:
            color1_by_rem_mask119[key] = []
        color1_by_rem_mask119[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask120 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask120:
            color2_by_rem_mask120[key] = []
        color2_by_rem_mask120[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask120 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask120:
            color3_by_rem_mask120[key] = []
        color3_by_rem_mask120[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask120 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask120:
            color1_by_rem_mask120[key] = []
        color1_by_rem_mask120[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask121 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask121:
            color2_by_rem_mask121[key] = []
        color2_by_rem_mask121[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask121 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask121:
            color3_by_rem_mask121[key] = []
        color3_by_rem_mask121[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask121 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask121:
            color1_by_rem_mask121[key] = []
        color1_by_rem_mask121[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask122 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask122:
            color2_by_rem_mask122[key] = []
        color2_by_rem_mask122[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask122 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask122:
            color3_by_rem_mask122[key] = []
        color3_by_rem_mask122[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask122 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask122:
            color1_by_rem_mask122[key] = []
        color1_by_rem_mask122[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask123 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask123:
            color2_by_rem_mask123[key] = []
        color2_by_rem_mask123[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask123 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask123:
            color3_by_rem_mask123[key] = []
        color3_by_rem_mask123[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask123 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask123:
            color1_by_rem_mask123[key] = []
        color1_by_rem_mask123[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask124 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask124:
            color2_by_rem_mask124[key] = []
        color2_by_rem_mask124[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask124 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask124:
            color3_by_rem_mask124[key] = []
        color3_by_rem_mask124[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask124 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask124:
            color1_by_rem_mask124[key] = []
        color1_by_rem_mask124[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask125 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask125:
            color2_by_rem_mask125[key] = []
        color2_by_rem_mask125[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask125 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask125:
            color3_by_rem_mask125[key] = []
        color3_by_rem_mask125[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask125 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask125:
            color1_by_rem_mask125[key] = []
        color1_by_rem_mask125[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask126 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask126:
            color2_by_rem_mask126[key] = []
        color2_by_rem_mask126[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask126 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask126:
            color3_by_rem_mask126[key] = []
        color3_by_rem_mask126[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask126 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask126:
            color1_by_rem_mask126[key] = []
        color1_by_rem_mask126[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask127 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask127:
            color2_by_rem_mask127[key] = []
        color2_by_rem_mask127[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask127 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask127:
            color3_by_rem_mask127[key] = []
        color3_by_rem_mask127[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask127 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask127:
            color1_by_rem_mask127[key] = []
        color1_by_rem_mask127[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask128 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask128:
            color2_by_rem_mask128[key] = []
        color2_by_rem_mask128[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask128 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask128:
            color3_by_rem_mask128[key] = []
        color3_by_rem_mask128[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask128 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask128:
            color1_by_rem_mask128[key] = []
        color1_by_rem_mask128[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask129 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask129:
            color2_by_rem_mask129[key] = []
        color2_by_rem_mask129[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask129 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask129:
            color3_by_rem_mask129[key] = []
        color3_by_rem_mask129[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask129 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask129:
            color1_by_rem_mask129[key] = []
        color1_by_rem_mask129[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask130 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask130:
            color2_by_rem_mask130[key] = []
        color2_by_rem_mask130[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask130 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask130:
            color3_by_rem_mask130[key] = []
        color3_by_rem_mask130[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask130 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask130:
            color1_by_rem_mask130[key] = []
        color1_by_rem_mask130[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask131 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask131:
            color2_by_rem_mask131[key] = []
        color2_by_rem_mask131[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask131 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask131:
            color3_by_rem_mask131[key] = []
        color3_by_rem_mask131[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask131 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask131:
            color1_by_rem_mask131[key] = []
        color1_by_rem_mask131[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask132 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color2_by_rem_mask132:
            color2_by_rem_mask132[key] = []
        color2_by_rem_mask132[key].append(mask)
    
    # Precompute color3 candidates by remaining and mask
    color3_by_rem_mask132 = {}
    for mask in color3_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color3_by_rem_mask132:
            color3_by_rem_mask132[key] = []
        color3_by_rem_mask132[key].append(mask)
    
    # Precompute color1 candidates by remaining and mask
    color1_by_rem_mask132 = {}
    for mask in color1_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not in color1_by_rem_mask132:
            color1_by_rem_mask132[key] = []
        color1_by_rem_mask132[key].append(mask)
    
    # Precompute color2 candidates by remaining and mask
    color2_by_rem_mask133 = {}
    for mask in color2_cand:
        rem = comp[mask]
        key = (rem, mask)
        if key not