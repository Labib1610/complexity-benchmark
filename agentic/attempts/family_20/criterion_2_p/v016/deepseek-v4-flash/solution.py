import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

S, T, m = map(int, input().split())
edges = []
deg_src = [0] * (S + 1)
deg_dst = [0] * (T + 1)

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    deg_src[u] += 1
    deg_dst[v] += 1

D = max(max(deg_src), max(deg_dst), 0)

color = [0] * m
# color_src[u][c] = edge index or -1 if free
color_src = [[-1] * (D + 1) for _ in range(S + 1)]
color_dst = [[-1] * (D + 1) for _ in range(T + 1)]

for idx, (u, v) in enumerate(edges):
    # find smallest color not used by u or v
    c = 1
    while color_src[u][c] != -1 or color_dst[v][c] != -1:
        c += 1
    color[idx] = c
    color_src[u][c] = idx
    color_dst[v][c] = idx

# Now possibly fix collisions by flanking might not be needed if we use direct assignment,
# But since it's bipartite, greedy smallest free works if we do it in correct order?
# For bipartite graphs, greedy smallest free at each edge is NOT always valid.
# So we implement the standard algorithm:
# We will use a more reliable method: iteratively color by finding matchings.

# Let's redo with a proven decomposition approach:

# Build adjacency list for sources
adj = [[] for _ in range(S + 1)]
for i, (u, v) in enumerate(edges):
    adj[u].append((v, i))

res = [0] * m
# We'll color via matching decomposition:
for color_idx in range(1, D + 1):
    match_src = [-1] * (S + 1)
    match_dst = [-1] * (T + 1)
    # Try to augment matchings
    for u in range(1, S + 1):
        if match_src[u] != -1:
            continue
        # find augmenting path via DFS
        visited = [False] * (T + 1)
        def dfs(src):
            for v, ei in adj[src]:
                if visited[v]:
                    continue
                visited[v] = True
                if match_dst[v] == -1 or dfs(match_dst[v]):
                    match_src[src] = ei
                    match_dst[v] = src
                    return True
            return False
        dfs(u)
    for u in range(1, S + 1):
        if match_src[u] != -1:
            ei = match_src[u]
            res[ei] = color_idx
            # remove this edge from adj lists for future colors
    # remove matched edges
    matched_edges = set(match_src[1:]) - { -1 }
    for u in range(1, S + 1):
        adj[u] = [(v, ei) for (v, ei) in adj[u] if ei not in matched_edges]

print("YES")
print(" ".join(map(str, res)))