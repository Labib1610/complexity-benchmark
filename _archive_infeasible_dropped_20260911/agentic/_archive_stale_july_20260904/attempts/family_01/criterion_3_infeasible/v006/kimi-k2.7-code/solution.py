import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    bits = [0] * (n + 1)
    neigh = [set() for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        bits[u] |= 1 << v
        bits[v] |= 1 << u
        neigh[u].add(v)
        neigh[v].add(u)

    sorted_neigh = [None] * (n + 1)
    for i in range(1, n + 1):
        sorted_neigh[i] = sorted(neigh[i])

    for a in range(1, n + 1):
        found = False
        for b in sorted_neigh[a]:
            if b <= a:
                continue
            inter = bits[a] & bits[b]
            if inter:
                t = inter >> (b + 1)
                if t:
                    c = (t & -t).bit_length() - 1 + b + 1
                    sys.stdout.write(f"{a} {b} {c}")
                    found = True
                    break
        if found:
            break

if __name__ == "__main__":
    solve()