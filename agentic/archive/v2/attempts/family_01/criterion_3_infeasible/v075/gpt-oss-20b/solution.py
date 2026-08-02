import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n  # bitmask of neighbors for each node

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        neigh_a = adj[a]
        # neighbors greater than a
        mask_ab = neigh_a >> (a + 1)
        b_bit = 0
        while mask_ab:
            if mask_ab & 1:
                b = b_bit + a + 1
                common = adj[a] & adj[b]
                common_shift = common >> (b + 1)
                if common_shift:
                    lsb = common_shift & -common_shift
                    c_offset = lsb.bit_length() - 1
                    c = c_offset + b + 1
                    # output 1-based indices
                    sys.stdout.write(f"{a+1} {b+1} {c+1}\n")
                    return
            mask_ab >>= 1
            b_bit += 1

if __name__ == "__main__":
    solve()