import sys

# Reading number of guilds and treaties
n, m = map(int, input().split())

# Adjacency matrix for the guilds
adj = [[False] * n for _ in range(n)]

# Fill adjacency matrix with given treaties
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    adj[u][v] = True
    adj[v][u] = True

# Try all possible triples (a, b, c)
for a in range(n):
    for b in range(a + 1, n):
        if not adj[a][b]:
            continue
        for c in range(b + 1, n):
            if adj[a][c] and adj[b][c]:
                # Found a valid triplet (a+1, b+1, c+1)
                print(f"{a + 1} {b + 1} {c + 1}")
                sys.exit()