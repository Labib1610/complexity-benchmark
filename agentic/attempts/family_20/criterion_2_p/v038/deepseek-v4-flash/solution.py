import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

N_in, N_out, M = map(int, input().split())
edges = []
adj_in = [[] for _ in range(N_in + 1)]
adj_out = [[] for _ in range(N_out + 1)]

for idx in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))
    adj_in[u].append((v, idx))
    adj_out[v].append((u, idx))

# Compute maximum degree
deg_in = [len(adj_in[i]) for i in range(N_in + 1)]
deg_out = [len(adj_out[i]) for i in range(N_out + 1)]
D = max(max(deg_in), max(deg_out))

color = [0] * M

# We'll color edges by repeatedly finding matchings
# Use a simple DFS-based matching for each color
for c in range(1, D + 1):
    match_out = [0] * (N_out + 1)  # which inbound is matched to this outbound
    # Try to match each inbound that still has uncolored edges
    for u in range(1, N_in + 1):
        # Find an uncolored edge from u
        for v, idx in adj_in[u]:
            if color[idx] == 0:
                # Try to assign color c to this edge
                # Check if v is free
                if match_out[v] == 0:
                    match_out[v] = u
                    color[idx] = c
                else:
                    # Try to reassign
                    # Simple approach: just assign if possible, else skip
                    # For correctness, we can use DFS augmenting path
                    # But for simplicity, we'll just assign if free
                    pass
    # Actually, the above greedy may fail; we need proper matching.
    # Let's implement a proper DFS matching for each color.

# Let's redo with proper matching per color
color = [0] * M
for c in range(1, D + 1):
    match_to = [0] * (N_out + 1)  # outbound -> inbound
    # DFS to find augmenting paths
    def dfs(u, seen):
        for v, idx in adj_in[u]:
            if color[idx] == 0 and not seen[v]:
                seen[v] = True
                if match_to[v] == 0 or dfs(match_to[v], seen):
                    match_to[v] = u
                    color[idx] = c
                    return True
        return False

    for u in range(1, N_in + 1):
        seen = [False] * (N_out + 1)
        dfs(u, seen)

# Output
print("YES")
print(" ".join(map(str, color)))