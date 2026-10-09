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
    dp[0] = 0
    
    # Precompute neighbor masks
    neigh_mask = [0] * n
    for i in range(n):
        mask = 0
        for j in adj[i]:
            mask |= (1 << j)
        neigh_mask[i] = mask
    
    for mask in range(size):
        if dp[mask] == INF:
            continue
        pos = bin(mask).count("1")
        # Try adding each unplaced vertex
        for v in range(n):
            if not (mask >> v) & 1:
                new_mask = mask | (1 << v)
                # cost added = sum over neighbors already in mask of (pos - pos_of_neighbor)
                # pos_of_neighbor = position in mask
                # We can compute by iterating neighbors
                added = 0
                for u in adj[v]:
                    if (mask >> u) & 1:
                        # position of u in mask = number of set bits before u
                        # We can compute by mask & ((1<<u)-1)
                        pos_u = bin(mask & ((1 << u) - 1)).count("1")
                        added += pos - pos_u
                if dp[new_mask] > dp[mask] + added:
                    dp[new_mask] = dp[mask] + added
                    parent[new_mask] = mask
    
    full = size - 1
    if dp[full] > B:
        print("NO")
        return
    
    # Reconstruct
    assignment = [0] * n
    mask = full
    pos = n - 1
    while mask:
        prev = parent[mask]
        # find which bit was added
        diff = mask ^ prev
        v = diff.bit_length() - 1
        assignment[v] = pos + 1
        pos -= 1
        mask = prev
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    solve()