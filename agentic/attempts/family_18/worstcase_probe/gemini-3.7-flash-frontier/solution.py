import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    edges = []
    idx = 3
    adj_mask = [0] * n
    deg = [0] * n
    
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v:
            adj_mask[u] |= (1 << v)
            adj_mask[v] |= (1 << u)
            deg[u] += 1
            deg[v] += 1
            edges.append((u, v))

    if m == 0:
        print("YES")
        print(*(i + 1 for i in range(n)))
        return

    # If simple identity works
    def eval_perm(p):
        pos = [0] * n
        for i, v in enumerate(p):
            pos[v] = i
        return sum(abs(pos[u] - pos[v]) for u, v in edges)

    # Check trivial permutation
    perm_init = list(range(n))
    if eval_perm(perm_init) <= B:
        pos_out = [0] * n
        for i, v in enumerate(perm_init):
            pos_out[v] = i + 1
        print("YES")
        print(*pos_out)
        return

    # Solve using DP / Branch and Bound
    # For general n <= 22, bitmask DP is exact and optimal.
    # dp[mask] = min cost, parent[mask] = last added vertex
    
    num_states = 1 << n
    dp = [float('inf')] * num_states
    parent = [-1] * num_states
    cut = [0] * num_states
    
    dp[0] = 0
    cut[0] = 0
    
    # Precompute bit counts / cut values efficiently
    for mask in range(1, num_states):
        # find lowest set bit
        v = (mask & -mask).bit_length() - 1
        prev_mask = mask ^ (1 << v)
        cut[mask] = cut[prev_mask] + deg[v] - 2 * (prev_mask & adj_mask[v]).bit_count()
        
        # Now find min dp[mask ^ (1 << u)] + cut[mask]
        m_temp = mask
        min_prev = float('inf')
        best_u = -1
        while m_temp:
            lsb = m_temp & -m_temp
            u = lsb.bit_length() - 1
            m_temp ^= lsb
            val = dp[mask ^ (1 << u)]
            if val < min_prev:
                min_prev = val
                best_u = u
        
        total_val = min_prev + cut[mask]
        dp[mask] = total_val
        parent[mask] = best_u

    final_mask = num_states - 1
    if dp[final_mask] <= B:
        print("YES")
        # reconstruct permutation
        # order of vertices placed from left to right (position 1 to n)
        curr = final_mask
        placement = []
        while curr > 0:
            u = parent[curr]
            placement.append(u)
            curr ^= (1 << u)
        placement.reverse()
        
        pos_ans = [0] * n
        for i, node in enumerate(placement):
            pos_ans[node] = i + 1
        print(*pos_ans)
    else:
        print("NO")

if __name__ == '__main__':
    solve()