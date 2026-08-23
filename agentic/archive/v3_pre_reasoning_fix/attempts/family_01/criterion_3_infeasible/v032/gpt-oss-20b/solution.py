import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [0] * n
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        # neighbors of a with index > a
        neigh_bits = adj[a] & ~((1 << (a + 1)) - 1)
        b_bits = neigh_bits
        while b_bits:
            # lowest set bit in b_bits
            b = (b_bits & -b_bits).bit_length() - 1
            # intersection of neighbors of a and b
            common = adj[a] & adj[b]
            # keep bits > b
            c_bits = common & ~((1 << (b + 1)) - 1)
            if c_bits:
                c = (c_bits & -c_bits).bit_length() - 1
                sys.stdout.write(f"{a+1} {b+1} {c+1}\n")
                return
            # remove b from b_bits
            b_bits ^= 1 << b

if __name__ == "__main__":
    main()