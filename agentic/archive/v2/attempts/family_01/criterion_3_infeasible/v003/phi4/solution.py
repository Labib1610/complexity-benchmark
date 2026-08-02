import sys

def find_smallest_mutually_interfering_triple(n, m, pairs):
    # Create adjacency list for graph representation
    adj = {i: set() for i in range(1, n + 1)}
    for u, v in pairs:
        if u < v:
            adj[u].add(v)
            adj[v].add(u)

    # Find the lexicographically smallest triple (a, b, c)
    for a in range(1, n + 1):
        neighbors_a = sorted(adj[a])
        for i, b in enumerate(neighbors_a):
            if b > a:
                for c in neighbors_a[i+1:]:
                    if c > b and c in adj[b] and c in adj[a]:
                        return a, b, c

# Read input
input_data = sys.stdin.read().strip().split()
n = int(input_data[0])
m = int(input_data[1])

pairs = []
index = 2
for _ in range(m):
    u = int(input_data[index])
    v = int(input_data[index + 1])
    pairs.append((u, v))
    index += 2

# Find and print the result
result = find_smallest_mutually_interfering_triple(n, m, pairs)
print(*result)