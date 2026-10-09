import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full = (1 << (n + 1)) - 1
    best = None

    for a in range(1, n + 1):
        if best is not None and a > best[0]:
            break
        adj_a = adj[a]
        # candidates b > a
        b_mask = adj_a & ~((1 << (a + 1)) - 1)
        b = a + 1
        while b_mask:
            # isolate lowest set bit >= b
            shifted = b_mask >> b
            if shifted == 0:
                break
            low = shifted & -shifted
            b = (b.bit_length() - shifted.bit_length()) + low.bit_length()
            b_mask &= ~(1 << b)
            common = adj_a & adj[b]
            # candidates c > b
            c_mask = common & ~((1 << (b + 1)) - 1)
            if c_mask:
                shifted = c_mask >> (b + 1)
                low = shifted & -shifted
                c = b + 1 + low.bit_length()
                if best is None or (a, b, c) < best:
                    best = (a, b, c)
                    break
            b += 1

    print(best[0], best[1], best[2])

solve()