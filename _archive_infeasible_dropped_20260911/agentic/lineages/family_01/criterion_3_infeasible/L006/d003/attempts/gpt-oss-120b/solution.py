import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based
    edge_set = set()

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        edge_set.add((u, v))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if (a, b) not in edge_set:
                continue
            common = adj[a] & adj[b]
            # clear bits for vertices <= b
            mask = (1 << b) - 1          # bits 0..b-1 are 1
            common &= ~mask
            if common:
                low = common & -common
                c_idx = low.bit_length() - 1
                c = c_idx + 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()