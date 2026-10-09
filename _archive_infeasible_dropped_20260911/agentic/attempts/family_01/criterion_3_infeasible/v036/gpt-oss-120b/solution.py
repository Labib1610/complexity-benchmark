import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # bitsets
    nbr = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        # set bits
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        nbr[u].append(v)
        nbr[v].append(u)

    for i in range(1, n + 1):
        nbr[i].sort()

    full_mask = (1 << (n + 1)) - 1   # bits 0..n set, we ignore bit 0

    out = []
    for a in range(1, n - 1):
        for b in nbr[a]:
            if b <= a:
                continue
            common = adj[a] & adj[b]
            # keep only vertices > b
            mask = full_mask ^ ((1 << (b + 1)) - 1)
            common &= mask
            if common:
                low = common & -common
                c = low.bit_length() - 1
                out = [a, b, c]
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()