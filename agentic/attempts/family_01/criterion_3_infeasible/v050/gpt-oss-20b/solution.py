import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    base_all = (1 << n) - 1
    greater_mask = [0] * n
    for b in range(n):
        greater_mask[b] = base_all ^ ((1 << (b + 1)) - 1)

    for a in range(n):
        for b in range(a + 1, n):
            if (adj[a] >> b) & 1:
                mask = adj[a] & adj[b] & greater_mask[b]
                if mask:
                    low = mask & -mask
                    c = low.bit_length() - 1
                    print(a + 1, b + 1, c + 1)
                    return

if __name__ == "__main__":
    main()