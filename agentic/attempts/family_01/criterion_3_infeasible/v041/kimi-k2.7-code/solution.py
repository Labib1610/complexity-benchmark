import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    bits = [0] * (n + 1)
    for _ in range(m):
        x = int(next(it))
        y = int(next(it))
        adj[x].append(y)
        adj[y].append(x)
        bits[x] |= 1 << y
        bits[y] |= 1 << x
    for i in range(1, n + 1):
        adj[i].sort()
    for a in range(1, n + 1):
        ba = bits[a]
        for b in adj[a]:
            if b <= a:
                continue
            common = ba & bits[b]
            mask = ~((1 << (b + 1)) - 1)
            common &= mask
            if common:
                low = common & -common
                c = low.bit_length() - 1
                sys.stdout.write(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()