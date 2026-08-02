import sys

# Read number of staff members and mutual incompatibilities
n, m = map(int, input().split())

# Create an adjacency list for the graph representation
G = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)

# Sort the neighbors of each staff member to help find lexicographically smallest triplets
for i in range(n):
    G[i] = sorted(G[i])

# Iterate over all possible pairs (a, b) and check for a valid third staff member c
for a in range(n):
    for b in G[a]:
        if a < b:  # Ensure lexicographic order a < b
            for c in G[b]:
                if a < c and c in G[a]:  # Check if a, b, c form a mutually incompatible triplet
                    print(a + 1, b + 1, c + 1)
                    sys.exit(0)