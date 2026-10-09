import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)  # bitmask, bits 1..n
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        if u == v:
            continue
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # For each u<v, check common neighbors w>v
    for u in range(1, n + 1):
        # iterate neighbors v>u
        mask_u = adj[u]
        v = u + 1
        while v <= n:
            if mask_u >> v & 1:
                # common neighbors of u and v
                common = adj[u] & adj[v]
                # keep only w > v
                higher = common & (~((1 << (v + 1)) - 1))
                if higher:
                    # smallest w
                    w_bit = higher & -higher
                    w = w_bit.bit_length() - 1
                    print(u, v, w)
                    return
            v += 1

if __name__ == "__main__":
    solve()