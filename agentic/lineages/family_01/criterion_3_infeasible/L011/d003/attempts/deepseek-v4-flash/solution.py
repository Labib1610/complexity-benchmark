n, m = map(int, input().split())
adj = [0] * (n + 1)
edges = []

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    adj[u] |= 1 << v
    adj[v] |= 1 << u

best = None
best_trace = None

for u, v in edges:
    common = adj[u] & adj[v]
    # We need a w such that u < v < w or u < w < v etc.
    # Since we iterate all edges, we can just check all w in common
    # and ensure ordering u < v < w or u < w < v etc.
    # But to avoid duplicates, we can enforce u < v and w > v
    if u > v:
        u, v = v, u
    # Now u < v
    # Find smallest w > v in common
    # We can iterate over bits
    while common:
        lsb = common & -common
        w = lsb.bit_length()  # gives index+1
        if w > v:
            trace = u * 10**8 + v * 10**4 + w
            if best_trace is None or trace < best_trace:
                best_trace = trace
                best = (u, v, w)
            break  # smallest w > v found for this edge
        common ^= lsb

print(best[0], best[1], best[2])