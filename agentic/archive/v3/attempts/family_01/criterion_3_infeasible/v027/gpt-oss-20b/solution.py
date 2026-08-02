import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    it = iter(data[2:])

    neighbors = [[] for _ in range(n + 1)]
    adj_bits = [0] * (n + 1)

    for _ in range(m):
        u = next(it)
        v = next(it)
        neighbors[u].append(v)
        neighbors[v].append(u)
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u

    for i in range(1, n + 1):
        neighbors[i].sort()

    for a in range(1, n - 1):
        for b in neighbors[a]:
            if b <= a:
                continue
            mask = (~0) << (b + 1)
            inter = adj_bits[a] & adj_bits[b] & mask
            if inter:
                lsb = inter & -inter
                c = lsb.bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}\n")
                return

if __name__ == "__main__":
    main()