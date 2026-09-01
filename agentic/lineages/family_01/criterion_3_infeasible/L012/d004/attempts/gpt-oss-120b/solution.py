import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    masks = [0] * n               # adjacency bitsets
    adj = [[] for _ in range(n)]  # neighbour lists

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        masks[u] |= 1 << v
        masks[v] |= 1 << u
        adj[u].append(v)
        adj[v].append(u)

    for lst in adj:
        lst.sort()

    for a in range(n):
        ma = masks[a]
        for b in adj[a]:
            if b <= a:
                continue
            # vertices adjacent to both a and b
            common = ma & masks[b]
            # keep only vertices > b
            common &= ~((1 << (b + 1)) - 1)
            if common:
                low = common & -common          # lowest set bit
                c = low.bit_length() - 1
                # output in 1‑based, sorted order
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()