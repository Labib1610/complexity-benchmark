import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    masks = [0] * (n + 1)          # 1‑based
    adj = [set() for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        masks[u] |= 1 << (v - 1)
        masks[v] |= 1 << (u - 1)
        adj[u].add(v)
        adj[v].add(u)

    full_mask = (1 << n) - 1

    for a in range(1, n + 1):
        # neighbours larger than a
        for b in sorted(v for v in adj[a] if v > a):
            common = masks[a] & masks[b]
            # keep only vertices > b
            keep = full_mask ^ ((1 << b) - 1)   # bits b..n-1 are 1
            cand = common & keep
            if cand:
                low = cand & -cand
                c_index = low.bit_length() - 1   # 0‑based
                c = c_index + 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()