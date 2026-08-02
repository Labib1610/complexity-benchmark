import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    masks = [0] * n
    neigh = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        masks[u] |= 1 << v
        masks[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    for lst in neigh:
        lst.sort()

    for a in range(n):
        ma = masks[a]
        for b in neigh[a]:
            if b <= a:
                continue
            inter = ma & masks[b]
            shift = inter >> (b + 1)
            if shift:
                # lowest set bit after shifting
                c = (shift.bit_length() - 1) + (b + 1)
                print(a + 1, b + 1, c + 1)
                return

if __name__ == "__main__":
    solve()