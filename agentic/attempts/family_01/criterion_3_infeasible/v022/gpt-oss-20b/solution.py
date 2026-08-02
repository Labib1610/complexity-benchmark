import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)  # 1-indexed bitsets

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full_mask = (1 << (n + 1)) - 1  # bits 0..n

    for a in range(1, n - 1):
        # neighbors of a with index > a
        neigh_a = adj[a] & (~((1 << (a + 1)) - 1))
        b_bits = neigh_a
        while b_bits:
            # lowest set bit gives smallest b
            lowb = b_bits & -b_bits
            b = lowb.bit_length() - 1
            b_bits -= lowb

            # candidate c > b that is neighbor to both a and b
            cand = adj[a] & adj[b] & (~((1 << (b + 1)) - 1))
            if cand:
                lowc = cand & -cand
                c = lowc.bit_length() - 1
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()