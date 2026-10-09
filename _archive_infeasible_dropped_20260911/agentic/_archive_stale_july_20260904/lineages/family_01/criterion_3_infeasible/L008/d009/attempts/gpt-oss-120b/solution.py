import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    mask = [0] * (n + 1)          # 1‑based
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        # set bits (0‑based inside integer)
        mask[u] |= 1 << (v - 1)
        mask[v] |= 1 << (u - 1)
        if u < v:
            adj[u].append(v)
            adj[v].append(u)
        else:
            adj[v].append(u)
            adj[u].append(v)

    # neighbours are already collected; sort them for deterministic order
    for lst in adj:
        lst.sort()

    for a in range(1, n + 1):
        ma = mask[a]
        for b in adj[a]:
            if b <= a:
                continue
            common = ma & mask[b]
            # keep only vertices > b
            shifted = common >> b
            if shifted:
                low = shifted & -shifted
                pos = low.bit_length() - 1   # 0‑based inside shifted
                c = pos + b + 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()