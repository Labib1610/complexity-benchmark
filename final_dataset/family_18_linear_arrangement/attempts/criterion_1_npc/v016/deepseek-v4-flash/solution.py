import sys
from array import array

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    # edge_count[i][j] for i<j
    edge = [[0]*n for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edge[u][v] = 1
        edge[v][u] = 1
    
    if n > 20:
        # Fallback: not expected for given constraints
        print("NO")
        return
    
    N = 1 << n
    # popcount for all masks
    pop = [0] * N
    for i in range(1, N):
        pop[i] = pop[i >> 1] + (i & 1)
    
    # sum_pos[mask][v] = sum of positions of neighbors of v in mask
    # deg_mask[mask][v] = number of neighbors of v in mask
    sum_pos = [array('i', [0]*n) for _ in range(N)]
    deg_mask = [array('i', [0]*n) for _ in range(N)]
    
    for mask in range(1, N):
        lsb = mask & -mask
        u = (lsb.bit_length() - 1)
        prev = mask ^ lsb
        pos_u = pop[prev]  # position where u was placed (0-indexed)
        for v in range(n):
            if (mask >> v) & 1:
                continue
            if edge[u][v]:
                deg_mask[mask][v] = deg_mask[prev][v] + 1
                sum_pos[mask][v] = sum_pos[prev][v] + pos_u
            else:
                deg_mask[mask][v] = deg_mask[prev][v]
                sum_pos[mask][v] = sum_pos[prev][v]
    
    INF = 10**18
    dp = [INF] * N
    parent_mask = [-1] * N
    parent_v = [-1] * N
    dp[0] = 0
    
    for mask in range(N):
        if dp[mask] == INF:
            continue
        pos = pop[mask]
        for v in range(n):
            if (mask >> v) & 1:
                continue
            new_mask = mask | (1 << v)
            cost_add = pos * deg_mask[mask][v] - sum_pos[mask][v]
            nd = dp[mask] + cost_add
            if nd < dp[new_mask]:
                dp[new_mask] = nd
                parent_mask[new_mask] = mask
                parent_v[new_mask] = v
    
    full = N - 1
    if dp[full] > B:
        print("NO")
        return
    
    # reconstruct
    perm = [0] * n
    mask = full
    while mask:
        pm = parent_mask[mask]
        v = parent_v[mask]
        pos = pop[pm]
        perm[v] = pos + 1  # 1-indexed
        mask = pm
    
    print("YES")
    print(' '.join(map(str, perm)))

if __name__ == "__main__":
    solve()