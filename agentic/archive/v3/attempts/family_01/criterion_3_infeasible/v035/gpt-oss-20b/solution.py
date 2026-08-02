import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adjacency = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    full_mask = (1 << n) - 1

    for a in range(n):
        neigh_a = adjacency[a]
        # iterate over neighbors b > a
        for b in range(a + 1, n):
            if not (neigh_a >> b) & 1:
                continue
            inter = neigh_a & adjacency[b]
            # mask to keep bits > b
            mask = (~((1 << (b + 1)) - 1)) & full_mask
            inter_masked = inter & mask
            if inter_masked:
                c_bit = inter_masked & -inter_masked
                c = c_bit.bit_length() - 1
                # output 1-based indices
                sys.stdout.write(f"{a+1} {b+1} {c+1}\n")
                return

if __name__ == "__main__":
    solve()