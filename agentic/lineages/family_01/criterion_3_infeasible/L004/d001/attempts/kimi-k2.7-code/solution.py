import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj_bits = [0] * n
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_bits[u] |= 1 << v
        adj_bits[v] |= 1 << u
        neighbors[u].append(v)
        neighbors[v].append(u)

    for i in range(n):
        neighbors[i].sort()

    for a in range(n):
        mask_a = adj_bits[a]
        for b in neighbors[a]:
            if b <= a:
                continue
            common = mask_a & adj_bits[b]
            if common == 0:
                continue
            shift = b + 1
            sub = common >> shift
            if sub:
                low = sub & -sub
                c = shift + low.bit_length() - 1
                sys.stdout.write(f"{a + 1} {b + 1} {c + 1}")
                return

if __name__ == "__main__":
    solve()