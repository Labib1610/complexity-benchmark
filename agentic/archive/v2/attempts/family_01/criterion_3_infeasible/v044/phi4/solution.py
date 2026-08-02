import sys

# Read number of units and direct conflict links
n, m = map(int, input().split())

# Initialize a matrix to store direct conflicts (adjacency matrix)
conflict_matrix = [[False] * n for _ in range(n)]

# Fill the adjacency matrix with the provided direct conflicts
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    conflict_matrix[u][v] = True
    conflict_matrix[v][u] = True

# Find the lexicographically smallest triplet (a, b, c)
for a in range(n):
    for b in range(a + 1, n):
        if not conflict_matrix[a][b]:
            continue
        for c in range(b + 1, n):
            if conflict_matrix[a][c] and conflict_matrix[b][c]:
                # Print the triplet (a+1, b+1, c+1) as units are 1-indexed
                print(a + 1, b + 1, c + 1)
                sys.exit(0)