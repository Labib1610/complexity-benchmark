import sys

def solve():
    input = sys.stdin.readline
    n, m, B = map(int, input().split())
    edges = []
    adj = [0]*n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        edges.append((u, v))
    
    # Precompute cost of adding each vertex to a mask
    # cost_add[mask][v] = sum of edges from v to mask
    # We'll compute on the fly in DP.
    
    INF = 10**18
    dp = [INF] * (1 << n)
    parent = [-1] * (1 << n)
    dp[0] = 0
    
    for mask in range(1 << n):
        if dp[mask] == INF:
            continue
        # Try adding each vertex not in mask
        for v in range(n):
            if not (mask >> v) & 1:
                # cost = sum over u in mask of (adj[v] has u) * (popcount(mask))
                # Actually distance = popcount(mask) because we place at position popcount(mask)+1
                # and each edge to already placed u contributes distance = popcount(mask)
                # So cost = popcount(mask) * (number of edges from v to mask)
                cnt = (adj[v] & mask).bit_count()
                new_mask = mask | (1 << v)
                new_cost = dp[mask] + cnt * mask.bit_count()
                if new_cost < dp[new_mask]:
                    dp[new_mask] = new_cost
                    parent[new_mask] = v
    
    full = (1 << n) - 1
    if dp[full] <= B:
        # reconstruct
        order = []
        mask = full
        while mask:
            v = parent[mask]
            order.append(v)
            mask ^= (1 << v)
        order.reverse()
        # order[0] is first placed, so assign bay 1 to order[0], etc.
        pos = [0]*n
        for i, v in enumerate(order):
            pos[v] = i+1
        print("YES")
        print(" ".join(map(str, pos)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()