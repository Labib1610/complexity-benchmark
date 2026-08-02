import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * (n + 1)          # adjacency bitsets, 0 index unused
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        a_bits = adj[a]
        for b in range(a + 1, n + 1):
            # check if edge a-b exists
            if (a_bits >> (b - 1)) & 1:
                common = a_bits & adj[b]
                tmp = common >> b      # remove bits for vertices <= b
                if tmp:
                    low = tmp & -tmp   # lowest set bit in tmp
                    pos = low.bit_length() - 1
                    c = pos + b + 1
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()