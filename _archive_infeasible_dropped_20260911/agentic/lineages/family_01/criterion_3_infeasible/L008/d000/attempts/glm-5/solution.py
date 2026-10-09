import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))

    # Sort edges by (u, v) so we process in lexicographic order of the first two vertices.
    edges.sort()

    # For each edge (u, v), find the smallest common neighbor w > v.
    # Since edges are sorted by (u, v), the first triangle found is lexicographically minimal.
    for u, v in edges:
        # Iterate over neighbors of u that are > v (to ensure u < v < w).
        # We want the smallest such w that is also a neighbor of v.
        # To optimize, iterate over the smaller adjacency set.
        if len(adj[u]) <= len(adj[v]):
            smaller = adj[u]
            larger = adj[v]
        else:
            smaller = adj[v]
            larger = adj[u]

        # We need w > v and w in both adj[u] and adj[v].
        # Since we want the smallest w, iterate in sorted order.
        # But iterating in sorted order over a set is O(k log k).
        # Instead, we can iterate and track the minimum.
        min_w = None
        for w in smaller:
            if w > v and w in larger:
                if min_w is None or w < min_w:
                    min_w = w
        if min_w is not None:
            print(f"{u} {v} {min_w}")
            return

    # Should never reach here per problem guarantees.
    print("-1 -1 -1")

solve()