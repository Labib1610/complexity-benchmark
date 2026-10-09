import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * (n + 1)          # 1‑based
    neighbours = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        if u < v:
            neighbours[u].append(v)
            neighbours[v].append(u)
        else:
            neighbours[v].append(u)
            neighbours[u].append(v)

    # sort neighbour lists to guarantee increasing order
    for lst in neighbours:
        lst.sort()

    full_mask = (1 << n) - 1

    for a in range(1, n + 1):
        for b in neighbours[a]:
            if b <= a:
                continue
            common = adj[a] & adj[b]
            # keep only vertices > b
            mask = full_mask ^ ((1 << b) - 1)   # bits b .. n-1 are 1
            cand = common & mask
            if cand:
                # lowest set bit
                low = cand & -cand
                c = low.bit_length()            # gives position (1‑based)
                # c is already > b because of mask
                print(a, b, c)
                return

if __name__ == "__main__":
    solve()