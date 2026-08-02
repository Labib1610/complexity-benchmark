import sys

def main() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for a in range(n):
        for b in range(a + 1, n):
            if (adj[a] >> b) & 1:          # edge (a,b) exists
                inter = adj[a] & adj[b]    # common neighbors of a and b
                mask = inter >> (b + 1)    # drop indices <= b
                if mask:
                    low = mask & -mask     # lowest set bit
                    c_offset = low.bit_length() - 1
                    c = b + 1 + c_offset
                    print(a + 1, b + 1, c + 1)
                    return

if __name__ == "__main__":
    main()