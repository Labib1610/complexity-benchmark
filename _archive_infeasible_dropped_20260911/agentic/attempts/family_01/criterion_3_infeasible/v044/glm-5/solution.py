import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    adj = [set() for _ in range(n + 1)]
    deg = [0] * (n + 1)

    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].add(v)
        adj[v].add(u)
        deg[u] += 1
        deg[v] += 1

    # Order vertices by degree ascending; among equal degrees, by id ascending.
    order = sorted(range(1, n + 1), key=lambda x: (deg[x], x))

    # For each vertex, store neighbors that come later in `order`.
    later = [set() for _ in range(n + 1)]
    rank = [0] * (n + 1)
    for r, v in enumerate(order):
        rank[v] = r
    for v in range(1, n + 1):
        for u in adj[v]:
            if rank[u] > rank[v]:
                later[v].add(u)

    best = None

    for v in order:
        if best is not None and deg[v] >= best[0]:
            # Even if v is the smallest vertex of a triangle, the third vertex
            # has degree >= deg[v] >= best[0], so it cannot beat current best.
            continue
        L = later[v]
        if len(L) < 2:
            continue
        # Iterate neighbors u of v that come later, with u < best[1] if best set.
        for u in L:
            if best is not None and u >= best[1]:
                continue
            common = L & adj[u]
            if not common:
                continue
            if best is None:
                w = min(common)
                best = (w, u, v)
            else:
                # Need smallest w < best[0] with w in common.
                limit = best[0]
                w = None
                for c in common:
                    if c < limit and (w is None or c < w):
                        w = c
                if w is not None:
                    best = (w, u, v)
        if best is not None and best[1] == v + 1:
            # Cannot improve further: next v would be >= current best[1].
            break

    print(f"{best[2]} {best[1]} {best[0]}")

if __name__ == "__main__":
    main()