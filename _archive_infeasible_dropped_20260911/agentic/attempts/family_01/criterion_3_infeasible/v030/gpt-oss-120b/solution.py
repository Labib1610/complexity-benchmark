import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_bits = [0] * n               # bitset for each vertex
    neigh = [[] for _ in range(n)]   # adjacency list (for enumeration)

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        # set bits
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for i in range(n):
        neigh[i].sort()

    # search lexicographically smallest triangle
    for a in range(n):
        for b in neigh[a]:
            if b <= a:
                continue
            common = adj_bits[a] & adj_bits[b]
            # keep only vertices > b
            mask = common >> (b + 1)
            if mask:
                low_bit = mask & -mask
                offset = low_bit.bit_length() - 1
                c = offset + b + 1
                # output in 1‑based indexing
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()