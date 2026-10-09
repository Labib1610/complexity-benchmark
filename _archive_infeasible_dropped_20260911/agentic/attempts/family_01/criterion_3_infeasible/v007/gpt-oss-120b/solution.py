import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_int = [0] * (n + 1)          # 1‑based
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        # set bits
        adj_int[u] |= 1 << (v - 1)
        adj_int[v] |= 1 << (u - 1)
        adj_list[u].append(v)
        adj_list[v].append(u)

    full_mask = (1 << n) - 1

    for a in range(1, n + 1):
        adj_list[a].sort()
        for b in adj_list[a]:
            if b <= a:
                continue
            common = adj_int[a] & adj_int[b]
            # keep only vertices > b
            mask = full_mask ^ ((1 << b) - 1)   # bits b .. n-1 are 1
            common &= mask
            if common:
                low = common & -common
                c = low.bit_length()            # 1‑based
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()