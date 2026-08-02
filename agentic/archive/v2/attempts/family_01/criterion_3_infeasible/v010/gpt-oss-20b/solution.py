import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    bits = [0] * (n + 1)          # bitsets for adjacency
    neigh = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        bits[u] |= 1 << (v - 1)
        bits[v] |= 1 << (u - 1)
        neigh[u].append(v)
        neigh[v].append(u)

    for a in range(1, n + 1):
        neigh[a].sort()

    for a in range(1, n + 1):
        for b in neigh[a]:
            if b <= a:
                continue
            common = bits[a] & bits[b]
            shifted = common >> b
            if shifted:
                pos = (shifted & -shifted).bit_length() - 1
                c = pos + b + 1
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    solve()