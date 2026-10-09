import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    masks = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        masks[u] |= 1 << v
        masks[v] |= 1 << u

    for a in range(n):
        mask_a = masks[a]
        for b in range(a + 1, n):
            if (mask_a >> b) & 1 == 0:          # edge (a,b) missing
                continue
            common = mask_a & masks[b]
            # keep only vertices with index > b
            higher = common & ~((1 << b) - 1)
            if higher:
                low = higher & -higher
                c = low.bit_length() - 1
                # output 1‑based and sorted (a<b<c already)
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()