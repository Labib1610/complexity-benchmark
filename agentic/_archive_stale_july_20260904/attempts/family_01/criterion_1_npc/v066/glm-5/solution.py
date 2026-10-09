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
        u = int(data[idx]); v = int(data[idx+1])
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Precompute for each subset of vertices the set of vertices adjacent to any vertex in the subset.
    # adj_union[subset] = union of neighbors of vertices in subset, restricted to vertices not in subset.
    size = 1 << n
    adj_union = [0] * size
    for subset in range(size):
        temp = 0
        s = subset
        while s:
            low = s & (-s)
            v = low.bit_length() - 1
            temp |= adj[v + 1]
            s ^= low
        adj_union[subset] = temp & (~subset)

    # DP over subsets: dp[mask] = True if mask is 3-colorable.
    dp = [False] * size
    dp[0] = True
    for mask in range(1, size):
        s = mask
        while s:
            low = s & (-s)
            sub = low | (adj_union[low] & mask & (low - 1))
            if dp[mask ^ sub]:
                dp[mask] = True
                break
            s ^= low

    if not dp[size - 1]:
        print("NO")
        return

    # Greedy lexicographically smallest assignment.
    color = [0] * (n + 1)
    remaining = size - 1
    for i in range(1, n + 1):
        bit = 1 << (i - 1)
        for c in range(1, 4):
            # Build the set of vertices that must take color c: vertex i plus all uncolored vertices adjacent to i.
            forced = bit
            forced |= adj[i] & remaining
            # Check if removing 'forced' from 'remaining' leaves a 3-colorable set.
            if dp[remaining ^ forced]:
                color[i] = c
                remaining ^= forced
                break

    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()