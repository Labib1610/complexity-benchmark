import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency matrix as bitsets (Python integers)
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Try all possible a, then b, then c in lexicographic order
    for a in range(1, n + 1):
        # candidates for b: neighbors of a with label > a
        bmask = adj[a] & ~((1 << (a + 1)) - 1)
        while bmask:
            # lowest set bit
            low = bmask & -bmask
            b = low.bit_length() - 1
            bmask ^= low

            # candidates for c: common neighbors of a and b with label > b
            cmask = adj[a] & adj[b] & ~((1 << (b + 1)) - 1)
            if cmask:
                lowc = cmask & -cmask
                c = lowc.bit_length() - 1
                # Since we iterate a in increasing order, b in increasing order,
                # and c is the smallest possible for this (a,b), this is lexicographically smallest
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()