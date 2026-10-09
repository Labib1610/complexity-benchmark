import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    INF = 10**18
    size = 1 << n
    dp = [INF] * size
    parent = [-1] * size
    last_added = [-1] * size
    
    dp[0] = 0
    
    for mask in range(size):
        if dp[mask] == INF:
            continue
        k = bin(mask).count("1")  # next position index (0-based)
        # try adding each vertex not in mask
        for v in range(n):
            if not (mask >> v) & 1:
                new_mask = mask | (1 << v)
                cost = 0
                # sum distances to already placed neighbors
                for u in adj[v]:
                    if (mask >> u) & 1:
                        # position of u is its order in mask
                        # we can compute by iterating bits
                        # but we can precompute positions? Let's compute on the fly.
                        # We'll compute position of u in mask by counting bits before it.
                        pos_u = 0
                        # count bits in mask up to u
                        for i in range(u):
                            if (mask >> i) & 1:
                                pos_u += 1
                        cost += k - pos_u
                if dp[mask] + cost < dp[new_mask]:
                    dp[new_mask] = dp[mask] + cost
                    parent[new_mask] = mask
                    last_added[new_mask] = v
    
    full_mask = size - 1
    if dp[full_mask] <= B:
        # reconstruct
        perm = [0] * n
        mask = full_mask
        while mask:
            v = last_added[mask]
            pos = bin(mask).count("1") - 1  # 0-based position
            perm[v] = pos + 1
            mask = parent[mask]
        print("YES")
        print(" ".join(map(str, perm)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()