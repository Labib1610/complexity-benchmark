n, m = map(int, input().split())

# Create adjacency list representation of the graph
# We'll store the neighbors of each node in a set for O(1) lookup
adj = [set() for _ in range(n + 1)]

# Read edges
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].add(v)
    adj[v].add(u)

# Find the lexicographically smallest triangle
result = None

# Check all combinations of three nodes
for a in range(1, n - 1):
    for b in range(a + 1, n):
        # If a and b are not connected, skip
        if b not in adj[a]:
            continue
        for c in range(b + 1, n + 1):
            # Check if all three edges exist (a-b, b-c, a-c)
            if c in adj[a] and c in adj[b]:
                # Found a triangle
                result = (a, b, c)
                break
        if result:
            break
    if result:
        break

print(result[0], result[1], result[2])