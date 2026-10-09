import sys

def main():
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

    # We need lexicographically smallest triangle in the conflict graph.
    # n <= 2000, so O(n^3 / word) using bitsets is fine.
    # For each a from 1 to n, for each b > a that conflicts with a,
    # check if there is c > b that conflicts with both a and b.
    # To get lexicographically smallest, iterate a, then b, then c in order.
    # Use bitsets to find common neighbors quickly.

    for a in range(1, n + 1):
        # neighbors of a with index > a
        neigh_a = adj[a] & ~((1 << (a + 1)) - 1)
        # iterate b in increasing order among neighbors of a
        b_mask = neigh_a
        while b_mask:
            lsb = b_mask & -b_mask
            b = lsb.bit_length() - 1
            b_mask ^= lsb
            # common neighbors of a and b with index > b
            common = adj[a] & adj[b] & ~((1 << (b + 1)) - 1)
            if common:
                # smallest c is the lowest set bit
                c = (common & -common).bit_length() - 1
                print(a, b, c)
                return

if __name__ == "__main__":
    main()