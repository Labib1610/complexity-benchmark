n, m = map(int, input().split())

# Create adjacency list representation
adj = [set() for _ in range(n + 1)]
edges = []

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].add(v)
    adj[v].add(u)
    edges.append((min(u, v), max(u, v)))

# Create a set of all edges for O(1) lookup
edge_set = set(edges)

# Find the lexicographically smallest triangle
result = None

# Try all pairs of nodes
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        # If a and b are connected
        if b in adj[a]:
            # Look for a third node c that connects to both
            for c in range(b + 1, n + 1):
                if c in adj[a] and c in adj[b]:
                    # Found a triangle
                    result = (a, b, c)
                    break
            if result:
                break
    if result:
        break

print(*result)