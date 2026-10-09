import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    masks = [0] * n          # bitset of neighbours
    neigh = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        masks[u] |= 1 << v
        masks[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    # ensure neighbour lists are sorted for increasing order
    for lst in neigh:
        lst.sort()

    for a in range(n):
        ma = masks[a]
        for b in neigh[a]:
            if b <= a:
                continue
            common = ma & masks[b]
            # keep only vertices > b
            common >>= (b + 1)
            if common:
                low = common & -common          # lowest set bit
                c = (low.bit_length() - 1) + (b + 1)
                # output 1‑based indices
                sys.stdout.write(f"{a+1} {b+1} {c+1}")
                return

if __name__ == "__main__":
    solve()