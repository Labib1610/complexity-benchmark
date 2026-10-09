import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    mask = [0] * n
    adj = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        mask[u] |= 1 << v
        mask[v] |= 1 << u
        adj[u].append(v)
        adj[v].append(u)

    full = (1 << n) - 1          # lower n bits are 1

    for a in range(n):
        ma = mask[a]
        for b in adj[a]:
            if b <= a:
                continue
            # vertices adjacent to both a and b
            common = ma & mask[b]
            # keep only vertices with index > b
            gt_mask = full ^ ((1 << (b + 1)) - 1)
            cand = common & gt_mask
            if cand:
                # lowest set bit -> smallest possible c
                low = cand & -cand
                c = low.bit_length() - 1
                # output in 1‑based, increasing order
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()