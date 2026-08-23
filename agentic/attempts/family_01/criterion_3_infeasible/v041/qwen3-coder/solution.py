n, m = map(int, input().split())
edges = set()
for _ in range(m):
    x, y = map(int, input().split())
    edges.add((x, y))
    edges.add((y, x))

# Create adjacency list
adj = [set() for _ in range(n + 1)]
for x, y in edges:
    adj[x].add(y)
    adj[y].add(x)

# Find the lexicographically smallest triangle
for a in range(1, n - 1):
    for b in range(a + 1, n):
        if (a, b) in edges:
            # Find common neighbors of a and b that are greater than b
            for c in range(b + 1, n + 1):
                if (a, c) in edges and (b, c) in edges:
                    print(a, b, c)
                    exit()