import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    bits = [0] * (n + 1)          # 1‑based
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        bits[u] |= 1 << (v - 1)
        bits[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    for lst in neigh:
        lst.sort()

    for a in range(1, n + 1):
        ba = bits[a]
        for b in neigh[a]:
            if b <= a:
                continue
            common = ba & bits[b]
            # delete vertices <= b
            mask = (1 << b) - 1          # bits 0 .. b-1 are 1
            common &= ~mask
            if common:
                low = common & -common    # lowest set bit
                c = low.bit_length()      # because bits are 0‑based, gives c
                # c is already > b
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()