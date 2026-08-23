import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [0] * (n + 1)
    it = iter(data[2:])
    for u, v in zip(it, it):
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    # precompute masks for b (1..n)
    masks = [0] * (n + 1)
    for i in range(n + 1):
        masks[i] = (1 << i) - 1

    for a in range(1, n - 1):
        adj_a = adj[a]
        for b in range(a + 1, n + 1):
            # check if edge a-b exists
            if (adj_a >> (b - 1)) & 1:
                inter = adj_a & adj[b]
                inter_masked = inter & ~masks[b]
                if inter_masked:
                    low = inter_masked & -inter_masked
                    c = low.bit_length() - 1 + 1  # convert to 1-based
                    sys.stdout.write(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    main()