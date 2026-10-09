import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx+1] - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    full_mask = (1 << n) - 1

    for a in range(n):
        # mask for vertices with index > a
        mask = full_mask ^ ((1 << (a + 1))) - 1)
        S = adj[a] & mask
        remaining = S
        while remaining:
            b_bit = remaining & -remaining
            b = b_bit.bit_length() - 1
            remaining ^= b_bit
            common = remaining & adj[b]
            if common:
                c_bit = common & -common
                c = c_bit.bit_length() - 1
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    main()