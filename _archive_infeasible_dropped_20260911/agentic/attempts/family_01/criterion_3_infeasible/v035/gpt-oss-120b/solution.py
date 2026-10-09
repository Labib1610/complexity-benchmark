import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_mask = [0] * n          # bit masks
    adj_list = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u
        adj_list[u].append(v)
        adj_list[v].append(u)

    for a in range(n):
        adj_list[a].sort()
        mask_a = adj_mask[a]
        for b in adj_list[a]:
            if b <= a:
                continue
            # common neighbours of a and b
            common = mask_a & adj_mask[b]
            # keep only vertices > b
            common >>= (b + 1)
            if common == 0:
                continue
            # lowest set bit -> smallest c
            low = common & -common
            c = (b + 1) + (low.bit_length() - 1)
            # output 1‑based
            sys.stdout.write(f"{a+1} {b+1} {c+1}")
            return

if __name__ == "__main__":
    solve()