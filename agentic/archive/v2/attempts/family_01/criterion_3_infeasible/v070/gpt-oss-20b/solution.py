import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n  # bitset for each vertex (0-indexed)
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        a_bits = adj[a]
        # iterate over b > a
        for b in range(a + 1, n):
            if (a_bits >> b) & 1:
                common = a_bits & adj[b]
                shift = b + 1
                mask = common >> shift
                if mask:
                    # lowest set bit in mask
                    low = mask & -mask
                    pos = low.bit_length() - 1
                    c = pos + shift
                    print(a + 1, b + 1, c + 1)
                    return

if __name__ == "__main__":
    solve()