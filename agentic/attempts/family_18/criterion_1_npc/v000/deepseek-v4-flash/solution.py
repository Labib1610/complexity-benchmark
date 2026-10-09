INF = 10**18
n, m, B = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    adj[u].append(v)
    adj[v].append(u)

# DP
dp = [INF] * (1<<n)
dp[0] = 0
parent = [-1] * (1<<n)  # store last added vertex and previous mask? maybe store prev_mask and added v
# We'll store prev_mask and last_added vertex separately.

for mask in range(1<<n):
    if dp[mask] == INF: continue
    k = bin(mask).count("1")  # number placed
    # Try to place each v not in mask
    for v in range(n):
        if mask & (1<<v): continue
        # Compute added cost
        added_cost = 0
        for u in adj[v]:
            if mask & (1<<u):
                # pos[u] = rank of u in mask (0-based)
                # rank of u = number of vertices in mask that are <= u? Actually rank among mask in order we placed them.
                # But we don't know the order from mask alone.