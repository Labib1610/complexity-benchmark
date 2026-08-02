import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    masks = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)

    for lst in adj:
        lst.sort()

    mask_all = (1 << n) - 1
    for a in range(1, n + 1):
        for b in adj[a]:
            if b <= a:
                continue
            # bits for vertices > b
            mask_above_b = mask_all & ~((1 << b) - 1)
            common = masks[a] & masks[b] & mask_above_b
            if common:
                low = common & -common
                c = low.bit_length()  # index (1-based)
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()