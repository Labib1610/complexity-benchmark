import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    targets = []
    for _ in range(t):
        targets.append(int(input_data[idx]) - 1); idx += 1
    
    INF = float('inf')
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for _ in range(m):
        u = int(input_data[idx]) - 1; idx += 1
        v = int(input_data[idx]) - 1; idx += 1
        w = int(input_data[idx]); idx += 1
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    for k in range(n):
        for i in range(n):
            if dist[i][k] < INF:
                for j in range(n):
                    if dist[k][j] < INF:
                        if dist[i][k] + dist[k][j] < dist[i][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
    
    if t <= 1:
        print(0)
        return
    
    T = t
    full = (1 << T) - 1
    
    # g[S] = min cost to connect all targets in S into one component
    g = [INF] * (1 << T)
    for S in range(1, 1 << T):
        bits = [i for i in range(T) if S & (1 << i)]
        if len(bits) == 1:
            g[S] = 0
        else:
            # Prim's algorithm on targets in S
            size = len(bits)
            in_mst = [False] * size
            min_edge = [INF] * size
            min_edge[0] = 0
            total = 0
            for _ in range(size):
                u = -1
                best = INF
                for j in range(size):
                    if not in_mst[j] and min_edge[j] < best:
                        best = min_edge[j]
                        u = j
                if u == -1:
                    total = INF
                    break
                in_mst[u] = True
                total += min_edge[u]
                for j in range(size):
                    if not in_mst[j]:
                        d = dist[targets[bits[u]]][targets[bits[j]]]
                        if d < min_edge[j]:
                            min_edge[j] = d
            g[S] = total
    
    # f[mask] = min cost to partition targets in mask into groups, each connected
    f = [INF] * (1 << T)
    f[0] = 0
    for mask in range(1, 1 << T):
        # Find lowest set bit
        low = mask & (-mask)
        low_idx = low.bit_length() - 1
        # Iterate over subsets S of mask containing low_idx
        sub = mask
        while sub > 0:
            if sub & low:
                rest = mask ^ sub
                if g[sub] < INF and f[rest] < INF:
                    val = g[sub] + f[rest]
                    if val < f[mask]:
                        f[mask] = val
            sub = (sub - 1) & mask
    
    print(f[full])

solve()