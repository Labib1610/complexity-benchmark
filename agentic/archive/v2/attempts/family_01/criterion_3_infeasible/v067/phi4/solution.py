import sys

def find_smallest_triad(n, m, connections):
    # Create an adjacency matrix
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    
    for u, v in connections:
        adj[u][v] = True
        adj[v][u] = True
    
    # Check all combinations of triplets (a, b, c)
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if not adj[a][b]:
                continue
            for c in range(b + 1, n + 1):
                if adj[a][c] and adj[b][c]:
                    return a, b, c

# Read input from standard input
input = sys.stdin.read
data = input().split()
n, m = int(data[0]), int(data[1])
connections = [(int(data[i*2 + 2]), int(data[i*2 + 3])) for i in range(m)]

# Find and print the lexicographically smallest triad
a, b, c = find_smallest_triad(n, m, connections)
print(a, b, c)